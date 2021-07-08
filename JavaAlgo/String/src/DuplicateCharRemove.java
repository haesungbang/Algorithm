import java.util.Scanner;

public class DuplicateCharRemove {

	public String solution(String str) {
		String answer="";
//		char[] s = str.toCharArray();
		for(int i=0; i<str.length(); i++) {
			System.out.println(str.charAt(i)+" "+i+" "+str.indexOf(str.charAt(i)));
			// 가장 첫 번째 위치를 찾는다.
			if(str.indexOf(str.charAt(i))==i) {
				answer += str.charAt(i);
			}
		}
		return answer;
	}
	public static void main(String[] args) {
		DuplicateCharRemove T = new DuplicateCharRemove();
		Scanner kb = new Scanner(System.in);
		String str = kb.next();
		
		System.out.println(T.solution(str));
	}

}
