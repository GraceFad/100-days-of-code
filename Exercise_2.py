### Python If-else

i = int(input())

if i >= 1 and i <= 100:
    if (i%2) != 0:
        print('Weird')
    else:
        if i >= 2 and i <= 5:
            print("Not Weird")
        elif i >= 6 and i <=20:
            print('Weird')
        elif i>20:
            print('Not Weird')
else: 
    print('Input a valid number')
