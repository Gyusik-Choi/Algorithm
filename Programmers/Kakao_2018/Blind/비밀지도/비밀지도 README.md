# Programmers

## 코딩테스트 연습 

### 2018 카카오 블라인드 채용

#### 비밀지도

- 논리연산

  - 정수끼리 논리연산하면 이진수 기반 연산이 수행된다.

    - or -> |
    - and -> &

    

- 이진 변환
  - 정수의 이진수 변환. 단 변환시 문자열이 된다.
    - bin
      - bin(13) => '0b1101'
    - format
      - format(13, 'b') => '1101'



- 문자열 클래스 메소드

  - maketrans와 translate

    - ```python
      a = '11010' # a는 반드시 문자열이여야 한다.
      b = a.maketrans('10', '# ') # 여기선 딕셔너리 상태
      							# {49: 35, 48: 32}
      c = a.translate(b)	# c는 '## # '가 된다.
      ```

