'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()'''

'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()'''

'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(n-i-1):
        print(' ',end=' ')
    for z in range(i+1):
        print('*',end=' ')
    print()'''


'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(i):
        print(' ',end=' ')
    for z in range(n-i):
        print('*',end=' ')
    print()'''

'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==n//2 or j==n//2 or j==0 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

'''n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()'''

n=int(input("enter the size:"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
