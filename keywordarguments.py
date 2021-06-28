#keyword arrguments-->here we can specify the keys and also values
def fun1(**args) :
    for values in args.values() :
        print(values)
fun1(name="karthikeya",age=18,be="master")
#karthikeya
#18
#master
def fun1(**args) :
    for keys in args.keys() :
        print(keys)
fun1(name="karthikeya",age=18,be="master")
#name
#age
#be
def fun1(**args) :
    for keys,values in args.items() :
        print(keys,values)
fun1(name="karthikeya",age=18,be="master")
#name karthikeya
#age 18
#be master

def fun1(a,b,**args) : #always specify after formal arguments
    print(a+b)#11
    print(type(args))#<class 'dict'>
    for values in args.values() :
        print(values)
fun1(5,6,name="karthikeya",age=18)
#11
#<class 'dict'>
#karthikeya
#18
