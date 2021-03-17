# Scope - what variables do I have access to?
def outer():
    x = "local"

    def inner():
        nonlocal x  # it refering parent variable x
        x = "nonlocal"  # and changing value of parent local so the x value change from local to non local
        print("inner:", x)
    inner()
    print("outer:", x)


outer()

# 1 - start with local
# 2 - Parent local?
# 3 - global
# 4 - built in python functions
