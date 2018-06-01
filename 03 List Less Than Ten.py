a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
try:
    max_value = float(input('Print values less than: '))
    for i in a:
        if i < max_value:
            b.append(i)
    print(b)
except Exception:
    print('Input must be a number')
