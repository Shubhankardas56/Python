# program to print str like
# p
# p y
# p y t
# p y t h
# p y t h o
# p y t h o n
#..............xxx...........
lang="python"
for row in range(6):
    for col in range(row+1):
        print(lang[col],end=" ")
        print()
# program to print str like
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
print()
print()
i=1
for row in range(6):
    print(" *"*i,end=" ")
    i+=1
    print()
    print()
    print()
# program to print str like
#     * i=0
#    * * i=1
#   * * * i=2
#  * * * * i=3
# * * * * * i=4
num=int(input("Enter a number: "))
for i in range(num):
    print(" "*(num-i-1),"* "*(i+1),end="")
    print()
    print()
# program to print str like
#     * i=0
#    * * i=1
#   * * * i=2
#  * * * * i=3
# * * * * * i=4
#  * * * * i=0
#   * * * i=1
#    * * i=2
#     * i=3
num=int(input(("Enter a number: ")))
for i in range(num):
    print(" "*(num-i-1),"* "*(i+1),end="")
    print()
    for i in range(num-1):
        print(" "*(i+1),"* "*(num-i-1),end="")
        print()