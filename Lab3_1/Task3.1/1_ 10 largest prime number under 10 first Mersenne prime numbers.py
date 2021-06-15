from random import randrange, getrandbits

def Check_SoNguyenTo(n, k=128):
    if n <= 1:  return False
    if n <= 3:  return True

    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2

    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def is_mersenne(n):
    m=2**n-1
    if Check_SoNguyenTo(m):
        return True
    return False

list_1=[]
for i in range(2,90):
    if Check_SoNguyenTo(i,128) and is_mersenne(i):
        x=2**i-1
        list_1.append(x)

list_2=[]
for i in list_1:
    x = i -1
    while x >=2:
        if Check_SoNguyenTo(x):
            list_2.append(x)
            break
        x=x-1


print("->> 10 first Mersenne prime numbers:")
print(list_1)
print("\n->> 10 largest prime number under 10 first Mersenne prime numbers")
print(list_2)

x = 618970019642690137449562111 -1
while x >=2:
    if Check_SoNguyenTo(x):
        print(x)
        break
    x=x-1