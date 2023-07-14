#The first n elements of an input array in increasing order and the last k elements in decreasing order
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1)/2)-1
    a[mid], a[n-1] = a[n-1], a[mid]

    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return
#Determine which player will win the tower Breakers game, 1 if the first player win, otherwise 2
def towerBreakers(n, m):
    if n%2==0:
        return 2
    elif m==1:
        return 2
    else:
        return 1

# CaesarCipher implementation
def caesarCipher(s, k):
    s2=''
    alp='abcdefghijklmnopqrstuvwxyz'

    for i in range(len(s)):
        char = s[i]
        # Encrypt uppercase characters
        if char.isupper():
            s2 += chr((ord(char) + k-65) % 26 + 65)
 
        # Encrypt lowercase characters
        elif char in alp:
            s2 += chr((ord(char) + k - 97) % 26 + 97)
        else:
            s2 += char
    return s2
    
#test_cases = int(input())
#for cs in range (test_cases):
#    n = int(input())
#    a = list(map(int, input().split()))
#    findZigZagSequence(a, n)

n=2 #n towers
m=6 #m height of each tower
print(towerBreakers(n,m))

#s='There\'s-a-starman-waiting-in-the-sky'
#k=3
s='www.abc.xy'
k=87
print(caesarCipher(s,k))