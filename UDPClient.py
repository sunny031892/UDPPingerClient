import time
import socket

server_address = ('140.114.89.43', 55556)
#socket.AF_INET using Internet Protocol , socket.SOCK_DGRAM means UDP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSocket.settimeout(1.0) #will stop after 1s if failed
#socket.AF_INET using Internet Protocol , socket.SOCK_RAW means no specific protocol, socket.IPPROTO_ICMP using ICMP
r = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
r.settimeout(1.0) #will stop after 1s if failed

message = 'ping'

for i in range(0,10):
    clientSocket.sendto(message.encode(), server_address) #(data,address)
    try:
        packet, address = r.recvfrom(1024) #recvfrom receive the data
        icmpHeaderPacket = packet[20:28] #get the ICMP header
        icmpType = icmpHeaderPacket[0] #type in header[0]
        icmpCode = icmpHeaderPacket[1] #code in header[1]
        #the message according to ICMP type and code
        if (icmpType == 3) :
            if (icmpCode == 0):
                message = 'destination network unreachable.'
            elif (icmpCode == 1):
                message = 'destination host unreachable.'
            elif (icmpCode == 2):
                message = 'destination protocol unreachable.'
            elif (icmpCode == 3):
                message = 'destination port unreachable.'
            elif (icmpCode == 4):
                message = 'Fragmentation required, and DF flag set.'
            elif (icmpCode == 5):
                message = 'Source route failed.'
            elif (icmpCode == 6):
                message = 'Destination network unknown.'
            elif (icmpCode == 7):
                message = 'Destination host unknown.'
            elif (icmpCode == 8):
                message = 'Source host isolated.'
            elif (icmpCode == 9):
                message = 'Network administratively prohibited.'
            elif (icmpCode == 10):
                message = 'Host administratively prohibited.'
            elif (icmpCode == 11):
                message = 'Network unreachable for ToS.'
            elif (icmpCode == 12):
                message = 'Host unreachable for ToS.'
            elif (icmpCode == 13):
                message = 'Communication administratively prohibited.'
            elif (icmpCode == 14):
                message = 'Host Precedence Violation.'
            elif (icmpCode == 15):
                message = 'Precedence cutoff in effect.'
        elif (icmpType == 5):
            if (icmpCode == 0):
                message = 'Redirect Datagram for the Network.'
            elif (icmpCode == 1):
                message = 'Redirect Datagram for the Host.'
            elif (icmpCode == 2):
                message = 'Redirect Datagram for the ToS & network.'
            elif (icmpCode == 3):
                message = 'Redirect Datagram for the ToS & host.'
        elif (icmpType == 8):
            message = 'Echo request (used to ping).'
        elif (icmpType == 0):
            message = 'Echo reply (used to ping).'
        elif (icmpType == 9):
            message = 'Router Advertisement.'
        elif (icmpType == 10):
            message = 'Router discovery/selection/solicitation.'
        elif (icmpType == 11):
            if (icmpCode == 0):
                message = 'TTL expired in transit.'
            elif (icmpCode == 1):
                message = 'Fragment reassembly time exceeded.'
        elif (icmpType == 12):
            if (icmpCode == 0):
                message = 'Pointer indicates the error.'
            elif (icmpCode == 1):
                message = 'Missing a required option.'
            elif (icmpCode == 2):
                message = 'Bad length.'
        elif (icmpType == 13):
            message = 'Timestamp.'
        elif (icmpType == 14):
            message = 'Timestamp reply.'
        elif (icmpType == 42):
            message = 'Request Extended Echo.'
        elif (icmpType == 43):
            if (icmpCode == 0):
                message = 'No Error.'
            elif (icmpCode == 1):
                message = 'Malformed Query.'
            elif (icmpCode == 2):
                message = 'No Such Interface.'
            elif (icmpCode == 3):
                message = 'No Such Table Entry.'
            elif (icmpCode == 4):
                message = 'Multiple Interfaces Satisfy Query.'
        print(f"ICMP Info: type={icmpType}, code={icmpCode}, message: {message}")
    except:
        pass