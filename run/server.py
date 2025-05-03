from concurrent import futures
import grpc
import calculator_pb2
import calculator_pb2_grpc

class CalculatorServicer(calculator_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        result = request.a + request.b
        return calculator_pb2.AddReply(result=result)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    calculator_pb2_grpc.add_CalculatorServicer_to_server(CalculatorServicer(), server)
    server.add_insecure_port('0.0.0.0:50051')
    server.start()
    print("Servidor gRPC rodando em porta 50051")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
