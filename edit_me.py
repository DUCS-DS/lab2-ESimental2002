
def monotonic(lst):
    if len(lst) <= 1:
        return True

    is_ascending = True
    is_descending = True

    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            is_ascending = False
        if lst[i] > lst[i - 1]:
            is_descending = False

    return is_ascending or is_descending

print(monotonic([12, 16, 34, 80])) 
print(monotonic([45, 12, -10, -19]))  
print(monotonic([2, 3, 2, 3]))  
print(monotonic([5, 5, 5]))  
print(monotonic([]))  
print(monotonic([1405006]))  
print(monotonic([100, 200, 150, 250, 300]))