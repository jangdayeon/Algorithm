import sys
input = sys.stdin.readline

n = input().strip()

rst = 0
a = ""
while 1:
    if(n.find("c=")==-1 and n.find("c-")==-1 and n.find("dz=")==-1 and n.find("d-")==-1 and n.find("lj")==-1 and n.find("nj")==-1 and n.find("s=")==-1 and n.find("z=")==-1):
        break
    elif(n.find("c=")!=-1):
        rst+=n.count("c=")
        n=n.replace("c="," ")
    elif(n.find("c-")!=-1):
        rst+=n.count("c-")
        n=n.replace("c-"," ")
    elif(n.find("dz=")!=-1):
        rst+=n.count("dz=")
        n=n.replace("dz="," ")
    elif(n.find("d-")!=-1):
        rst+=n.count("d-")
        n=n.replace("d-"," ")
    elif(n.find("lj")!=-1):
        rst+=n.count("lj")
        n=n.replace("lj"," ")
    elif(n.find("nj")!=-1):
        rst+=n.count("nj")
        n=n.replace("nj"," ")
    elif(n.find("s=")!=-1):
        rst+=n.count("s=")
        n=n.replace("s="," ")
    elif(n.find("z=")!=-1):
        rst+=n.count("z=")
        n=n.replace("z="," ")
    else:
        rst+=0

n = n.split()
n = (''.join(n))

rst+=len(n)
print(rst)
        