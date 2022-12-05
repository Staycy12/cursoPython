##escriba una funcion en python que acepte una lista y 
# genere otra lista eliminando los duplicados
myList = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]
print(myList)
myList = [2, 1, 2, 3, 0, 6, 7, 6, 4, 8]

resultantList = []
 
for element in myList:
    if element not in resultantList:
        resultantList.append(element)

print(resultantList)

## escriba una funcion que acepte una lista y genere otra
#con los numeros pares

mySet = {80, 10, 50, 18, 3, 50, 8, 18, 9, 8}
print(mySet)
original_list = [80, 10, 50, 18, 3, 50, 8, 18, 9, 8]

print("Original List is: ",original_list)

convert_list_to_set = set(original_list)
print("Set is: ",convert_list_to_set)

new_list = list(convert_list_to_set)
print("Resultant List is: ",new_list)

original_list = list(convert_list_to_set)
print("Removed duplicates from original list: ",original_list)