#Xong
import time

#B1: Kiểm tra số nguyên tố nhập vào
def Miller_Rabin_Test(n):
    q = (n - 1) / 2
    k=1
    while(q%2==0):
        q = q / 2
        k+=1
    q = int(q)
    a = 2
    x = (a**q)%n
    if x==1 or x==n-1:
        return True
    else:
        for j in range(1,k):
            x = x**2 % n
            if x == n-1:
                return True
        return False

#Tìm ước chung lớn nhât
def GCD(a,b):
    if(b==0):
        return a
    else:
        return GCD(b,a%b)

#Ktra e nhập vào
def Ktra_e(e,phi_n):
    if e >= phi_n or e <2:
        return False
    if GCD(phi_n,e)==1:
        return True
    return False

def Tim_d(e,phi_n):
    temp=phi_n
    x1=0
    x2=1
    while(True):
        qi=phi_n//e
        ri=phi_n-e*qi
        if ri==0 and xi <0:
            return xi+temp
        elif ri==0 and xi >0:
            return xi
        xi = x1 - (x2 * qi)
        phi_n=e
        e=ri
        x1=x2
        x2=xi

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

#Mã hoá RSA - 1 kí tự
# def encrypt_1character(data,e,n):
#     c=data**e%n
#     return c
def encrypt_1character(data,e,n):
    c=ChiaLayDu(data,e,n)   #c=data**e%n
    return c

#Giải mã RSA - 1 kí tự
# def chia2(input):
#     if input%2!=0:
#         input-=1
#     while(input%2==0):
#         input=int(input/2)
#     return input

# def decrypt(data,d,n):
#     x1=chia2(d)
#     thuong=int(d//x1)
#     du=d-thuong*x1
#     x1=data**x1%n
#     x1=x1**thuong
#     x2=data**du%n
#     ketqua=(x1*x2)%n
#     # ketqua=((((data**x1)%n)**thuong)*((data**du)%n))%n
#     return ketqua
def decrypt(data,d,n):
    ketqua=ChiaLayDu(data,d,n)  #m=data**d%n
    return ketqua

#Mã hoá RSA chuỗi
def encrypt_RSA1(pt,e,n):
    l=[]
    for i in pt:
        i=ord(i)
        i = encrypt_1character(i,e,n)
        l.append(i)
    return l

#Giải mã RSA chuỗi
def decrypt_RSA1(ct,d,n):
    pt=""
    for i in ct:
        i = decrypt(i,d,n)
        i=chr(i)
        pt+=i
    return pt


#Ktra p,q
check=False
while(check==False):
    p=int(input("Nhap so nguyen to p: "))
    check=Miller_Rabin_Test(p)
    if check ==False:
        print("p khong hop le")

check=False
while(check==False):
    q=int(input("Nhap so nguyen to q: "))
    check=Miller_Rabin_Test(q)
    if check ==False:
        print("q khong hop le")

n=p*q
phi_n=(p-1)*(q-1)
print("p: ",p)
print("q: ",q)
print("n: ",n)
print("phi_n: ",phi_n)

#Ktra e
check=False
while(check==False):
    e=int(input("Nhap so e: "))
    check=Ktra_e(e,phi_n)
    if check ==False:
        print("e khong hop le")


print("==================================")
start=time.time()
d=Tim_d(e,phi_n)
pt="Cong Nghe Thong Tin - UIT"
print("p: ",p)
print("q: ",q)
print("n: ",n)
print("Phi_n: ",phi_n)
print("e: ",e)
print("d: ",d)
cipher=encrypt_RSA1(pt,e,n)
print("cipher:",cipher)
plaintext=decrypt_RSA1(cipher,d,n)
print("plaintext: ",plaintext)
print("x: ",plaintext)
print("Time: ",time.time()-start)


# e:  7
# p:  1000081
# q:  1000037
# n:  1000118002997
#phi_n:  1000116002880


