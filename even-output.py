#1부터 100까지의 수에서 짝수들만 출력하는 코드 구현
# 두 가지 방식을 생각하여 구현
#[1]: if 조건문 이용, 짝수 판단 후 처리

for i in range(1, 101):
    if (i % 2 == 0):
        print(i, end=' ')

#[2]: range() 함수의 step(간격) 옵션 값을 이용하여 처리

for i in range(2, 101, 2):
    print (i, end=' ')
