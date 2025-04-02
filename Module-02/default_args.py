# def sum(n1,n2,n3 = 0) :
#     result = n1 + n2 + n3;
    # return result;
def sum(n1,n2,*n3) : # pass args
    print(n3)
    result = n1 + n2;
    return result;

print(sum(77,33,5,21,3,12))