def odd(n):
    i=0
    while(i<len(n)):
        if i%2==0:
            print(n[i])
        i+=1

print(odd([2,3,4,5]))