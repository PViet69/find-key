class phuthuocham:
    def __init__(self,left,right):
        self.left=left
        self.right=right
    def __str__(self):
        return f"{self.left} -> {self.right}"
    def __repr__(self):
        return f"{self.left} -> {self.right}"

def check(phuthuoc,desig):
    return desig in phuthuoc


def themvao(phuthuoc,desig):
    if not check(phuthuoc,desig):
        return phuthuoc+desig
    

def xulypth(phuthuoc,currentpth): #code này làm cái gì vậy??????
    soluongpth=len(currentpth)
    flag=True
    while flag==True:
        flag=False
        for i in range(soluongpth):
            Allinpth=True
            for j in range (len(currentpth[i].left)):
                if not check(phuthuoc, currentpth[i].left[j]):   #duyệt phần tử thứ j của pth i(j đi từ 0-> chiều dài của kí tự bên trái)
                    Allinpth=False
                    break
            if (Allinpth==True):
                for k in range(len(currentpth[i].right)):                   
                    if not check(phuthuoc,currentpth[i].right[k]):
                        phuthuoc=themvao(phuthuoc,currentpth[i].right[k])
                        flag = True
    return "".join(sorted(phuthuoc))


def findkey(phuthuoc,currentpth):
    temp=phuthuoc
    danhsach=sorted(phuthuoc)
    for i in range(len(phuthuoc)):
        if xulypth(phuthuoc.replace(danhsach[i],""),currentpth)==temp:
            phuthuoc=phuthuoc.replace(danhsach[i],"")
    return phuthuoc

def chuanhoa(PTH:str):
    group=[]
    try:
        handle1=PTH.strip().split(",")      #tách các pth ra
        for pth in handle1:     
            group.append(phuthuocham(pth.strip().split(" ")[0],pth.strip().split(" ")[1]))  #tách vế trái vế phải
        return group
    except Exception:
        pass
def docfile(tenfile:str):
    try:
        with open (tenfile,"r") as file:
            dongdau=file.readline().strip().upper()
            dongsau=file.readline().strip().upper()
            chuanhoa(dongsau)
            return [dongdau,dongsau]
                     
    except FileNotFoundError:
        return 1
        
def main():
    a= phuthuocham("AB","D")
    c= phuthuocham("C","B")
    group=(a,c)
    # print(a)
    # xulypth("AB",group)
    # h=findkey("ABCD",group)
    # print(h)
    n=docfile("test.txt")
    # print(n)
 
if __name__ == "__main__":
    main()