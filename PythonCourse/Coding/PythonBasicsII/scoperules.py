#1
# a = 1

# def confusion():
#     a=5
#     return a

# print(a)
# print(confusion())

#2

# a = 1

# def confusion():
#     a=5
#     return a

# print(confusion())
# print(a)


# #3

# a = 1

# def parent():
#     a =10
#     def confusion(): # not a in local scope but a have a value in parent scope
#         return a
#     return confusion()
# print(parent())
# print(a)


#4

# a = 1

# def parent():
#     def confusion(): # not a in local scope not in parent scope but a have value in global scope
#         return a
#     return confusion()
# print(parent())
# print(a)


#5

a = 1

def parent():
    def confusion(): # last rule check built - in functions
        return sum  # checking sum in local first, then parent , then global and last check built-in functions
    return confusion()
print(parent())
print(a)