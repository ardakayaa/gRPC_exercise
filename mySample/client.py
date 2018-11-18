import grpc

# import the generated classes
import stringer_pb2
import stringer_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = stringer_pb2_grpc.StringerStub(channel)

# create a valid request message
number = stringer_pb2.ResultRequest(text="arda",value=332)


# make the call
response = stub.addstring_id(number)

# et voil
print(response.text)
