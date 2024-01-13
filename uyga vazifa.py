# 1.1
def summa_n():
  num = int(input("Sonni kiriting: "))
  summ = 0
  max = 0
  for i in range(1,num+1):
    summ += i
  print("1 dan",num,"gacha sonlar yigindisi:",summ)
  for j in range(1,summ+1):
    max += j
  print("1 dan",summ,"gacha sonlar yig`indisi",max)
summa_n()

# 1.2
def eku_b(a, b):
  while b:
    a,b = b,a % b
  return a
birinchi_son = int(input("Birinchi sonni kiriting: "))
ikkinchi_son = int(input("Ikkinchi sonni kiriting: "))
ekub = eku_b(birinchi_son, ikkinchi_son)
print("EKUB = ",ekub)


# 1.3
number = int(input("Masalalar sonini kiriting: "))
num_1 = 0
for i in range(number):
  num = int(input("sonni kiriting: "))
  if num > num_1:
      num_1 = num
print("Qayta ishlash uchun masala: ",num_1)


# 2.3
def floating_point_numbers(x):
  if x > 10:
    a = x / 10.0
    b = 1
    while a >= 10:
        a /= 10.0
        b += 1
    print("x =",a,"*10**",b)
  else:
    print("x musbat va 10 dan kichik bo'lishi kerak")
x = float(input("Foydalanuvchi musbat x (x>10) sonni kiriting: "))
floating_point_numbers(x)


# 3.2
a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))
c = float(input("Uchinchi sonni kiriting: "))
result = round(a + b, 15) == round(c, 15)
print(result)
