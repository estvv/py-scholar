array = [1, 2, 3, 4, 5]
print("Len of the array :",len(array))

for nombre in array:
    print(nombre)

####################################################
print("-------------------------------------------")
####################################################

for i in range(0, len(array)):
    print("Value :",array[i],"| Index :", i)

####################################################
print("-------------------------------------------")
####################################################

for i in range(0, len(array), 2):
    print("Value :",array[i],"| Index :", i)

####################################################
print("-------------------------------------------")
####################################################

for i in range(len(array) - 1, -1, -1):
    print("Value :",array[i],"| Index :", i)

