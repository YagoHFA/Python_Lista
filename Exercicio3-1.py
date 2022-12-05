from xmlrpc.client import boolean


list = []
r = false = boolean
for num in range(10):
    list.append(int(input("Digite um número: ")))


while(r == false):
    n = int(input("Digite um Valor a ser procurado: ")) 

    if(n in list):
     print(list.count(n)) 
     break
    else: print("O valor digitado não é valido por favor digite outro")
