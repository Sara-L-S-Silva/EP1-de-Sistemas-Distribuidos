import grpc
import calculator_pb2
import calculator_pb2_grpc

def run():
    channel = grpc.insecure_channel('192.168.15.16:50051')
    stub = calculator_pb2_grpc.CalculatorStub(channel)
    response = stub.Add(calculator_pb2.AddRequest(a=3, b=5))
    print("Resultado da soma:", response.result)

if __name__ == '__main__':
    run()
