import time
from socket import *

server_address = ('140.114.89.43', 55555)
#socket.AF_INET using Internet Protocol , socket.SOCK_DGRAM means UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1.0) #will stop after 1s if failed
message = 'ping'
lost_package = 0
average_rtt = 0

for i in range(0,10):
    t = time.perf_counter() #time counter
    clientSocket.sendto(message.encode(), server_address) #(data,address)
    try: 
        ret = clientSocket.recv(1024).decode('utf-8') #recv receive the data
        tmp = (time.perf_counter() - t) * 1000 #turn to ms
        average_rtt += tmp
        print("{} {} {:.3f}".format(ret, i+1, tmp))
    except:
        lost_package += 1
        print("Request timed out.")

print("Result:")
print("Average RTT", average_rtt/(10-lost_package))
print("Packet loss rate", lost_package/10)