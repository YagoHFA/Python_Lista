
list = []
list2 = []
l = 0
v = 0
for n in range(10):
    list.append(int(input("Digite um valor a ser armazenado: ")))
list2 = list.copy()
list2.reverse()
print(list2)
print(list)
for m in range(10):
    if(list[m] == list2[m]):
        print("valor ", list[m], "na posição ", m)    