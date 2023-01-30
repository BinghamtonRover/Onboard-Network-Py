import time

from network import ProtoClient
from generated.drive_pb2 import DriveCommand

client = ProtoClient()

data = DriveCommand(throttle=0.5, left=1.0, right=0.0)

while True: 
	client.send_message("DriveCommand", data, "localhost", 8001)
	print("Sent a message")
	time.sleep(1)
