def mergeRecursive(a,b):
    # if both strings have some value
    if len(a)>0 and len(b)>0:
        if a[0] <= b[0]:
            return a[0] + mergeRecursive(a[1:], b)
        else:
            return b[0] + mergeRecursive(a,b[1:])
   #for empty strings
    else:
        #a is not empty
        if len(a)>0:
            return a
        #b is not empty
        elif len(b)>0:
            return b
       #both a and b are empty
        else:
            return ""
def orderedMerge(a,b):
    i=0
    j=0
    output = ""
    #to merge the strings
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            output+=a[i]
            i=i+1
        else:
            output+=b[j]
            j=j+1

    while i<len(a):
        output+=a[i]
        i=i+1
        
    while j<len(b):
        output+=b[j]
        j=j+1
    return output

def main():
    a = input("Enter the first ordered string: ")
    b = input("Enter the second ordered string: ")
    print("First string: " + a)
    print("Second string: " + b)
    print("Result of recursive function: " + mergeRecursive(a,b))
    print("Result of non-recursive function: " + orderedMerge(a,b))

main()
