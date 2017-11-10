while True:
    x=(input("Enter a number to count to: "))
    if x=="q" or x=="Q" or x=="quit":    
        break
    x=int(x)
    y=1
    while y<=x:
        print(y)
        y=y+1
