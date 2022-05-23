from asyncio.windows_events import NULL
from encodings import utf_8
from re import A
from numpy import identity
import requests
import json
from models import Staff
class StaffPut:
    
     def __init__(self, name, post, online, hashlog):  
            
            self.NameSurnameStaff = name    
            self.Post = post
            self.OnlineStatus = online
            self.HashLogpass = hashlog


class StaffEncoder(json.JSONEncoder):
        def default(self, o):
            return o.__dict__  

def getStaffs(urlstring):
    data = requests.get(urlstring)
    alist = []
    alist = json.loads(data.text)
    blist = []
    for i in alist:
        a = Staff(i['idStaff'],i['nameSurnameStaff'],i['post'],i['onlineStatus'],i['hashLogpass'])
        blist.append(a)
    return blist

def postStaff(name, post, online, hashlog,urlstring):
    # c = Customer.__init2__(nameCustomer, phoneCustomer, emailCustomer, adressCustomer)
    c = StaffPut(name, post, online, hashlog)
    

    #data = json.JSONEncoder.encode(c)
    StaffJSONData = json.dumps(c, indent=4,cls=StaffEncoder)
    # customerJSONData = json.loads(str(customerJSONData))
    StaffJSONData = json.loads(str(StaffJSONData))
    r = requests.post(urlstring,json=StaffJSONData)
    print(r)

def putStaff(idStaff,nameSurnameStaff, post, onlineStatus, hashLogpass,url):
    c = Staff(int(idStaff) ,nameSurnameStaff,post, onlineStatus, hashLogpass)
    StaffJSONData = json.dumps(c, indent=4,cls=StaffEncoder)
    StaffJSONData = json.loads(str(StaffJSONData))
    r = requests.put(url+'/'+str(idStaff),json = StaffJSONData )
    print(r.content)
    

def deleteStaff(id,url):
    r = requests.delete(url+'/'+str(id) )
    print(r)

def getStaffByName(urlstring,name):
    data = requests.get(urlstring+'/'+str(name))
    if data.status_code == 404:
        return NULL
    alist = []
    alist = json.loads(data.text)
    blist = []
    for i in alist:
        a =  Staff(i['idStaff'],i['nameSurnameStaff'],i['post'],i['onlineStatus'],i['hashLogpass'])
        blist.append(a)
    return blist

def getStaffById(urlstring,id):
    data = requests.get(urlstring+'/getbyid/'+str(id))
    if data.status_code == 404:
        return NULL
    i = json.loads(data.text)
    a =  Staff(i['idStaff'],i['nameSurnameStaff'],i['post'],i['onlineStatus'],i['hashLogpass'])
   
    return a
