a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
if (a>=b) and (a>=c):
	largest=a
elif (b>=a) and (b>=c):
	largest=b
else:
	largest=c
print int(largest)
