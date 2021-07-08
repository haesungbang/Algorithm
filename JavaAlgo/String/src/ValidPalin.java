import java.util.Scanner;

public class ValidPalin {

	public String solution(String str) {
		String answer="NO";
		// 알파벳만 있게 만들기, 알파벳만 남긴다.
		// A-Z 가 아니면(^) 다 빈 문자열로 바꾼다.
		str = str.toUpperCase().replaceAll("[^A-Z]", "");
//		System.out.println(str);
		String tmp=new StringBuilder(str).reverse().toString();
		
		// str==tmp 하면 안 된다. 다르게 나온다. 메모리 주소를 비교하는 듯? 둘다 오브젝트
		if(str.equals(tmp)) answer="YES";
		return answer;
	}
	public static void main(String[] args) {
		ValidPalin T = new ValidPalin();
		Scanner kb = new Scanner(System.in);
		String str = kb.nextLine();
		System.out.println(T.solution(str));
		
	}

}
