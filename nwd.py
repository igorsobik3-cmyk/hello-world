def nwd_i(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def nwd_r(a, b):
    if b == 0:
        return a
    return nwd_r(b, a % b)

if __name__ == "__main__":
    a, b = 13, 17

    print(f"Wynik (iteracyjnie): {nwd_i(a, b)}")
    print(f"Wynik (rekurencyjnie): {nwd_r(a, b)}")
