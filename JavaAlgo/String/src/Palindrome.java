import java.util.Scanner;

public class Palindrome {

	public String solution(String str) {
//		String answer="YES";
		String answer="NO";
		str = str.toUpperCase();
//		int len=str.length();
//		// 몫까지만 하면 된다.
//		for(int i=0; i<len/2; i++) {
//			if(str.charAt(i)!=str.charAt(len-i-1)) return "NO";
//		}
		String tmp=new StringBuilder(str).reverse().toString();
		if(str.equals(tmp)) answer="YES";
		return answer;
	}
	public static void main(String[] args) {
		Palindrome T = new Palindrome();
		Scanner kb = new Scanner(System.in);
		String str = kb.next();
		
		System.out.println(T.solution(str));
	}

}
