#Find the ID[a-z] of the employee who has the longest single time slot at the task
def findLongestSingleSlot(leaveTimes):
    employee="abcdefghijklmnopqrstuvwxyz"
    time_work=[[0,0]]
    time_work[0]=leaveTimes[0]
    for i in range(1,len(leaveTimes)):
        time_work.append([leaveTimes[i][0], leaveTimes[i][1]-leaveTimes[i-1][1]])
        #time_work[i][0]=leaveTimes[i][0]
        #print(time_work, i)
        #time_work[i][1]+=(leaveTimes[i][1]-leaveTimes[i-1][1])
        #print(time_work)
    
    #print(time_work[time_work.index(max(time_work, key=lambda x:x[1]))][0])
    return employee[time_work[time_work.index(max(time_work, key=lambda x:x[1]))][0]]

#amount is an array of the amount required by person i of an ATM, k the max amount at one time of the ATM
#return the order the people leave the ATM 
def getFinalOrder(k, amount):
    wdw_order=list()#[0]*len(amount)
    x_tuple=list(map(list, zip(list(range(1,len(amount)+1)), amount)))
    while x_tuple:
        if x_tuple[0][1]<=k:
            wdw_order.append(x_tuple[0][0])
            x_tuple.pop(0)
        else:
            x_tuple[0][1]-=k
            x_tuple.append(x_tuple.pop(0))

    return wdw_order


def findLowestStartingStair(jumps):
    lowest_stair=0
    i=0 
    if jumps[0]<0:
        lowest_stair-=jumps[0]
    current_stair=lowest_stair
    while i<len(jumps):
        current_stair+=jumps[i]
        if current_stair<1:
            #lowest_stair+=1
            lowest_stair-=current_stair
            current_stair=lowest_stair
            i=0
        else:            
            i+=1
            
    
    return lowest_stair

#first number employee ID, second number leave time of that employee
print(findLongestSingleSlot([[0, 3], [2, 5], [0, 9], [1, 15]]))
#print(findLongestSingleSlot([[0, 2], [1, 3], [0, 7]]))
#print(findLongestSingleSlot([[0, 1], [0, 3], [4, 5], [5, 6], [4, 10]]))

print(getFinalOrder(2, [2,5,1]))
#print(getFinalOrder(3, [1,3,2]))
#print(getFinalOrder(2, [6, 1, 2, 3, 2, 7]))

print(findLowestStartingStair([1, -6, -2, 3]))
#print(findLowestStartingStair([-5, 4, -2, 3, 1, -1, -6, -1, 0, 5]))
