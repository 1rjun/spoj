def result(char):
    mean = int(len(char)/2)
    print(char[0:mean:2])

cases = int(input())
for i in range(0,cases):
    n=input()
    result(n)
