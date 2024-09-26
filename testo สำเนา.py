
n = int(input())


years = []

for _ in range(n):
    year = int(input())
    years.append(year)


for i in years:
    if (i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(f"{i}: Y (Leap Year)")  
    else:
        print(f"{i}: N (Not a Leap Year)")  
4