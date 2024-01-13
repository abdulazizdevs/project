# 1
import math
def floating_point_format(num):
    exponent = math.floor(math.log10(abs(num)))
    mantissa = num / 10**exponent
    print("x =",mantissa,"* 10^",exponent)
num = float(input("Sonni kiriting: "))
floating_point_format(num)

# 2
num = int(input("Birinchi sonni kiriting: "))
num_1 = int(input("Ikkinchi sonni kiriting: "))
num_2 = int(input("Uchinichi sonni kiriting: "))
summ = ((num + num_1)+abs(num - num_1)) // 2
if summ > num_2:
  print("Eng katta son",summ)
else:
  print("Eng katta son",num_2)


# 3
def inverse_num_2(num):
  inverse_num = 0
  while num > 0:
      qoldiq = num % 10
      inverse_num = inverse_num * 10 + qoldiq
      num = num // 10
  return inverse_num
first_num = int(input("Birinchi sonni kiriting: "))
second_num = int(input("Ikkinchi sonni kiriting: "))
num_1 = inverse_num_2(first_num)
num_2 = inverse_num_2(second_num)
print("Birinchi songa teskari son:",num_1)
print("Ikkinchi songa teskari son:",num_2)
summ = first_num + second_num
inverse_summ = inverse_num_2(summ)
print("Yig'indi:",summ)
print("Yig'indiga teskari son:",inverse_summ)

# 5
first_n = int(input("Birinchi sonni kiriting: ")) 
first_num_count = 0
temp = first_n
while temp > 0:
  first_num_count += 1
  temp = temp // 10
if first_num_count < 3:
  print("Birinchi sondagi raqamlar soni uchtadan kam.")
else:
  last_digit = first_n % 10
  first_digit = first_n // 10  
  (first_num_count - 1)
  between_digits = first_n % 10  
  (first_num_count - 1) // 10
  first_n = last_digit * 10  
  (first_num_count - 1) + between_digits * 10 + first_digit
print('O’zgartirilgan birinchi son: ', first_n)
def num1():
  second_n = int(input("\nIkkinchi sonni kiriting: "))
  second_num_count = 0 
  temp = second_n
  while temp > 0:
    second_num_count += 1 
    temp = temp // 10
  if second_num_count < 4:
    print("Ikkinchi sondagi raqamlar soni to‘rttadan kam.") 
  else:
    last_digit = second_n % 10
    first_digit = second_n // 10  
    (second_num_count - 1) 
    between_digits = second_n % 10  
    (second_num_count - 1) // 10
    second_n = last_digit * 10  
    (second_num_count - 1) + between_digits * 10 + first_digit 
  print('O’zgartirilgan ikkinchi son: ', second_n)
  print('\nSonlar yig’indisi: ', first_n + second_n)
num1()

# 6
num = float(input("Boshlang'ich amplitudani kiriting: "))
num_1 = float(input("To'xtash amplitudasini kiriting: "))
summ = 0
while True:
  num -= ((num*8.4)/100)
  summ += 1
  if num <= num_1:
    break
print("Mayatnik",summ,"ta tebranishdan keyin to'xtagan deb hisoblanadi.")


