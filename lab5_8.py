n = float(input("Введите число: "))
s = []
if n == int(n) and int(n) > 0:
    n = int(n)
    for i in range(1,n):
        if n%i == 0:
            s.append(i)
    if sum(s) == n:
        print("Число совершенное")
    else:
        print("Число несовершенное")

else:
    print("Число несовершенное")