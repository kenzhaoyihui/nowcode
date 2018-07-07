from grpc_tools import protoc

protoc.main((
    '',
    '-I  ../protos',
    '--python_out=../route_guide/',
    '--grpc_python_out=../route_guide/',
    '../protos/route_guide.proto',
))