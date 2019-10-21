include examples/mtls/keys/Makefile

__default__:
	@echo "Please specify a target to make"

GEN=python3 -m grpc_tools.protoc -I. --python_out=. --python_grpc_out=. --mypy_out=.
GENERATED=*{_pb2.py,_grpc.py,.pyi}

clean:
	rm -f grpclib/health/v1/$(GENERATED)
	rm -f grpclib/reflection/v1/$(GENERATED)
	rm -f grpclib/reflection/v1alpha/$(GENERATED)
	rm -f grpclib/channelz/v1/$(GENERATED)
	rm -f examples/helloworld/$(GENERATED)
	rm -f examples/streaming/$(GENERATED)
	rm -f examples/multiproc/$(GENERATED)
	rm -f tests/$(GENERATED)

proto: clean
	$(GEN) grpclib/health/v1/health.proto
	$(GEN) grpclib/reflection/v1/reflection.proto
	$(GEN) grpclib/reflection/v1alpha/reflection.proto
	$(GEN) grpclib/channelz/v1/channelz.proto
	cd examples && $(GEN) --grpc_python_out=. helloworld/helloworld.proto
	cd examples && $(GEN) streaming/helloworld.proto
	cd examples && $(GEN) multiproc/primes.proto
	cd tests && $(GEN) dummy.proto

release: proto
	./scripts/release_check.sh
	rm -rf grpclib.egg-info
	python setup.py sdist

server:
	@PYTHONPATH=examples python3 -m reflection.server

server_streaming:
	@PYTHONPATH=examples python3 -m streaming.server

_server:
	@PYTHONPATH=examples python3 -m _reference.server

client:
	@PYTHONPATH=examples python3 -m helloworld.client

client_streaming:
	@PYTHONPATH=examples python3 -m streaming.client

_client:
	@PYTHONPATH=examples python3 -m _reference.client
