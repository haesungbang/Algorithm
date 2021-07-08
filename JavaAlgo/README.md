# JavaAlgorithm

## 1. 문자열 찾기

- **입력 받기**

```java
Scanner kb = new Scanner();
// next() String 형태로 반환
String str = kb.next();
// .charAt(index) index 에 있는 문자 하나 반환한다.
char c = kb.next().charAt(0);
```

- **solution method 작성**

```java
// 대문자로 변환
str = str.toUpperCase();
c = Character.toUpperCase();

for(char x: str.toCharArray()){
  if(x==c) answer++;
}
```

- **String 인덱스, 도는 방법**

```java
// 그냥 String
str.charAt(index)
// String 을 배열로!
str.toCharArray()
```

- **Scanner 정리**
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

## 2. 대소문자 변환

- **대소문자 확인 및 변환**

```java
// 대소문자 확인(메서드 활용)
Character.isLowerCase(x)
Character.isUpperCase(x)

// 대소문자 확인(대소문자 상수 확인)
대문자는 65~90, 소문자는 97~122

// 대소문자 변환
Character.toUpperCase(x)
Character.toLowerCase(x)
str.toUpperCase(x)
str.toLowerCase(x)
```

## 3. 문장 속 단어

- **문장 공백 기준으로 나누기**

```java
// split() 활용
String[] s = str.split(" "); // " "을 기준으로 나누어서 배열에 저장

// indexOf(""), substring(index) 활용하기 : indexOf 는 첫 번째 위치를 반환한다.
// 없지 않을 때까지 반복
while((pos=str.indexOf(' '))!=-1){
			String tmp=str.substring(0, pos);
			int len=tmp.length();
			if(len>m){
				m=len;
				answer=tmp;
			}
  // pos+1 ~ 끝까지
			str=str.substring(pos+1);
    }
// 마지막에 남은 것도 확인 한다.
    if(str.length()>m) answer=str;
```

## 4. 단어 뒤집기

- **StringBuilder().reverse() 활용**

```java
for(String x : str){
      // StringBuilder 에 넣고, 뒤집고, 문자로
			String tmp=new StringBuilder(x).reverse().toString();
      // ArrayList 에 넣는다.
			answer.add(tmp);
		}
```

- **Index 위치 활용하기**

```java
for(String x : str){
			char[] s=x.toCharArray();
			int lt=0, rt=x.length()-1;
			// while(lt<rt) 잘 떠올리기
  		while(lt<rt){
				char tmp=s[lt];
				s[lt]=s[rt];
				s[rt]=tmp;
				lt++;
				rt--;
			}
			String tmp=String.valueOf(s);
			answer.add(tmp);
		}
```

- **StringBuilder 메서드**
  - append(값), insert(index, 값), delete(index1, index2), reverse()
  - indexOf(값), substring(index, index), replace(index, index, 값)

## 5. 특정 문자 뒤집기

- **Character.isAlphabetic(값)**

```java
// 알파벳인지 아닌지 확인하기
if(!Character.isAlphabetic(s[lt])) lt++;
```

- **String.valueOf(s)**

```java
// char[] 를 문자열로 바꿀 때
answer=String.valueOf(s);
```

## 6. 중복문자 제거

- **indexOf()** : 첫 번째 위치를 반환해주는 것을 활용한다.

```java
// 단어에 위치와 indexOf 가 같으면 중복된 것이 아니다. answer 에 추가
if(str.indexOf(str.charAt(i))==i) answer+=str.charAt(i);
```

## 7. 회문(Palindrome)

- **반으로 나눠서 앞, 뒤 비교**

```java
// 몫을 기준으로 앞 뒤
for(int i=0; i<len/2; i++){
			if(str.charAt(i)!=str.charAt(len-i-1)) answer="NO";
		}
```

- **뒤집어서 같으면 회문**
  - **equals()** : 대소문자를 구분해서 같은지 비교한다.
  - **equalsIgnoreCase()** : 대소문자 상관없이 같은지 비교한다.

```java
String tmp=new StringBuilder(str).reverse().toString();
if(str.equalsIgnoreCase(tmp)) answer="YES";
```

## 8. 유효한 회문

- **replaceAll() 활용**

```java
// A-Z 가 아니면(^) 공백으로 바꾼다.
s=s.toUpperCase().replaceAll("[^A-Z]", "");
String tmp=new StringBuilder(s).reverse().toString();
if(s.equals(tmp)) answer="YES";
```

- **replace, replaceAll 차이**

```java
String str = "aaabbbccccabcddddabcdeeee";
// replace : abc 문자열을 왕 으로
String result1 = str.replace("abc", "왕"); // aaabbbcccc왕dddd왕deeee

// replaceAll : a or b or c 문자를 왕으로
// 정규식을 활용할 수 있다. [^A-Z], [^0-9]
String result2 = str.replaceAll("[abc]", "왕"); // 왕왕왕왕왕왕왕왕왕왕왕왕왕dddd왕왕왕deeee

```

