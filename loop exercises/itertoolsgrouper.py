from itertools import zip_longest

def grouper(iterable_object, count, fillvalue= None ): 
    args= [iter(iterable_object)] * count 
    return zip_longest(* args , fillvalue=fillvalue)
iterable = ["P", "Y", "T", "H","0", "N", ]    
for x in grouper(iterable, 1, ""): 
    print(*x)

def sorter(iterable_object, count, fillvalue = None): 
    args=[iter(iterable_object)]* count 
    return zip_longest(*args, fillvalue=fillvalue )
iterable= [1,2,3, 4, 5, 6, 7, 8 ] 
for x in sorter(iterable, 1, ""): 
    print(*x)     