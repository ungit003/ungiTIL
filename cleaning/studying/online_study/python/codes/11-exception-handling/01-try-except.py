# try-except
# try :
#     result = 10/0
# except ZeroDivisionError :
    
try :
    num = int(input('숫자입력'))
except :
    print('숫자아님.')

# 복수 예외처리

try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except ValueError:
    print('숫자를 넣어주세요.')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')
except:
    print('에러가 발생하였습니다.')
    
try:
    num = int(input('100으로 나눌 값을 입력하시오 : '))
    print(100 / num)
except (ValueError, ZeroDivisionError):
    print('숫자를 넣어주세요.')
except:
    print('에러가 발생하였습니다.')