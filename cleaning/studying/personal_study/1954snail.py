'''
달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어져 있다.
다음과 같이 정수 N을 입력 받아 N크기의 달팽이를 출력하시오.

[제약사항]
달팽이의 크기 N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스에는 N이 주어진다.

[출력]
각 줄은 '#t'로 시작하고, 다음 줄부터 빈칸을 사이에 두고 달팽이 숫자를 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
T = int(input())

for i in range(T) :
    N = int(input())
    num = list(range(1, N**2 + 1))
    mat1 = [[0 for _ in range(N)] for _ in range(N)]
    print(mat1)
    print(num)
    
    while N - k > 0 :
        for j in range(N-1-2*k) :
            mat1[0+k][j] = num[j+0*(N-1)] # j + 4(N-1) 0(N-3)
        print(mat1)
        for j in range(N-1-2*k) :
            mat1[j][N-1-k] = num[j+1*(N-1)] # j + 4(N-1) + 1(N-3)
        print(mat1)
        for j in range(N-1-2*k) :
            mat1[N-1-k][N-1-j] = num[j+2*(N-1)] # # j + 4(N-1) 2(N-3)
        print(mat1)
        for j in range(N-1-2*k) :
            mat1[N-1-j][0+k] =  num[j+3*(N-1)] # # j + 4(N-1) 3(N-3)
        print(mat1)