#question 1

def great_devisor(a,b):
    if b==0:
        return a
    else:
        return great_devisor(b,a%b)
print(great_devisor(70,120))


        
        


    
