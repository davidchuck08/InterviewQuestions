#!/usr/bin/python

class RestoreIpAddress():
    def __init__(self,str):
        self.str=str
        self.res=[]
        
    def restore(self):
        self.dfs(self.str,0,"")
    def dfs(self, substr, part, Ipvalue):
        if part==4:
            if substr == '':
                self.res.append(Ipvalue[1:])
                return
        for i in range(1,4):
            if i <= len(substr):
                if int(substr[:i])<=255:
                    self.dfs(substr[i:], part+1,Ipvalue+"."+substr[:i])
#str = '2552551135'
str='0000'
ipaddr = RestoreIpAddress(str)
ipaddr.restore()
print ipaddr.res
