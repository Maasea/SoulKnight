import socket
import re

def start(player):
	palyerAddr = []
	sendPort = 23333
	hostRecv = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	dataSend = []
	hostRecv.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST or socket.SO_REUSEADDR, 1)
	pattern="^((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}$"
	for addr in player:
		staddr=addr.strip()
		if (staddr==""):
			continue
		re_addr=re.match(pattern,staddr)
		if(re_addr):
			print("Add player:{}".format(re_addr.group()))
			palyerAddr.append((re_addr.group(), sendPort))
			dataSend.append(socket.socket(socket.AF_INET, socket.SOCK_DGRAM))
		else:
			print("Player {} ip invalid".format(player.index(addr)))
	if (len(palyerAddr)==0):
		print("Insufficient player")
		return
	if(len(palyerAddr)>3):
		print("Invilide player")
		return
	try:
		hostRecv.bind(("", sendPort))
	except Exception as e:
		print("\nPort has been occupied")
		return
	print("\nrelay  start...")
	while (True):
		for i in range(len(palyerAddr)):
			hostData, hostAddr = hostRecv.recvfrom(1024)
			if (len(hostData) > 0 and hostAddr[0] not in player):
				dataSend[i].sendto(hostData, palyerAddr[i])
				print("send to ", palyerAddr[i])

if __name__ == '__main__':
	playIp1="" #成员ip
	playIp2=""
	playIp3=""
	player= [playIp1,playIp2,playIp3]
	start(player)

