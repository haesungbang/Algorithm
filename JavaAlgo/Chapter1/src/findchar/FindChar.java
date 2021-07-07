package findchar;
import java.util.Scanner;

public class FindChar {
	public int solution(String str, char t) {
		int answer = 0;
		 
		// 다 대문자로 바꾼다.
		str = str.toUpperCase();
		t = Character.toUpperCase(t);
		
//		System.out.println(str);
		
//		for(int i=0; i<str.length(); i++) {
//			if(str.charAt(i) == t) {
//				answer++;
//			}
//		}
		
		// : 뒤에는 배열이나 index 로 찾을 수 있는 것? 문자열을 배열로 바꾼다.
		for(char x : str.toCharArray()) {
			if(x==t) answer++;
		}
		
		return answer;
	}

	public static void main(String[] args) {
		FindChar T = new FindChar();
		
		// 공백을 기준으로 입력받는다.(객체를?) 다양한 형태로 변환 가능
		Scanner kb = new Scanner(System.in);
		
		// .next() 가 문자열로 반환한다.
		// .nextInt() 등 다양한 반환 형태를 취할 수 있다.
		String str = kb.next();
		
		// .charAt(index) 문자 한 개를 가져와라.
		char c = kb.next().charAt(0);
		
		
		System.out.println(T.solution(str, c));
	}
}
