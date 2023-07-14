class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""

#Print the tree's preorder traversal as a single line of space-separated values
def preOrder(root):
    bin_tree=[root.info]
    current=root
    queue=[]
    while current.right or current.left or queue:
        lft=current.left
        rgt=current.right
        if lft or rgt:
            if lft:
                current=lft
                if rgt:
                    queue.append(rgt)
            else:
                current=rgt
        else:
            current=queue.pop()
        bin_tree.append(current.info)
            
    print(*bin_tree)
#Given list of strings, the set is a GOOD SET if no string is a prefix of another string, Otherwise BAD SET followed by the string being checked 
def noPrefix(words):

    trie=dict()
    for wrd in words:
        curr=trie
        for ch in wrd:
            if ch not in curr:
                curr[ch] =dict()
            curr= curr[ch]
            if '_end' in curr:
                return print('BAD SET',wrd,sep='\n')
        
        if len(curr) > 0:
            return print('BAD SET',wrd,sep='\n')
        curr['_end'] = ''
    return print('GOOD SET')

    # for i in range(len(words)):
    #     tst=words[:i]
    #     for j in tst:
    #         if words[i].startswith(j):
    #             print('BAD SET',words[i],sep='\n')
    #             return
    # return print('GOOD SET')

tree = BinarySearchTree()
#t = int(input())
#arr = list(map(int, input().split()))

#t=6
t=15
#arr=[1, 2, 5, 3, 6, 4]
arr=[1, 14,3,7,4,5,15,6,13,10,11,2,12,8,9]

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)

#========================================
#words=['aab', 'defgab', 'abcde', 'aabcde', 'bbbbbbbbbb', 'jabjjjad']
#words=['aab','aac','aacghgh','aabghgh']
#words=['ahcicghgfdbjjbecigbhghjjgaib','bfbeejfiigbjjgcbhfdchbafhjefg','ahiijecijgb','bjfjaghffdggfc','deejffci','hcjbdjccihggbaiibggibeh','cgibjegidedgiefigfi','ac','ecdefeffgbbjhgahfeccibd','bbigcficigiafcddeieihehffcijfbhhbfh','cejjgbag','acfdfdecgcbdbbfica','ihhffecbdgbjbccbacichjdjdchbhea','iihbheghjddiiaahgbceahjccghdhggacijcee','jfgcbdhdbjjcdhabh','bhfaajhjjjbgccgbahhdjhgibhgiagaeibecaeiha','gbffbdachdhdbafghhhjiaiefgdaghje','fhjabfihbjjjfhhdbghahidf','hdgfafdichcfeheijhccfcfjgfabegbbadfhajfhiffea','hfcibbgcfdfichdjfjjahfbbdegiaeiaagc','cehfiebjgfjbbbdbcjffcefjigbajejaagjaiicaae','aidic','bfbd','bhcjadfheaabhechhacej','hb','dddjgiiadejjbfdijaiccjbecgjih','ghejgcgciijagadicdjdfbbhgfdabffghjebaiechcehhhh','ddjbbdhfggeaghgbehbdidfigcf','bbagiicdibbfabbadgdacicdhacfjafigaadccfic','daahdgaahghafd','hiijbfbjccjcihgfjbbbhiaeeihcdbdcecfcgciigj','cjggfbcgeibfbedgjijbhcjaebfaddifgjghjghabiiaebfafj','fhfdgfahfidaaaagdgbbggdeafhhadebhibfcfffj','ghdgaigacjeg','cbgciibgfibdchebbdcbacachhcfb','gdddibbaajbfcajejdicdaibejgagc','aicgjhedjacffdadbcijbgdcfjje','icaj','gbgafhccdgigbj','ajfajgjajggegaiddbdibbe','ecbcjbcecgfbfeeaegaigjieag','chhaffcjiigcgijacacihig','hecjdabdfadadajdbeeaaiihdieegbcfgh','gdbeebihjdcfccd','adejeefcfajc','adae','begddfcicfhdafaicbgbhahjgbdgbjbbabegdfi','cfdeagjjhhbefhbhcgaagagabhagbg','ghjbjfi','ihiabgaigghjeijdeejhabhjejedgdeiejcjf','djciccgfigggjbjigfh','eihajadh','jjgafjajcgcfcaebhhifhafejfab','jcafaefdhegbagdchgabg','c','caebhaeiegadacceaijijjbhgidcdggdbfgdgfhch','aibeiaeigfiifebgifdeajeabjcbgjgigeaciadchjcbbjj','bjhacjjcfacbhfabgdegiibdihjihgjdcfgjgchbfebdhagdg','gdecchhifjaefdfbgdaihejafjeedjchbddhjbf','dghfigagfdjcebfa','hicbjigdfbcfj','gcdjebafgeabcijcffjegg','abgeehdibcbgbaajdaa','cdffaejacjgffjjababej','fdeibbfa']
words=['aab','defgab','abcde','cedaaa','bbbbbbbbbb','jabjjjad']
noPrefix(words)

