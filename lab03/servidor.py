import zmq

context1 = zmq.Context()
context2 = zmq.Context()
socket = context1.socket(zmq.REP)
socket_hb = context2.socket(zmq.REQ)
socket.connect("tcp://localhost:5556") # conecta no broker local
socket_hb.connect("tcp://localhost:5557") # porta heartbeat
msg_count = 0
hb_count = 0

while True:
    print(f"Mensagem {msg_count}:", end=" ")
    message = socket.recv()
    socket.send_string("World")
    print(f"{message}")
    msg_count += 1

    print(f"Mensagem {hb_count}:", end=" ")
    socket_hb.send(b"Vivo") # envia mensagem (request)
    mensagem = socket_hb.recv() # recebe mensagem (reply)
    print(f"{mensagem}")
    hb_count += 1
