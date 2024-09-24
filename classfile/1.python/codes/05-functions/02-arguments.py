# 1. Positional Arguments
def greet(name, age) :
    print(f'안녕하세요. {name}님 ! {age}살이시군요.')
    
greet('harry', 20)
# greet(20. 'harry')
# 이따위로 쓰면 안되니까 docstring 필요

# greet('harry')
# TypeError: greet() missing 1 required positional argument: 'age'

# 2. Default Argument Values
def greet(name, age=20) :
    print(f'안녕하세요. {name}님 ! {age}살이시군요.')
    
greet('harry')

# 3. Keyword Arguments
def greet(name, age):
        print(f'안녕하세요, {name}님! {age}살이시군요.')


greet(name='Dave', age=35)
greet(age=35, name='Dave')
# 키워드 인자만 사용하면 가능.
# greet(age=35, 'Dave')
# 위치인자는 키워드 인자 이후에 등장할 수없다.

# 4. Arbitrary Argument Lists
def calculate_sum(*args) : # 암묵적으로 args 로 임의의 인자를 정의함
    print(args)
    print(type(args))
    
calculate_sum(1, 10, 50, 300)
    
'''
def calculate_sum(*args, params) : # 암묵적으로 args 로 임의의 인자를 정의함
    print(args)
    print(type(args))
    
calculate_sum(1, 10, 50, 300)
'''
# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs) : 
    print(kwargs)
    
print_info(name = 'eve', age = 30)

# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
