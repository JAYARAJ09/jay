t =raw_input()
t=t.split()
for num in range(int(t[0])+1,int(t[1])):  
   if num > 1:  
       for i in range(2,num):  
           if (num % i) == 0:  
               break  
       else:  
           print(num) 
