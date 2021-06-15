a = int(input("Nhap a: "))  # a^x mod p ( x> 80)
x = int(input("Nhap x: "))
p = int(input("Nhap p: "))


def ChiaLayDu(a, x, p):
    kq = 1
    a = a % p

    if (a == 0):
        return 0

    while (x > 0):

        if ((x & 1) == 1):  # Nếu x lẻ
            kq = (kq * a) % p
        x = x >> 1
        a = (a * a) % p

    return kq


print(a, "^", x, "mod", p, "=", ChiaLayDu(a,x,p))