import random as rd
import string
import Xuly
def RandQuanHe():
    g=[]
    a=list(string.ascii_lowercase)
    for i in range(rd.randint(4,8)):
        g.append(rd.choice(a))
    return "".join(sorted((set(g)))).upper() #biến list g thành str g, sau đó viết hoa lên rồi sort lại

def ListToText(a:list):
    return "".join(a)


def RandPTH(quanhe):
    quanhe=list(quanhe)
    luachon=[]
    temp1=[]
    temp2=[]
    for i in range(len(quanhe)):
        luachon.append(quanhe[i])
    for i in range(rd.randint(1,3)):
        temp1.append(rd.choice(luachon))
    for chu in list(set(temp1)):
        quanhe.remove(chu)
    try:
        for i in range(rd.randint(1,3)):
            temp2.append(rd.choice(quanhe))
    except IndexError:
        return 0
    
    temp1=ListToText(list(set(temp1)))
    temp2=ListToText(list(set(temp2)))
    value=Xuly.phuthuocham(temp1,temp2)
    return value

def main():
    RandPTH(RandQuanHe())
if __name__ == "__main__":
    main()