class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def unpack_list(sll):
    tmp_list=[]
    node=sll
    while node:
        tmp_list.append(node.data)
        node = node.next

    return tmp_list 

def mergeLists(head1, head2):
    mer_list=SinglyLinkedList()

    tmp_list=[]
    tmp_list.unpack_list(head1)
    tmp_list.extend(unpack_list(head2))
    tmp_list.sort()

    for i in tmp_list:
        mer_list.insert_node(i)

    return mer_list.head

#Determine if a s string of brackets is balances, If so YES, otherwise NO
def isBalanced(s):
    open_lst=['{', '[', '(']
    close_lst=['}',']',')']
    stck=[]
    if len(s)%2 !=0:
        return 'NO'
    for i in s:
        if i in open_lst:
            stck.append(i)
        elif i in close_lst:
            pos=close_lst.index(i)
            if len(stck) > 0 and stck[len(stck)-1] == open_lst[pos]:
                stck.pop()
            else:
                return "NO"

    if len(stck)==0:
        return "YES"
    else:
        return "NO"

        
lls1=[1,2,3]
lls2=[3,4]
llist1 = SinglyLinkedList()
llist2 = SinglyLinkedList()

for llist1_item in lls1:
    llist1.insert_node(llist1_item)

for llist2_item in lls2:
    llist2.insert_node(llist2_item)


# =========================================

# quue=[]
# for _ in range(int(input())):
#     i=input()
#     if len(i)>1:
#         quue.append(i[2:])
#     elif i[0] =="2":
#         quue.pop(0)
#     else:
#         print(quue[0])

#======================================

s=['{[()]}',  '{[(])}', '{{[[(())]]}}', '{(([])[])[]}','{(([])[])[]]}', '{(([])[])[]}[]']

for i in s:
    print(isBalanced(i))
