ch='y'
while (ch=='y' or ch=='Y'):
    nums= eval(input("Enter the array elements: "))
    c='y'
    while(c=='y' or c=='Y'):
        s = eval(input("Enter element to search: "))
        idx= []
        for i,val in enumerate(nums):
            if val==s:
                idx.append(i)
        if (len(idx)==0):
            print("No matching elements")
        else:
            print("Matching elements at {}".format(idx))
        c=input("Would you like to search again? (y/n): ")
    ch=input("Would you like to retry? (y/n): ")
