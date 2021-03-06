a = [[1, 0], [1, 3], [1, 2], [2, 3], [2, 1], [2, 5], [0, 5], [0, 2], [0, 1]]
a.sort(key=lambda x: (-x[0], x[1]))
print(a)

# [[2, 1], [2, 3], [2, 5], [1, 0], [1, 2], [1, 3], [0, 1], [0, 2], [0, 5]]
# 위의 람다식 조건에서 -는 내림차순을 의미한다.
# 위의 조건은 첫번째 원소를 기준으로 내림차순으로 정렬하고,
# 두번째 원소를 기준으로 오름차순 정렬한다.

# 참고
# https://otugi.tistory.com/164
