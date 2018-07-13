class product:
    On = 0
    def turnOn(self):
        self.On = 1
    def turnOff(self):
        self.On = 0

class TV(product):
    def __init__(self,vol,ch):
        self.volume = vol
        self.channel = ch
    def setChannel(self,x):
        self.channel = x
    def setVolume(self,y):
        self.volume = y

num_sam = int(input())
num_lg = int(input())

list_s = [ TV(i,i) for i in range(1,num_sam+1)]
list_l = [ TV(j,j) for j in range(1,num_lg+1)]

while(True):
    tmplist = input()
    comlist = tmplist.split()


    if comlist[0] == 'LG' or comlist[0] == 'SS':
        if comlist[0] == 'LG':
            tmpCompany = (list_l)
        elif comlist[0] == 'SS':
            tmpCompany = (list_s)

        if comlist[2] == 'volume':
            tmpCompany[int(comlist[1])].setVolume(int(comlist[3]))
        if comlist[2] == 'channel':
            tmpCompany[int(comlist[1])].setChannel(int(comlist[3]))
    elif comlist[0] == 'PP':
        if comlist[1] == 'LG':
            tmpCompany = list_l
        elif comlist[1] == 'SS':
            tmpCompany = list_s

        if comlist[3] == 'volume':
            print(tmpCompany[int(comlist[2])].volume)
        if comlist[3] == 'channel':
            print(tmpCompany[int(comlist[2])].channel)

    elif comlist[0] == 'END':
        break