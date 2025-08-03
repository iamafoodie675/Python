start = int(input("enter start range: "))
end = int(input("enter end range: "))

print("Prime numbers - ")

for i in range(start,end+1):
    if i >1:
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i,end=" ")