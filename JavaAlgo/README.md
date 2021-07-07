# JavaAlgorithm



## 1. 문자열 찾기

- 입력 받기

```java
Scanner kb = new Scanner();
// next() String 형태로 반환
String str = kb.next();
// .charAt(index) index 에 있는 문자 하나 반환한다.
char c = kb.next().charAt(0);
```

- solution method 작성

```java
// 대문자로 변환
str = str.toUpperCase();
c = Character.toUpperCase();

for(char x: str.toCharArray()){
  if(x==c) answer++;
}
```

- Scanner 정리
  - String next() : 다음 토큰을 문자열로 리턴 
  - byte nextByte() : 다음 토큰을 byte 타입으로 리턴 
  - short nextShort() : 다음 토큰을 short 타입으로 리턴 
  - int nextInt() : 다음 토큰을 int 타입으로 리턴
  - long nextLong() : 다음 토큰을 long 타입으로 리턴 
  - float nextFloat() : 다음 토큰을 float 타입으로 리턴 
  - double nextDouble() : 다음 토큰을 double 타입으로 리턴 
  - String nextLine() : ' \n '을 포함하는 한 라인을 읽고 ' \n '을 버린 나머지만 리턴 
  - void close() : Scanner의 사용 종료
  - boolean hasNext() 
    현재 입력된 토큰이 있으면 true, 아니면 새로운 입력이 들어올 때까지 무한정 기다려서, 새로운 입력이 들어오면 그 때 true 리턴. ctrl + z 키가 입력되면 입력 끝이므로 false 리턴 

