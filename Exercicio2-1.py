list = []
soma= 0
n = 0
while (n < 10):
    num = int(input("Digite um número: "))
    if (num >= 0):
        
        list.append(num)
    n += 1
    if (num < 0 and n > 0):
        n = n -1 
   
n=0       
for n in list:
    if(n%2 == 0):
        soma += list[n]  
        print(list[n])      
print(soma)   
print(list)     