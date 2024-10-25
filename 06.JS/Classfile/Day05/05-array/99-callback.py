numbers = [1, 2, 3]


def square(num):
    return num**2


new_numbers = list(map(square, numbers))       # square를 콜백함수로 볼 수 있다.
print(new_numbers)  # [1, 4, 9]
