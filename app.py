# https://support.ptc.com/help/thingworx/edge_sdk_java/en/index.html#page/java_sdk/c_troubleshooting_websocket_disconnects.html
# https://examples.javacodegeeks.com/core-java/net/sockettimeoutexception/java-net-sockettimeoutexception-how-to-solve-sockettimeoutexception/
from websocket_server import WebsocketServer
import time

# Called for every client connecting (after handshake)
def new_client(client, server):
  pulse = 0
  print("New client connected and was given id %d" % client['id'])
  server.send_message_to_all("Hey all, a new client has joined us")
  while True:
    time.sleep(5)
    server.send_message_to_all(f"Pulse {pulse}")
    pulse += 1

  


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	if len(message) > 200:
		message = message[:200]+'..'
	print("Client(%d) said: %s" % (client['id'], message))


PORT=8080
server = WebsocketServer(port = PORT)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()
