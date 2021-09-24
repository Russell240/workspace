iterable=[10,20,30,40,50,60,70]
iter_object= iter(iterable)

while True: 
    try:
        element= next(iter_object)
        print(element)
    except StopIteration: 
        break
