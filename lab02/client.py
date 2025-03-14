import grpc
import calc_pb2
import calc_pb2_grpc

print("Cliente conectando com servidor")

porta = "50001"
endereco = "10.102.2"

op = int(input("Digite o operador desejado: \n 1 - Soma\n 2 - Subtração\n 3 - Divisão\n 4 - Multiplicação\n"))
_n1 = float(input("Digite o primeiro numero\n"))
_n2 = float(input("Digite o segundo numero\n"))

with grpc.insecure_channel(f"{endereco}:{porta}") as channel:
    stub = calc_pb2_grpc.GreeterStub(channel)
    resposta = stub.HelloWorld(calc_pb2.MsgCliente(operacao = op, n1 = _n1, n2= _n2))
    print(f"Resposta do servidor: {resposta.resposta}")
    



