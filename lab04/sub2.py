import zmq

ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.setsockopt_string(zmq.SUBSCRIBE, "topico2")
sub.connect("tcp://localhost:5556")

while True:
    msg = sub.recv_string()
    print("%s" %(msg))

sub.close()
ctx.close()
