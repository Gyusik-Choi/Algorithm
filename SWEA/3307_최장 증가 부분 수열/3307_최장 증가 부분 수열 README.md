# SWEA

## 3307

백트래킹으로는 시간 초과가 나온다.

DP를 활용해야 한다.

최장 증가 부분 수열의 길이를 구하는 문제다. 배열 a가 있을 때 a[x]가 0부터 x - 1까지 구한 최장 증가 부분 수열의 맨 뒤에 추가될 수 있는 값이라면 a[0] ~a[x-1] 까지의 최장 증가 부분 수열 길이에서 1을 더한 값이 된다.

수열 길이를 구할 배열 b를 주어진 배열의 크기 만큼 생성한다. 최저 길이는 1이므로 모든 배열의 값을 1로 두고 시작한다.

인덱스를 1인 경우부터 마지막의 앞 인덱스까지 for문을 돌면서 내부 for문은 해당 인덱스의 앞 부분까지 처음부터 돈다. 그러면서 외부 for문 인덱스의 배열 값보다 작은 내부 for문의 인덱스 배열 값에서 1을 더하면서 외부 for문 인덱스 배열 값에 대응하는 배열 b의 인덱스 값을 계속해서 갱신한다.

[1, 3, 2, 5, 9, 4, 6 ,7]로 구성된 배열 a가 있다고 하자.

[1, 1, 1, 1, 1, 1, 1, 1] 이렇게 배열 b를 추가해주고 여기서 길이 값을 갱신해나간다.

처음에는 a의 2번째 값인 3을 앞의 값과 비교하면서 계산한다.

1보다 크기 때문에 b의 2번째 값을 1에서 1을 더한 2로 갱신한다.

다음에는 a의 3번째 값인 2를 앞의 값들과 비교한다.

먼저 1보다 크기 때문에 b의 3번째 값을 1에서 1을 더한 2로 갱신한다.

3보다는 2가 작기때문에 넘어간다.

그 다음으로 5를 1, 3, 2와 비교한다.

1보다 크기 때문에 1에서 1을 더해 2로 갱신한다.

3보다도 크기 때문에 3의 값인 2에서 1을 더해 3으로 갱신한다.

2보다도 크기 때문에 2의 값인 2에서 1을 더해 3으로 갱신한다. 이때는 a의 3과 2가 b에서 같은 값이기 때문에 1, 3, 5/ 1, 2, 5 최장 증가 부분 수열의 길이는 3이다.

이렇게 해서 b의 최대 값을 구한다.

