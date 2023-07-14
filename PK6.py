
from copy import copy
from heapq import heapify, heappop, heappush
def base_(mod_):
    f=[1]*(1001)
    f[1],f[2],f[3]=1,2,4
    for i in range(4,1001):
        f[i]=(f[i-1]+f[i-2]+f[i-3]+f[i-4])%mod_
    
    return f

#Make a wall of height n and width m, without holes in it, must be a solid structure and must be laid horizontally
#Return the valid wall formations modulo (10^9 + 7)
def legoBlocks(n, m): 
    mod_=10**9 +7
    sol_walls=[1]*(m+1)
    f=base_(mod_)
    pw= [pow(f[i], n, mod_) for i in range(m+1)]
    for i in range(2, m+1):
        sol_walls[i] = pw[i]
        for j in range(1,i):
            sol_walls[i] -= sol_walls[j]*pw[i-j]
            sol_walls[i] = (sol_walls[i]+mod_)%mod_
    return sol_walls[m]

#Sweetness of some cookies(A) to be greater than value k
#two cookies with the least sweetness are repeatedly mixed

def cookies(k, A):
    min_ops=0
    heapify(A)
    while len(A)>1 and A[0] < k:
        sweetness=heappop(A)+(2*heappop(A))
        heappush(A, sweetness)
        min_ops+=1


    # A.sort()
    
    # while len(A)>1 and A[0] < k:

    #     sweetness=A[0]+(2*A[1])
    #     A=A[2:]
    #     A.append(sweetness)
    #     A.sort()
    #     min_ops+=1

    return min_ops if A[0] >=k else -1

    

k=[9,7,5]
A=[[2,7,3,6,4,6], [1,2,3,9,10,12],[7]]
for i in range(len(k)):
    print(cookies(k[i],A[i]))

#=====================================================
print(legoBlocks(2, 2))
print(legoBlocks(3, 2))
print(legoBlocks(2, 3))
print(legoBlocks(4, 4))

#=====================================================
old=[]
new=[]
n=input()
#ops=['1 abcde', '1 fg', '3 6', '2 5', '4', '3 7', '4', '3 4']  
for _ in range(int(n)):
    ops=input().split(' ')
    #print(ops)
    #print('curr',new)
    #print('hist',old)
    if ops[0] == '1':
        old.append(copy(new))
        new.extend(ops[1])
        #print(new)
    elif ops[0] == '2':
        old.append(copy(new))
    elif ops[0] == '3':
        print(new[int(ops[1])-1])
    else:
        new=old.pop()



 


