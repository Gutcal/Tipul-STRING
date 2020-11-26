c=str(input("introduceti CNP: "))
d=0
for i in c:
    if (ord(i)>=48) and (ord(i)<=57):
        d+=1
if d==13:
    print("SIRUL E UN CNP")
else:
    print("gresit")