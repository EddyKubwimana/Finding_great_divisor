#finding the great devisor for more than two numbers

#sorting function using recursion
def great_d(a,b):
    if a%b==0:
        return b
    else:
        b = a%b
        a = b
        return great_d(a,b)

def great_division(*args):
    number = [*args]
    stack = []
    p =0
    great = great = great_d(number[p],number[p+1])
    while True:
        p+=2
        if p<len(number):
            divisor =great_d(number[p],great)
            great = divisor
        else:
            break
    return great
    
        
        
        
    
    

print(great_division(60,60,60,60))

        
        


    
