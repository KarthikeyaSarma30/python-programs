#variable length arguments-->used when we use more arguments in function call
#than in specified parameters of function definition
def add(a,b) :
    s=a+b
    return a+b
print(add(2,3))#5
#for specifying more than two arguments in function call
def add(*a) :
    sum1=0
    print(type(a)) #<class 'tuple'>
    for i in a :
        sum1+=i
    return sum1
print(add(5,6,7)) #18
#here *args is used for many arguments and store data in type of tuple data type
def data(name,age,*h) :
    print("name is ",name)
    print("age is ",age)
    for i in h :
        print(i)
data("karthikeya",18,1,2,3,4)
#name is  karthikeya
#age is  18
#1
#2
#3
#4
#here *h will work only after the formal arguments

