# Programmers

## 코딩테스트 연습 

### 2018 카카오 블라인드 채용

#### 프렌즈4블록

그간 시뮬레이션 문제가 어떻다는 얘기만 들었지 제대로 시뮬레이션을 풀어본적이 없었는데 이 문제를 통해 시뮬레이션이 무엇인지 알 수 있었다.

배열을 -90도(왼쪽으로 90도, 즉 270도 회전) 시키는 것부터 쉽지 않았다. 정사각형 배열만 주어지는게 아니라 이중 for문으로는 돌리기 힘들어서 zip 함수를 활용했다.

zip 함수만 쓰면 tuple 이 되므로 map 함수를 통해 list화 하고 [::-1]을 map 상태로 할 수 없으므로 다시 list로 감싸고 [::-1]을 한다.

arr이라는 이중 배열이 있다고 할때, 이를 다시 list로 감싼다고 해서 삼중 배열이 되지 않음을 알았다.

```python
a = arr = [["C", "C", "B", "D", "E"], ["A", "A", "A", "D", "E"],
        ["A", "A", "A", "B", "F"], ["C","C", "B", "B", "F"]]
arr2 = list(arr)
print(arr == arr2) # true다.
```



풀이는 겹치는 값이 안나올때 까지 돌렸다.

2x2 사이즈에서 같은 값이 나오면 check_arr 배열에 1을 넣는다. 1을 더해주는 것은 안된다. 만약 그렇게 하면 두번 연속으로 같은 값이 나오게 되면 1이 되어야 할 곳이 2가 된다.

배열을 다 돌고나면 check_arr을 돌면서 1을 모두 0으로 바꾸고, answer는 1씩 더해주면서 arr270을 0으로 바꾼다.

arr270을 돌면서 비어 있는 부분에 하나씩 요소를 옮긴다. 행의 뒤에서부터 돌면서 0이 아닌 값이 나오면 해당 행의 인덱스의 뒷부분까지 행의 뒤에서부터 다시 돌면서 0이 나오면 바로 거기에 값을 옮기고 기존 인덱스는 0으로 바꾼다. 이러면 행의 가장 뒷 부분에다가 행의 가장 뒤에 있는 0이 아닌 값을 옮길 수 있다.