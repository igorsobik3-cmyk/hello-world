def b_sort(dane):
    n = len(dane)
    for i in range(n):
        for k in range(n - i - 1):
            if dane[k] > dane[k + 1]:
                dane[k], dane[k + 1] = dane[k + 1], dane[k]
    return dane

tablica = [64, 34, 25, 12, 22, 11, 90]
print(b_sort(tablica))