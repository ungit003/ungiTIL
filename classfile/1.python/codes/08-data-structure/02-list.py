# append : 하나씩만 받음
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)
print(my_list.append(4)) # None : 반환이 없다
my_list.append([9, 9 ,9])
print(my_list) # [1, 2, 3, 4, 4, [9, 9, 9]] ??????

# extend : 하나씩만 받음
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
print(my_list) # [1, 2, 3, 4, 5, 6] : 리스트를 풀어서 다 넣어줌
# my_list.extend(5)
# print(my_list) # TypeError: 'int' object is not iterable

# insert
my_list = [1, 2, 3]
my_list.insert(1, 5)
print(my_list)

# remove
my_list = [1, 2, 3, 2, 2, 2]
my_list.remove(2)
print(my_list)

# pop
my_list = [1, 2, 3, 4, 5]
items1 = my_list.pop()
items2 = my_list.pop(0)
print(items1) # 5
print(my_list.pop())
print(items2) # 1
print(my_list) # [2, 3, 4]

# clear
my_list = [1, 2, 3]
my_list.clear()
print(my_list)

# index
my_list = [1, 2, 3]
index = my_list.index(2)
print(index) # 1

# count
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)

# reverse : 반환이 없다 = 원본을 바꿨다
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list.reverse()) # None
print(my_list) # [1, 3, 2, 8, 1, 9]

# sort
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list) # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse = True)
print(my_list) # [100, 3, 2, 1]