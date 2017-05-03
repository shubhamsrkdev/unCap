class Status:
    def __init__(self,success,reason):
        self.success=success
        self.reason=reason

def login(username,password):
    from requests import post
    try:
        creds={}
        creds['username']=username
        creds['password']=password
        creds['mode']=191
        #print(creds)
        response=post("http://172.16.0.30:8090/httpclient.html",data=creds,timeout=8)
        print(response.text)
        return login_status(response.text)
    except Exception as e:
        print(e)
        return Status(False,"cannot connect to cyberoam. is the ethernet/wifi working ?")

def getCreds():
    return {'username':'lol','password':'$as'}


def login_status(response):
    try:
        from lxml import etree
        status=etree.fromstring(response)
        print(status[1].tag)
        print(status[1].text)
        if(status[1].text=='You have successfully logged in'):
            #print("logged in")
            return Status(True,"Logged In")
        elif(status[1].text=='The system could not log you on. Make sure your password is correct'):
            #print("invalid Password")
            return Status(False,"invalid Password")
        elif(status[1].text=='Your data transfer has been exceeded, Please contact the administrator'):
            return Status(False,"Data Limit exceeded")
        else:
            print("Something wierd happened")
            return Status(False,"Oops.Something wierd happened !!")
    except Exception as e:
        print("error parsing Response")
        print(e)
        return Status(False,"Error Parsing response.")

def logout(username):
    from requests import post
    try:
        creds={}
        creds['username']=username
        creds['mode']=193
        response=post("http://172.16.0.30:8090/httpclient.html",data=creds,timeout=8)
        print(response.text)
        return logout_status(response.text)
    except Exception as e:
        print(e)
        return Status(False,"No Internet. So don't bother trying ")

def logout_status(response):
    try:
        from lxml import etree
        status=etree.fromstring(response)
        print(status[1].tag)
        print(status[1].text)
        if(status[1].text=='You have successfully logged off'):
            #print("logged in")
            return Status(True,"Logged out")
        else:
            print("Something wierd happened")
            return Status(False,"Oops.Something wierd happened !!")
    except Exception as e:
        print("error parsing Response")
        print(e)
        return Status(False,"Error Parsing response.")

def save(self,creds):
    with open('cred.bin','wb') as f:
        from pickle import dump
        dump(creds,f)
def load(self):
    with open('creds.bin','rb') as f:
        from pickle import load
        return load(f)