#list data type
l=[1,2,3,43,45,5]

l1=list() #empty list
l1=[] #empty list

l1.append(1) #add element at end
l1.append(2)
l1.append(3)
l1.append(4)
print(l1)

l1.insert(1,5) #insert element 5 at 1st index
print(l1)

print(l1.index(5,0)) #we will get index of element of 5 from starting index 
#print(l1.index(5,2)) #raises value error if element not present

print(l1.pop(1)) #return element at index 1
print(l1.pop())  #return last element

l1.remove(1)   #remove 1 element from list
print(l1)

print(l1.count(2)) #return count of element 2

l1.sort() #sort in increasing order
print(l1)
l1.sort(reverse=True)
print(l1)

l1.clear() #empty the list
print(l1)

l=[1,2,3]*3  #replication of list
print(l)

del l[2] #delete element at index 2
print(l)

print(l[2:6]) #print elements from 2nd index to 5th index
print(l[-2])  #print 2nd element from last
print(l[1:7:2]) #print elements from 1st index to 6th index with increment 2

print(len(l)) #length of list

for i in l :
    print(i) #print every element of list

for i,j in enumerate(l) :
    print("the element at {} position is {}".format(i,j)) #print element with index

print(2 in l) #checking element existance

print(any(l)) #if any element is true then returns true
print(all(l)) #if all elements are true then returns true

print(l[::-1]) #print list in reverse order
print(l+l)   #concatenation of two lists

l1=[1,2,3,4]
l2=[5,6,7,8,9]

for i ,j in zip(l1,l2) : 
    print(i,j) #print element to element in both the lists with least length list

l=[11,3,4,55,6,3,5,4]
print(list(set(l))) #removing duplicates in list

print(l1<l2) #comparisons of two lista
print(l1<=l2)
print(l1==l2)
print(l1>l2)
print(l1>=l2)
print(l1!=l2)
