# function is a first class object

# we can declare function in a function and return the inner function
def double_decker():
    print('starting the double decker function')

    def inner_fn():
        print('starting inner function')
        return 3000
    return inner_fn

# print(double_decker())
# print(double_decker()())

# we also can create a function with parameter and in parameter we can pass a function and call the passing function init
def do_somthing(work):
    print('work started')
    work()
    print('work ended')

# do_somthing('i am busy')

def codding():
    print('codding in python')

do_somthing(codding)

