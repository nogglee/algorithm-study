# PGM [181950] 문자열 반복해서 출력하기
<sup>[문제 바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/181950)</sup>

## 문제 분석
1. 문자열과 숫자를 각각 입력 받는다.
2. 숫자의 길이 만큼 문자열을 반복하여 한 줄로 출력한다.

---

## 접근 방법
1. 두 변수에 입력값을 저장한다.
2. 정수형 변수에 데이터타입 int를 지정한다.
3. 정수형 변수의 길이 만큼 문자열 변수의 값을 출력한다.

---

## 배운 점

### for문 미사용
충격적이다. 이렇게 간단하게 생각할 수 있는 문제였는데, 또 문제를 꼬아서 생각했다.  
'반복'이라는 키워드에 집중해서 풀이법 부터 생각했던 것 같다.  
다른 사람의 풀이를 참고하니 곱셈으로 끝내버렸다.  

```python
a, b = input().strip().split(' ')
b = int(b)

result = a * b
print(result)
```

### range 함수
반복문을 얼마나 반복할지 범위를 지정하는 함수이다. 
range() 함수 호출 시 start부터 stop-1 까지 step 만큼 증가하는 '정수' 시퀀스를 반환한다.  

`range(start, stop, step)`  
* start: 기본값 0
* stop: 필수 입력
* step: 기본값 1

제출한 답변에서는 start와 step을 기본값으로 사용하였으므로 stop 값만 정수형 변수 n으로 입력했다.  

### 변수 초기화
python에서 변수 선언 시 초기 값을 세팅해야한다.  
데이터 타입에 따라 아래와 같이 선언하면 된다.  

```python
string = ''
number = 0
boolean = True || False
```

---

## 결과
- 시간: 16.48ms
- 메모리: 7.5MB