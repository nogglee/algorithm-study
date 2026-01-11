# BOJ [1000] A+B
<sup>[문제 바로가기](https://www.acmicpc.net/problem/1000)</sup>

## 문제 분석
1. A와 B를 입력 받는다.
2. A+B를 출력한다.

---

## 접근 방법
1. 입력 값은 2개이다.
    ```python
    A = int(input())
    B = int(input())
    ```
2. 첫째 줄에 A와 B가 주어진다.
    ```python
    x, y = input().split()    # 공백을 기준으로 값을 쪼개기
    A = int(x)                # 값을 쪼개어 각 변수에 넣기
    B = int(y)
    ```
3. 2번을 map()으로 정리한 표준 입력 처리 방식
    ```python
    A, B = map(int, input().split())
    ```
---

## 배운 점
- `input()` : 한 줄을 문자열로 입력받는다.
- `split()` : 공백 기준으로 문자열을 분리한다.
- `map(int, ...)` : 분리된 각 값을 정수로 변환한다.

## 결과
- 시간: 72ms
- 메모리: 30840KB