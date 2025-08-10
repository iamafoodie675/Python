m = int(input("enter the amount: "))

note100 = m // 100
print("100 Taka note:",note100)
m = m % 100

note50 = m // 50
print("50 Taka note:",note50)
m = m % 50

note20 = m // 20
print("20 Taka note:",note20)
m = m % 20

note10 = m // 10
print("10 Taka note:",note10)
m = m % 10

note5 = m // 5
print("5 Taka note:",note5)
m = m % 5

note2 = m // 2
print("2 Taka note:",note2)
m = m % 2

print("1 Taka note:",m)
