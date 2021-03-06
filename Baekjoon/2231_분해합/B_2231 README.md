# 백준

## 2231

백준의 4673_셀프넘버 문제와 연관성이 있다.

(파이썬 풀이)

입력받은 정수 N을 반복문을 돌려서 N부터 1까지 숫자를 내려가면서 생성자가 될 수 있는지 검사했다. 그러면서 생성자를 몇 번이나 만들었는지 검사하고, 기존의 생성자 보다 작은 수가 생성자가 되면 답을 구할 변수의 값을 교체했다.

생성자를 한번도 못만들었으면 생성자가 없는 것이므로 0으로 출력했고, 생성자를 한번 이상 만들었으면 최소 생성자 값을 출력했다.



(자바스크립트 풀이)

자바스크립트로 다시 풀이해보았다. 

1부터 n - 1까지 반복문을 돌면서 문제에서 요구하는 분해합을 구해서 입력받은 N과 같으면 출력하고 끝냈다. 작은 수부터 올라갔기 때문에 N과 같은 분해합이 나오는 숫자가 바로 정답이 된다.

만약 반복문이 끝까지 돌았는데도 분해합이 N이 되는 숫자가 나오지 않으면 0을 출력했다.

이전 파이썬 풀이보다 나아진 점은 반복문을 도는 횟수를 줄였다. 파이썬 풀이에서는 큰 숫자부터 했기 때문에 답이 나오든 안나오든 끝까지 돌아야 했으나, 자바스크립트 풀이에선 1부터 반복문을 돌았기에 답이 나오면 반복문을 더 이상 돌지 않아도 된다.