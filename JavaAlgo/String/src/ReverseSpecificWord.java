import java.util.Scanner;

public class ReverseSpecificWord {

	public String solution(String str) {
		String answer;
		// 순회를 하고 싶어서?? 
		char[] s = str.toCharArray();
		// 첫번째와 마지막 위치
		int lt=0, rt=str.length()-1;
		while(lt<rt) {
			// 알파벳인지 확인한다. 알파벳이 아닐때!
			if(!Character.isAlphabetic(s[lt])) lt++;
			else if(!Character.isAlphabetic(s[rt])) rt--;
			// 둘다 알파벳이라면!!
			else {
				char tmp = s[lt];
				s[lt] = s[rt];
				s[rt] = tmp;
				lt++;
				rt--;
			}
		}
		// String 화 해준다. 숫자도 가능!
		answer=String.valueOf(s);
		
		return answer;
	}
	public static void main(String[] args) {

		ReverseSpecificWord T = new ReverseSpecificWord();
		Scanner kb = new Scanner(System.in);
		
		String str = kb.next();
		System.out.println(T.solution(str));
	}

}
