def subtract(n):
    product=1
    sum=0
    while(n!=0):
        d=n%10
        product=product*d
        sum=sum+d
        n=n//10

    return product-sum

print(subtract(234))    

       
