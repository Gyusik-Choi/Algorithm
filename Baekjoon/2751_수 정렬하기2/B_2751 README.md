# 백준

## 2751

병합정렬과 퀵정렬으로 풀이했을 때 처음에는 모두 시간초과가 나왔다.

그 다음에는 입력과 출력을 input과 print 대신에 import sys를 이용해서 sys.stdin.readline(), sys.stdout.write()로 바꿔서 풀이했다.

병합정렬은 통과했으나 퀵정렬은 시간초과가 나왔다.

통과한 병합정렬 코드를 pypy3에서 돌리면 메모리 사용량은 3배 가까이 커지지만 시간이 5배 이상 빨라진다.