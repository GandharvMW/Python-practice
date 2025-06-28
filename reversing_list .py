# Method 1: Using insert at position 0
list1 = [1, 2, 3, 4, 5]
reversed_list = []
for item in list1:
    reversed_list.insert(0, item)
print("Reversed (method 1):", reversed_list)

# Method 2: Using reverse loop
reversed_list2 = []
for i in range(len(list1)-1, -1, -1):
    reversed_list2.append(list1[i])
print("Reversed (method 2):", reversed_list2)
