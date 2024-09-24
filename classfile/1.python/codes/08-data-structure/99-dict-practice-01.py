# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    blood_number = {}
    blood_number['A'] = blood_types.count('A')
    blood_number['B'] = blood_types.count('B')
    blood_number['O'] = blood_types.count('O')
    blood_number['AB'] = blood_types.count('AB')
    return blood_number


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    blood_number = {'A': 0, 'B': 0, 'O': 0, 'AB': 0}
    for blood_type in blood_types:
        if blood_type in blood_number:
            blood_number[blood_type] = blood_number.get(blood_type) + 1
    return blood_number


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
