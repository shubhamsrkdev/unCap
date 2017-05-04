import socket as sk
def getWebsite():
    return "www.google.com"

def getIpPort():
    sock_info=sk.getaddrinfo(getWebsite(),80,proto=sk.IPPROTO_TCP)
    return sock_info[0][-1]

def checkInternet():
    sock=sk.socket()
    sock.settimeout(1)
    try:
        sock.connect(getIpPort())
        sock.send(b'GET /HTTP/1.0\r\n\r\n')
        resp=sock.recv(8)
        sock.shutdown(1)
        sock.close()
        if(resp==b'HTTP/1.0'):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def checkSpeed():
    import psutil
    import time
    init=[psutil.net_io_counters().bytes_sent,psutil.net_io_counters().bytes_recv]
    time.sleep(1)
    final=[psutil.net_io_counters().bytes_sent,psutil.net_io_counters().bytes_recv]
    readings=[(final[0]-init[0]),(final[1]-init[1])]
    print(readings)
    if readings[0] < 200 or readings[1] < 200:
        return False
    else:
        return True
            
    