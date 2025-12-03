import random as rd
import string
def RandQuanHe():
    g=[]
    a=list(string.ascii_lowercase)
    for i in range(rd.randint(1,8)):
        g.append(rd.choice(a))
    return "".join(set(g))
def RandPTH(quanhe):
    pass

def main():
    pass
if __name__ == "__main__":
    main()