def some_function(*args,**kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total


print(some_function(1,2,3,4,5, num1 =5,num2=10))

# Rule : params, *args, default params, **kwargs