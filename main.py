#REMOVE PASS AND FIX THE FUNCTION
#change to test push and forks
prods = []
def sum_of_products(list1,list2):
    for i in range(len(list1)):
        prods.append(int(list1[i]) * int(list2[i]))
        
    total = sum(prods)
    return total

if __name__ == '__main__':
   #REMOVE PASS AND YOUR CODE GOES HERE
    list1 = input().split()
    list2 = input().split()
    print(sum_of_products(list1, list2))