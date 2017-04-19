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
        resp=sock.recv(12)
        sock.shutdown(1)
        sock.close()
        if(resp==b'HTTP/1.0 404'):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
        
    