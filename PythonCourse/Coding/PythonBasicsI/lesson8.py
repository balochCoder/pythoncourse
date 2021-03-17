# #Lists
# new_list = ['a', 'b', 'c']
# print(new_list[1])
# print(new_list[-2])
# print(new_list[1:3])
# new_list[0] = 'z'
# print(new_list)

# my_list = [1,2,3]
# bonus = my_list + [5]
# my_list[0] = 'z'
# print(my_list)
# print(bonus)

# amazon_cart=[
#     'notebooks',
#     'sunglasses',
#     'toys',
#     'grapes'
# ]

# amazon_cart[0]= 'laptop'

# #Assigning amazon_cart to new cart list
# new_cart = amazon_cart
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart)

# # For Copying list we use slicing function
# new_cart = amazon_cart[:]
# new_cart[0] = 'gum'
# print(new_cart)
# print(amazon_cart) 

# #Matrix

# # using this list: 
# basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]]
# # access "Oranges" and print it:
# # You will find the answer if you scroll down to the bottom, but attempt it yourself first!

# # Solution:
# basket[1][1][0]

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# print(matrix[0][1])


# using this list, 
# basket = ["Banana", "Apples", "Oranges", "Blueberries"]

# # 1. Remove the Banana from the list
# basket.remove("Banana")
# print(basket)

# # 2. Remove "Blueberries" from the list.
# basket.pop()
# print(basket)

# # 3. Put "Kiwi" at the end of the list.
# basket.append("Kiwi")
# print(basket)

# # 4. Add "Apples" at the beginning of the list
# basket.insert(0,"Apples")
# print(basket)

# # 5. Count how many apples in the basket
# print(basket.count('Apples'))
# # 6. empty the basket
# basket.clear()
# print(basket)

#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']

new_friend = ['Stanley']
friends.extend(new_friend)
print(sorted(friends))