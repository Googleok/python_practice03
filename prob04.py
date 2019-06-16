# 문제4.
# 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다.
# 프로그램은 정답 여부를 다시 출력합니다.
# [출력]
# 6 x 9 = ?
#
# 81	12	32
# 18	54	4
# 32	6	32
#
# answer: 54           [입력]
# 정답                 [출력]
import random
print('[출력]')
a = random.randint(1, 9)
b = random.randint(1, 9)
answer = a * b
show_answers = {}
show_answers[1] = answer

# 답 보여주기
while len(show_answers) < 9:
    index = len(show_answers) + 1
    show_answers[index] = random.randint(1, 99)

# 답 shuffling 을 위해 dict -> list 로 변환
answer_list = []
for i in show_answers:
    answer_list.append(show_answers[i])
l = random.sample(answer_list, len(answer_list))
print(a, 'x', b, '= ?\n')

# 보기 출력
for i in range(0, len(l)):
    if i % 3 == 0 and i != 0:
        print()
    print(l[i], end='\t\t')

print()
# 입력
while True:
    user = input('answer: ')
    if int(user) == answer:
        print('정답입니다!')
        break


