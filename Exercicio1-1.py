list = []
listP = []
cont = 0
for n in range (12):
    num =int(input("Digite um número"))
    list.append(num)
    if (num >= 0):
        listP.append(num)
    else:cont +=1
print(list)
print(listP)    
print(cont)
    