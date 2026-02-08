# PGM [Lv.0] 문자열 겹쳐쓰기
<sup>[문제 바로가기](https://school.programmers.co.kr/learn/courses/30/lessons/181943)</sup>

## 결과
- 시간: 0.00ms
- 메모리: 9.29MB

---

## 문제 분석
1. 기준 문자열에서 주어진 인덱스를 기준으로 변환 문자열을 끼워넣는다.

---

## 접근 방법
1. 기준 문자열을 인덱스-1 만큼 자른다.
2. 변환 문자열은 그대로 사용한다.
3. 기준 문자열에서 변환 문자열만큼 변경된 길이 이후의 문자열을 구한다.
4. 결과값으로 1+2+3을 출력한다.

처음에는 return 값을 아래와 같이 작성하였다.
```python
return my_string[:s] + overwrite_string + my_string[len(my_string[:s] + overwrite_string):]
```

중복되는 코드가 있어서 변수로 담아서 리펙터링하게 되었다.
```python
x = my_string[:s] + overwrite_string
return x + my_string[len(x):]
```

---

## 배운 점

문자열을 자를 때 사용하는 slicing 문법을 알게되었다.
slicing 문법에는 이번에 사용하지 않은 'step'이라는 옵션도 있다.
그래서 좀 더 상세히 알아보았다.

### slicing 기본 문법

```python
seq[start : stop : step]
```

* start : 시작 인덱스 (범위에 포함)
* stop : 끝 인덱스 (범위에 미포함)
* step : 증가 간격 (기본 1)

```python
string = "abcdef"

string[:3]      # 0 ~ 3-1   >>> 'abc'
string[3:]      # 3 ~ last  >>> 'def'
string[::2]     # 2칸씩      >>> 'ace'
string[::-1]    # 뒤집기     >>> 'fedcba'
string[1::2]    # 1부터 2칸씩 >>> 'bdf'
```

