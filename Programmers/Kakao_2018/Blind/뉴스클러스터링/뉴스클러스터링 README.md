# Programmers

## 코딩테스트 연습 

### 2018 카카오 블라인드 채용

#### 뉴스 클러스터링

단순히 교집합과 합집합의 공식을 이용해버리면 답을 구할 수 없다.

a에 'AA'가 2개 있고 b에 'AA'가 3개 있다면 교집합 공식(&)을 이용하면 'AA'만 남는다. 그러나 문제에서 원하는 것은 'AA', 'AA'다.

합집합 공식(|)을 이용하더라도 집합 자체에 'AA'를 1개 이상 넣을 수 없기에 문제에서 원하는 답을 구할 수 없다.

교집합의 경우 딕셔너리를 이용해 각 요소별 갯수를 구하고 이를 비교해서 더 작은 값을 저장했다.

합집합의 경우 이중 for문이 아닌 하나의 for문을 두번 돌면서 시간 복잡도를 줄이고자 했다. 두개의 딕셔너리를 각각 for문 돌면서 답을 구할 딕셔너리에 없으면 넣었고, 있다면 값을 비교해서 더 큰 값을 넣었다.