print("Prime Numbers Using for Loop")

for value in range(1,1000):
    count = 0
    for i in range (2,Value//2 + 1):
        if( value%i == 0):
            count++;
            break;
if(count == 0 and value !=1):      
    print("%d"%value, end = " ")
