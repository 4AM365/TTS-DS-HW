# N = int(input("Enter a number: "))
# if(N % 2 != 0):
#     print("weird")
# if(N % 2 == 0 & 2 <= N <= 5):
#     print("Not Weird")
# if(N % 2 == 0 & 6 <= N <= 20):
#     print("Weird")
# if(N % 2 == 0 & N >= 20):
#     print("Weird")


# add = lambda x, y: x + y
# print(add(1,2))

import re
data=list(input() for i in range(int(input())))
for i in data:
    print(re.sub(r'(?<=\s)(&&)(?=\s)',r"and",re.sub(r'(?<=\s)(\|\|)(?=\s)',r"or",i)))