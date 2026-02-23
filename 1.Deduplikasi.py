def deduplikasi(lst):
    seen = set()
    hasil = []
    for item in lst:
        if item not in seen:
            hasil.append(item)
            seen.add(item)
    return hasil

# Contoh
print(deduplikasi([1,2,2,3,4,1,5]))