def sum(num1,num2):
    def another_sum(n1,n2):
        return n1+n2
    return another_sum(num1,num2)

total = sum(10,20)

print(total)