def UocChungLonNhat(a,b):
    if(b==0):
        return a
    else:
        return UocChungLonNhat(b,a%b)

x=int(input("Nhap x: "))
y=int(input("Nhap y: "))

print("Uoc Chung Lon nhat: ",UocChungLonNhat(x,y))