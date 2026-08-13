#when a function calls itself repeatedly.
#recusion are same as loops.


#base case:
def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)

show(0) #(kuch bhi print nhinhoga 0 se).




#recursion function:
def show(n):
    if(n == 0):
        return
    print(n)
    show(n - 1)
    print("END")

show(5) #(5, 4, 3, 2, 1)




