import random


def binary_search_recursive(data,target,low_index,high_index):
    if low_index > high_index:
        return False
    
    mid = (low_index + high_index)//2

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data, target, low_index, mid-1)
    else:
        return binary_search(data, target, mid +1, high_index)


def binary_search_loop(data,target):
    



if __name__ == "__main__":
    data = [random.randint(0,100) for i in range(10)]
    data.sort()

    print(data)

    target = int(input("What number would you like to find? "))
    found = binary_search_recursive(data, target, 0, len(data)-1) # len devuelve el numero de elementos del array, es por eso que es necesario restarle -1 para que no arroje error de indice

    print(found)