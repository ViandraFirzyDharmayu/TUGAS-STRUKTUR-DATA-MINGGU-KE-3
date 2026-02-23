def intersection(arr1, arr2):
    set2 = set(arr2)
    hasil = []
    for item in arr1:
        if item in set2:
            hasil.append(item)
    return hasil

# Contoh
print(intersection([1,2,3,4], [3,4,5,6]))