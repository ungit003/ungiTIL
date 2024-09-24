my_dict_1 = {}
my_dict_2 = {'key': 'value'}
my_dict_3 = {'apple': 12, 'list': [1, 2, 3]}
my_dict_3 = {
    'apple': 12, 
    'list': [1, 2, 3]
    }

print(my_dict_1)  # {}
print(my_dict_2)  # {'key': 'value'}
print(my_dict_3)  # {'apple': 12, 'list': [1, 2, 3]}


my_dict = {'apple': 12, 'list': [1, 2, 3]}

# 딕셔너리는 키에 접근해 값을 얻어냄
print(my_dict['apple']) # dict[ ] -> value 값 뽑아내기

# 추가
my_dict['banana'] = 50
print(my_dict)

my_dict['banana'] = 1000
print(my_dict)

# 변경



a = 100
# 재할당
a = 99