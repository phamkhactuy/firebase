import os

path = 'C:\\Users\\pktss\\Downloads\\NewPipe-dev\\NewPipe-dev\\app\\src\\main\\java\\org\\schabi\\newpipe\\database\\playlist\\model'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.java' in file:
            files.append(os.path.join(r, file))

m = open(path+"\\All content.txt", "w")
m.close()
n = open(path+"\\All content.txt", "a")


for f in files:
    print(f)
    n.write("\n")
    n.write("#################################")
    n.write("\n")
    n.write("\n")
    a = open(f, "r")
    for x in a:
        if x.startswith('import ') or x.startswith('package ') :
            print(x)
        else :
            n.write(x)
n.close()
