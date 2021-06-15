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

def generate_prime_candidate(length):
    p = getrandbits(length)        #Random số p: theo số lượng bits (length)
    p |= (1 << length - 1) | 1
    return p

def TaoSoNguyenTo(length):
    p = 4
    while not Check_SoNguyenTo(p, 128):         #Kiểm tra xem số p phải là số nguyên tố hay không
        p = generate_prime_candidate(length)    #Nếu p không phải => tạo số p bits (bits=length)
    return p


print("So Nguyen to 2 bytes: ",TaoSoNguyenTo(16))
print("So Nguyen to 8 bytes: ",TaoSoNguyenTo(64))
print("So Nguyen to 32bytes: ",TaoSoNguyenTo(256))


