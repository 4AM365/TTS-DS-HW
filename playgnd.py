N = int(input("Enter a number: "))
if(N % 2 != 0):
    print("weird")
if(N % 2 == 0 & 2 <= N <= 5):
    print("Not Weird")
if(N % 2 == 0 & 6 <= N <= 20):
    print("Weird")
if(N % 2 == 0 & N >= 20):
    print("Weird")
