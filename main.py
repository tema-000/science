import khi
import genmat
import norm
import time
import random

start = time.time()
file1 = open("Khi.txt", 'w')
file2 = open("Norm.txt", 'w')
file3 = open("Auxiliary.txt", 'w')

s = []
finish = []
finish2 = []
i = 0 
while i < 300:
	a = random.randint(1, 4)
	s.append(a)
	i = i + 1
m = []
i = 0
while i < 300:
	m.append(s[i])
	i = i + 1
file3.write(str(s)+"\n")
r1 = genmat.genmat(s)
m1 = norm.norm(r1, 300.0)
file3.write(str(m1)+"\n")
l = []
random.shuffle(s)
i = 0
while i < 300:
	l.append(s[i])
	i = i + 1
r2 = genmat.genmat(l)
m2 = norm.norm(r2, 300.0)
file3.write("\n"+str(l))
file3.write("\n"+str(r2))
file2.write("\n"+str(m2))
param = 0.0
param = khi.khi2(r1,r2)
file3.write("\n"+str(param))
if param < 18.0:
	finish.append(r2)
length = len(finish)
print(length)
fin = time.time()
print(fin-start)
print(len(finish))
file1.close()
file2.close()
file3.close()
