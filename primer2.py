b =raw_input()
b=b.split()
for num in range(int(b[0])+1,int(b[1])):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num) 
