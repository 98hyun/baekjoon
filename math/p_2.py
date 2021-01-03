'''
정수 배열 numbers가 주어집니다.
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는
모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.

입력예제 

2 1 3 4 1 

출력예제 

[2,3,4,5,6,7]
'''

# 1. 구현 & 조합


nums=list(map(int,input().split()))

n=len(nums)
result=[]

for i in range(n):
    for j in range(i+1,n):
        tmp=nums[i]+nums[j]
        result.append(tmp)

print(sorted(set(result)))