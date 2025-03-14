from concurrent import futures
import grpc
import calc_pb2
import calc_pb2_grpc

class Greeter(calc_pb2_grpc.GreeterServicer):
    def HelloWorld(self, request, context):
        print(f"Operação do cliente: {request.operacao}")
        print(f"Primeiro número do cliente: {request.n1}")
        if(request.operacao == 1):
            _x = request.n1 + request.n2
            return calc_pb2.MsgServidor(resposta= _x)
        if(request.operacao == 2):
            _x = request.n1 - request.n2
            return calc_pb2.MsgServidor(resposta= _x)
        if(request.operacao == 3):
            _x = request.n1 / request.n2
            return calc_pb2.MsgServidor(resposta= _x)
        if(request.operacao == 4):
            _x = request.n1*request.n2
            return calc_pb2.MsgServidor(resposta= _x)
        

        return calc_pb2.MsgServidor( mensagem="World")

endereco = "[::]:50001"
servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=1))
calc_pb2_grpc.add_GreeterServicer_to_server(Greeter(), servidor)

servidor.add_insecure_port(endereco)
servidor.start()
print(f"Servidor escutando em {endereco}")
servidor.wait_for_termination()
