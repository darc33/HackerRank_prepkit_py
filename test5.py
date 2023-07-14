#Determine the number of pairs of an array elements that have a difference equal to the tarket valaue k
def pairs(k, arr):
    num_pairs=0
    arr.sort()
    #tmp_arr=[]
    lft=0
    rght=1
    # for i in range(len(arr)):
    #     tmp_arr=arr[i:]
    #     #print(tmp_arr)
    #     for j in tmp_arr:
    #         if abs(arr[i]-j)==k:
    #             num_pairs+=1
    #         elif abs(arr[i]-j)>k:
    #             break

    while rght < len(arr):
        val = arr[rght]-arr[lft]
        if val == k:
            num_pairs += 1
            lft += 1
            rght += 1
        elif val < k:
            rght += 1
        else:
            lft += 1
            if lft == rght:
                rght += 1

    return num_pairs

#k=2
#arr=[1,5,3,4,2]
k=1
arr=[1,2,3,4]

print(pairs(k,arr))