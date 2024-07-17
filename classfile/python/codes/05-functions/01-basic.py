def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2

result = make_sum(100, 30)
print(result)

return_value = print(result)
print(return_value)

# 프린트는 출력은 있고 리턴은 없다.

# *교제에 없음*
def my_func():
    print('hello world')
    
result = my_func()
print(result)