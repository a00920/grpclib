import socket

import pytest

from google.protobuf.descriptor_pb2 import FileDescriptorProto

from grpclib.client import Channel
from grpclib.server import Server
from grpclib.reflection.service import ServerReflection
from grpclib.reflection.v1.reflection_pb2 import ServerReflectionRequest
from grpclib.reflection.v1.reflection_pb2 import ServerReflectionResponse
from grpclib.reflection.v1.reflection_pb2 import ErrorResponse
from grpclib.reflection.v1.reflection_grpc import ServerReflectionStub

from dummy_pb2 import DESCRIPTOR
from test_functional import DummyService


@pytest.fixture(name='port')
def port_fixture():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('127.0.0.1', 0))
        _, port = s.getsockname()
    return port


@pytest.fixture(name='channel')
def channel_fixture(loop, port):
    services = [DummyService()]
    services = ServerReflection.extend(services)

    server = Server(services)
    loop.run_until_complete(server.start(port=port))

    channel = Channel(port=port)
    try:
        yield channel
    finally:
        channel.close()
        server.close()
        loop.run_until_complete(server.wait_closed())


@pytest.mark.asyncio
async def test_file_by_filename_response(channel):
    r1, r2 = await ServerReflectionStub(channel).ServerReflectionInfo([
        ServerReflectionRequest(
            file_by_filename=DESCRIPTOR.name,
        ),
        ServerReflectionRequest(
            file_by_filename='my/missing.proto',
        ),
    ])

    proto_bytes, = r1.file_descriptor_response.file_descriptor_proto
    dummy_proto = FileDescriptorProto()
    dummy_proto.ParseFromString(proto_bytes)
    assert dummy_proto.name == DESCRIPTOR.name
    assert dummy_proto.package == DESCRIPTOR.package

    assert r2 == ServerReflectionResponse(
        error_response=ErrorResponse(
            error_code=5,
            error_message='not found',
        ),
    )


@pytest.mark.asyncio
async def test_file_containing_symbol_response(channel):
    r1, r2 = await ServerReflectionStub(channel).ServerReflectionInfo([
        ServerReflectionRequest(
            file_containing_symbol=(
                DESCRIPTOR.message_types_by_name['DummyRequest'].full_name
            ),
        ),
        ServerReflectionRequest(
            file_containing_symbol='unknown.Symbol',
        ),
    ])

    proto_bytes, = r1.file_descriptor_response.file_descriptor_proto
    dummy_proto = FileDescriptorProto()
    dummy_proto.ParseFromString(proto_bytes)
    assert dummy_proto.name == DESCRIPTOR.name
    assert dummy_proto.package == DESCRIPTOR.package

    assert r2 == ServerReflectionResponse(
        error_response=ErrorResponse(
            error_code=5,
            error_message='not found',
        ),
    )


def test_all_extension_numbers_of_type_response():
    pass  # message extension is a deprecated feature and not exist in proto3


@pytest.mark.asyncio
async def test_list_services_response(channel):
    r1, = await ServerReflectionStub(channel).ServerReflectionInfo([
        ServerReflectionRequest(
            list_services='',
        ),
    ])

    service, = r1.list_services_response.service
    assert service.name == DESCRIPTOR.services_by_name['DummyService'].full_name
