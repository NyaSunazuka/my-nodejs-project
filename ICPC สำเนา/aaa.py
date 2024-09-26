
x = input()
n = []
s = []
index = 0
temp = ""
count = 1
num1 = 0
num2 = 0
for i in x:
    
    if(temp == ""):
        temp = i 
        s.append(i)
        n.append(count)
    elif(temp == i):
        count = count+1
        n[index] = count
    else:
        temp = i
        count = 1
        index = index + 1
        s.append(i)
        n.append(count)
index = 0
ans = ""
for i in (s):
    if s[index] == "7" or s[index] == "9":

        if n[index] /4 <= 1: 

            if s[index] == "7":
                if ((n[index] % 4 )== 1 ):
                    ans += "p"
                elif ((n[index] % 4 )== 2):
                    ans += "q"
                elif ((n[index] % 4 )== 3):
                    ans += "r"
                elif ((n[index] % 4 )== 0):
                    ans += "s"

            if s[index] == "9":
                if ((n[index] % 4 )== 1 ):
                    ans += "w"
                elif ((n[index] % 4 )== 2):
                    ans += "x"
                elif ((n[index] % 4 )== 3):
                    ans += "y"
                elif ((n[index] % 4 )== 0):
                    ans += "z"
        else:

            num2 = n[index] % 4 
            num3 = n[index] - num2
            num1 = int(num3 / 4)
            
            if s[index] == "7":
                if ((n[index] % 4 )== 1 ):
                    ans += "p"
                elif ((n[index] % 4 )== 2):
                    ans += "q"
                elif ((n[index] % 4 )== 3):
                    ans += "r"
                for i in range(num1):
                    ans += "s"

            if s[index] == "9":
                if ((n[index] % 4 )== 1 ):
                    ans += "w"
                elif ((n[index] % 4 )== 2):
                    ans += "x"
                elif ((n[index] % 4 )== 3):
                    ans += "y"
                for i in range(num1):
                    ans += "z"

    else:
        if n[index] /3 <= 1:  
            if s[index] == "2":
                if ((n[index] % 3 )== 1):
                    ans += "a"
                elif ((n[index] % 3 )== 2):
                    ans += "b"
                elif ((n[index] % 3 )== 0):
                    ans += "c"  
            if s[index] == "3":
                if ((n[index] % 3 )== 1):
                    ans += "d"
                elif ((n[index] % 3 )== 2):
                    ans += "e"
                elif ((n[index] % 3 )== 0):
                    ans += "f"  
            if s[index] == "4":
                if ((n[index] % 3 )== 1):
                    ans += "g"
                elif ((n[index] % 3 )== 2):
                    ans += "h"
                elif ((n[index] % 3 )== 0):
                    ans += "i"  
            if s[index] == "5":
                if ((n[index] % 3 )== 1):
                    ans += "j"
                elif ((n[index] % 3 )== 2):
                    ans += "k"
                elif ((n[index] % 3 )== 0):
                    ans += "l"  
            if s[index] == "6":
                if ((n[index] % 3 )== 1):
                    ans += "m"
                elif ((n[index] % 3 )== 2):
                    ans += "n"
                elif ((n[index] % 3 )== 0):
                    ans += "o"  
            if s[index] == "8":
                if ((n[index] % 3 )== 1):
                    ans += "t"
                elif ((n[index] % 3 )== 2):
                    ans += "u"
                elif ((n[index] % 3 )== 0):
                    ans += "v"
        else:

            num2 = n[index] % 3 
            num3 = n[index] - num2
            num1 = int(num3 / 3)
            
            if s[index] == "2":
                if ((n[index] % 3 )== 1 ):
                    ans += "a"
                elif ((n[index] % 3 )== 2):
                    ans += "b"
                for i in range(num1):
                    ans += "c"
            if s[index] == "3":
                if ((n[index] % 3 )== 1 ):
                    ans += "d"
                elif ((n[index] % 3 )== 2):
                    ans += "e"
                for i in range(num1):
                    ans += "f"
            if s[index] == "4":
                if ((n[index] % 3 )== 1 ):
                    ans += "g"
                elif ((n[index] % 3 )== 2):
                    ans += "h"
                for i in range(num1):
                    ans += "i"
            if s[index] == "5":
                if ((n[index] % 3 )== 1 ):
                    ans += "j"
                elif ((n[index] % 3 )== 2):
                    ans += "k"
                for i in range(num1):
                    ans += "l"
            if s[index] == "6":
                if ((n[index] % 3 )== 1 ):
                    ans += "m"
                elif ((n[index] % 3 )== 2):
                    ans += "n"
                for i in range(num1):
                    ans += "o"
            if s[index] == "8":
                if ((n[index] % 3 )== 1 ):
                    ans += "t"
                elif ((n[index] % 3 )== 2):
                    ans += "u"
                for i in range(num1):
                    ans += "v"
    index += 1


print(ans)

