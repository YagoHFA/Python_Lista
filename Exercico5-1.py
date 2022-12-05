list = []
list2 = []


n = int(input("Digite o tamanho do número: "))
for p in range(n):
    list.append(int(input("Digite um valor a ser armazenado: ")))
list2 = list.copy()
list2.reverse()
if(list == list2):
    print("O número é Palídromo")
else: print("O número não é Palídromo")    

