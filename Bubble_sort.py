# Bubble Sort

def Bubble(lst):
    n = len(lst)

    for i in range(n-1):
        for j in range(0,n-i-1):
            if(lst[j] > lst[j+1]):
                lst[j],lst[j+1] = lst[j+1],lst[j]

    print(" The Sorted list is :  ",lst)


lst = [23,12,98,345,987,67,22,456,66,543,45,24,99]

Bubble(lst)

# Output:-  The Sorted list is :   [12, 22, 23, 24, 45, 66, 67, 98, 99, 345, 456, 543, 987]
