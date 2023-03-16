
PORT=53
MESSAGE = "ping"
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
if client == -1:
    print("udp socket creation failed")
sock1 = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
sock1.settimeout(20)
def getServiceName(PORT, proto):
        try:
            name = socket.getservbyport(int(PORT), proto)
        except:
            return None
        return name

if sock1 == -1:
    print("icmp socket creation failed")
try:
            client.sendto(MESSAGE.encode('utf_8'), ("185.204.197.88",PORT ))
            sock1.settimeout(1)
            data, addr = sock1.recvfrom(1024)
except socket.timeout:
    serv = getServiceName(PORT, 'udp')
    if not serv:
        pass
    else:
        print('Port {}:      Open'.format(PORT))
except socket.error as sock_err:
                if (sock_err.errno == socket.errno.ECONNREFUSED):
                    print(sock_err('Connection refused'))
                client.close()
                sock1.close()
