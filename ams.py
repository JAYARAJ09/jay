a=raw_input()
a=int(a)
sum=0
temp=a
while a>0:
    rem=a%10
    sum=sum+(rem**3)
    a=a/10
if sum==temp:
    print"yes"
else:
    print'no'
