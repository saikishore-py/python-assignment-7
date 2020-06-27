#python code to find amx and minimum of a given list

lst= []

num= int(input("how many numbers:"))

for n in range (num):
    numbers= float(input('enter number list'))
    lst.append(numbers)
print("maximum elements in the list is:",max(lst))
print("minimum elements in the list is:",min(lst))