a,b = map(int,input('두 정수를 입력하시오: ').split())

c=bin(a^b)


d=int(c[:-4],2)
e=int(c[-4:],2)

print(d)
print(d*e,d*e,sep="")


