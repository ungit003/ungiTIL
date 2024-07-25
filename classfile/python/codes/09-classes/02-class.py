# 클래스 정의
class Person:
    blood_color = 'red' # 클래스 안에서는 변수선언이 아니라 속성을 만든 것
    
    def __init__(self, name) :
        self.name = name
    
    def singing(self) :
        return f'{self.name}이 노래합니다.'


# 인스턴스 생성
singer1 = Person('iu')

# (인스턴스) 메서드 호출
print(singer1.singing())

# 속성(변수) 접근
print(singer1.blood_color)

# 인스턴스 속성(변수) # 인스턴스를 생성할 때 부여한 속성
print(singer1.name)
