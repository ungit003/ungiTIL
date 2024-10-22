### 문제 10. (서술형) Django의 Form과 ModelForm의 차이점을 설명하고, 각각 어떤 상황에서 사용하는 것이 적절한지 서술하시오.

Form : DB에 저장하지 않아도 될 때 사용
ModelForm : DB에 저장해야 할 때 사용

### 문제 11. (서술형) Django의 MTV 패턴을 기반하여 HTTP 요청 응답이 반환되기까지의 흐름을 서술하시오.

1. client가 url를 request
2. url 에 맞는 view 함수 출력
3. view 함수 출력 과정에서 models와 templates를 통해 필요한 db와 html을 불러옴
4. client에게 html을 통해 필요한 db와 함께 response
