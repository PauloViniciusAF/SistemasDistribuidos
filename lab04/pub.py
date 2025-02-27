import time
import zmq
import random
ctx = zmq.Context.instance()
pub = ctx.socket(zmq.PUB)
pub.connect("tcp://localhost:5555")

while True:
    msg = str(time.time())
    topico1 = "horario"
    print(f"msg: {msg}")
    pub.send_string("%s %s" % (topico1, msg))
    time.sleep(1)

ctx.close()
pub.close()
