# def palindromeIndex(s): #Cuando hay dos seguidos escoge el menor indice y deberia escoger el mayor
#     indx=-1
#     if s!=s[::-1]:
#         for i in range(len(s)):
#             s2=s[:i]+s[i+1:]
#             if s2==s2[::-1]:
#                 if s[i]!=s[i+1]:
#                   indx=i
#                   break
#                 else:
#                   indx=i+1
#                   break
    
#     return indx

#Determine the index of a character that can be removes to make the string "s" a palindrome, 
#-1 if it is already a palindrome or there is no solution
def palindromeIndex(s):
    ret = -1
    lens = len(s)
    ind = 0
    
    if s == s[::-1]:
        return ret
    
    while ind < lens//2:
        if s[ind] != s[lens-ind-1]:
            if s[ind+1] == s[lens-ind-1] and s[ind+2] == s[lens-ind-2]:
                ret = ind
                break
            else:
                ret = lens-ind-1
                break
        ind += 1
    
    return ret

#t=['aaab', 'baa', 'aaa']
t=['quyjjdcgsvvsgcdjjyq','hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh','fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf','bsyhvwfuesumsehmytqioswvpcbxyolapfywdxeacyuruybhbwxjmrrmjxwbhbyuruycaexdwyfpaloyxbcpwsoiqtymhesmuseufwvhysb','fvyqxqxynewuebtcuqdwyetyqqisappmunmnldmkttkmdlnmnumppasiqyteywdquctbeuwenyxqxqyvf','mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm','tpqknkmbgasitnwqrqasvolmevkasccsakvemlosaqrqwntisagbmknkqpt','lhrxvssvxrhl','prcoitfiptvcxrvoalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlaorxcvtpiftiocrp','kjowoemiduaaxasnqghxbxkiccikxbxhgqnsaxaaudimeowojk']
for i in t:
	print(palindromeIndex(i))
sol=[1,8,33,23,25,44,20,-1,14,-1]