'''
별 찍기 - 10 성공분류
시간 제한	메모리 제한	제출	정답	맞은 사람	정답 비율
1 초	256 MB	23173	11834	8552	50.862%
문제
재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.

크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.

***
* *
***
N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.

입력
첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.

출력
첫째 줄부터 N번째 줄까지 별을 출력한다.
'''

# 1. 재귀

def star(n):
    global Map
    if n==3:
        Map[0][:3]=[1]*3
        Map[1][:3]=[1,0,1]
        Map[2][:3]=[1]*3
        return
    a=n//3
    star(a)

    for i in range(3):
        for j in range(3):
            if i==1 and j==1:
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*(j+1)]=Map[k][:a]

n=int(input())
Map=[[0]*n for _ in range(n)]
star(n)

for i in range(n):
    for j in range(n):
        if Map[i][j]:
            print("*",end="")
        else:
            print(" ",end="")
    print()


# 다른풀이

n=int(input())

def star(i,j):
    while i:
        if i%3==1 and j%3==1:
            pattern.append(' ')
            return
        i//=3
        j//=3
    pattern.append('*')

for i in range(n):
    pattern=[]
    for j in range(n):
        star(i,j)
    print(*pattern,sep='')