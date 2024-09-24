class StringUtils:
    def __init__(self) : 
        # 안에 기능이 따로 없으면 이거 안써도 파이썬이 알아서 써줌
        # 그래도 써라.
        pass
    
    @staticmethod
    def reverse_string(string) :
        return string[::-1]
    
    @staticmethod
    def Capitalize_string(string) :
        return string.capitalize()


text = 'hello, world'
result = StringUtils.reverse_string(text)
print(result)