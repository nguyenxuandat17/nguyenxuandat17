s=''
for i in range(2000,3201):
    
    if i%7==0 and i%5!=0 :
        if s=='':
            s=s+str(i)
        else:
            s=s+','+str(i)
print(s)
        