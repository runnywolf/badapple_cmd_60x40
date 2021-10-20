import time,os
folderlocate = os.path.dirname(os.path.realpath(__file__)).replace("\\","/")

f = open(folderlocate+"/data.txt",mode = "r")#decoding
w = ""
c = 0
data = []
for i in f.readline().split(","):
    n = int(i)
    if n < 0:
        data.append(" "*(n*-2))
    else:
        data.append("█"*n*2)
f.close()
w = "".join(data)

data = []#split
for j in (w[5400*i:5400*(i+1)] for i in range(6539)):
    data.append("\n".join(j[120*k:120*(k+1)] for k in range(45))+"\n")

delay = 0.022#print
time.sleep(0.5)
for i in data:
    t = time.time()
    print(i)
    t = delay-time.time()+t
    if t > 0:
        time.sleep(t)
