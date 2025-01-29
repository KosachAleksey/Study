def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        print(f"Prohod № {i+1}")
        for j in range(0, n-i-1):
            print(f"Compare {arr[j]} и {arr[j+1]}")
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                print(f"Swapping places {arr[j]} and {arr[j+1]}")
            else:
                print(f"No exchange detected")
        print(f"Output the array after each pass {i+1}: {arr}\n")
        if not swapped:
            break
c = int(input("Введите значание длинны массива"))
array = [] 
for i in range(c):
    array.append(int(input("Enter the numbers in the array")))
    print(f"The original array {array}")

sorted_arr = bubble_sort(array)

print(f"sorted_arr {sorted_arr}")