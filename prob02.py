# 문제2.
# range() 함수와 유사한 frange() 함수를 작성해 보세요.
# frange() 함수는 실수 리스트를 반환합니다.
# print(frange(2))
# print(frange(1.0, 2.0))
# print(frange(1.0, 3.0, 0.5))
def frange(val, base=0.0, step=0.1):
    list1 = []
    if val < base:
        start = val
        stop = base
    else:
        start = base
        stop = val
    while start <= stop:
        list1.append(start)
        start = round(start + step, 1)
    return list1



print(frange(2))
print(frange(1.0, 2.0))
print(frange(1.0, 3.0, 0.5))

