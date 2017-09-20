import asyncio
import datetime
import random
import websockets
import devicesql
import json
from aiocoap import *
connected=set()


async def coapsend(uri):
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri=uri)

    try:
        response = protocol.request(request).response
    except Exception as e:
        print('Failed to coapsend')
        print(e)

def states_now():
	state_device=devicesql.state_now()
	istate={'room':{'light':state_device[0],'temp':state_device[2]},'door':{'lock':state_device[1]}}
	sendtoui=json.dumps({'state':{'reported':istate,'desired':istate}})
	return sendtoui

async def time(websocket, path):
    while True:
        global connected
        connected.add(websocket)

        msg = await websocket.recv()
        print(msg)
        if msg=="{}" or msg=="state":
            sendtoui=states_now()
            await asyncio.wait([ws.send(sendtoui) for ws in connected])#           
        else:
            statenew=json.loads(msg)
            for key in statenew:
                if key=="desired":
                    for endpoint in statenew[key]:
                        for oid in statenew[key][endpoint]:
                            newvalue=statenew[key][endpoint][oid]
                            print(newvalue)
                            devicesql.update_state("ui",oid,newvalue)
                            uri='coap://localhost/'+endpoint+'/'+oid
                            await asyncio.wait([coapsend(uri)])

                else:
                    print("wrong message")

                    
#        except websockets.ConnectionClosed:
#            pass
def start():
    start_server = websockets.serve(time, '127.0.0.1', 5678)
    print("websocket start")
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()