import time
import zmq
import random
ctx = zmq.Context.instance()
pub = ctx.socket(zmq.PUB)
pub.connect("tcp://localhost:5555")

while True:
    numero = random.randint(0,19)
    topico2 = 'topico2'
    print(f"msg: {numero}")
    pub.send_string("%s %s" %(topico2, numero))
    time.sleep(1)

ctx.close()
pub.close()
