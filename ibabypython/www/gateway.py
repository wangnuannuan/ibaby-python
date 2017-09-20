import httpserver
from multiprocessing import Process
import coapserver
import websocketserver

state=0
newstate=0

p1=Process(target=httpserver.start)
p2=Process(target=coapserver.start)
p3=Process(target=websocketserver.start)
p1.start()
p2.start()
p3.start()
