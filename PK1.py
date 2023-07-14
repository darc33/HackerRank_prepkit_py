from math import floor

#The percentage of a positive, negative and zero in an array
def plusMinus(arr):
    pos_num=neg_mun=zer_num=0
    for i in arr:
        if i > 0:
            pos_num+=1
        elif i<0 :
            neg_mun+=1
        else:
            zer_num+=1

    print('%.6f'%(pos_num/len(arr)), "\n", '%6f'%(neg_mun/len(arr)), "\n", '%6f'%(zer_num/len(arr)))

# find the min sum and the max sum of an array
def miniMaxSum(arr):
    min_sum=max_sum=0
    arr.sort()
    min_sum=sum(arr[:len(arr)-1])
    max_sum=sum(arr[-(len(arr)-1):])
    print(min_sum, max_sum)

#Convert 12hr format to 24hr format
def timeConversion(s):
    mil_hr=int(s[:2])
    am_pm=s[-2:]
    if am_pm=="PM":
        if mil_hr!=12:
            mil_hr+=12
    else:
        if mil_hr==12:
            mil_hr='00'
        else:
            mil_hr=s[:2]

    return(f'{mil_hr}{s[2:-2]}')
#Find the median of an array
def findMedian(arr):
    arr.sort()
    return arr[floor(len(arr)/2)]

arr=[1,1,0,-1,-1]
plusMinus(arr)

arr=[1,3,5,7,9]
miniMaxSum(arr)

#s='07:05:45PM'
#s='12:01:45PM'
s='12:01:45AM'
#s='07:05:45AM'
print(timeConversion(s))

arr=[0,1,2,3,4,5,6]
print(findMedian(arr))


