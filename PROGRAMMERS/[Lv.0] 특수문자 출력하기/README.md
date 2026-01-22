# PGM [Lv.0] 특수문자 출력하기
<sup>[문제 바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/181948)</sup>

## 문제 분석
1. 주어진 특수문자를 print문으로 출력한다.  

---

## 배운 점
`\'`: 작은 따옴표 문자열로 출력
`\"`: 큰 따옴표 문자열로 출력
`\\`: 역슬래쉬 문자열로 출력

다른 방식이 있는지 다른 사람 풀이도 찾아보았다.
짧게 풀어낸 사람도 있고, 16진수를 활용한 사람도 있었다.(놀라움..)

좀 더 효율적인 방식으로 짧게 풀어낸 답변은 아래와 같다.
`print(r'!@#$%^&*(\'"<>?:;')`

문자열 앞에 붙는 r의 의미는 'raw string'으로,
문자열에 포함되어있는 역슬래쉬가 이스케이프 문자로 해석되는 것을 방지한다.

## 이스케이프 문자란?

> **이스케이프 문자:**
> 문자 출력을 제어하는 코드

이스케이프 문자 사용 예시는 아래와 같다.

[ Lin Feed / LF / 줄바꿈 ]
`print("Hello\nNogglee!")`
-> Hello
-> Nogglee! 

[ Crrage Return / CF / 커서를 맨 앞으로 ]
`print("Hello\cNogglee!")`
-> Nogglee!

[ BackSpace / 커서를 뒤로 한 칸 이동 ]
`print("Hello\b\b\bNogglee!")`
-> HeNogglee!

[ Tab / tab 공간을 추가 ]
`print("Hello\tNogglee!")`
-> Hello    Nogglee!

---

## 결과
- 시간: 10.67ms
- 메모리: 7.27MB