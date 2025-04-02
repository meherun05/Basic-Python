def palindrome(numbers):
    numList = numbers.split()
    flag = True
    for num in numList:
        s = str(num)
        temp = str(int(s[::-1]))
        if(s != s[::-1]) :
            flag = False
            print(temp)
        else :
            print(temp)
    if(flag) :
        print("YES")

    else :    
        print("NO")

numbers = input();
palindrome(numbers)