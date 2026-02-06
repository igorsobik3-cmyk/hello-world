tab = [4, 6, 2, 1, 3]

max_value = tab[0]

for i in range(1, len(tab)):
    if tab[i] > max_value:
        max_value = tab[i]

print("Maksymalna wartosc w tablicy:", max_value)