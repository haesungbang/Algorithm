

import java.util.Scanner;

public class WordInSentence {

	public String solution(String str) {
		String answer = "";
		
		// 최대값 갱신, 가장 작은 값으로 설정
		int m = Integer.MIN_VALUE, pos;
		
		// indexOf(s) s 가 들어있는 첫 번째 위치 반환
		while((pos=str.indexOf(" "))!=-1) {
			
			// substring 잘라낸다.
			String tmp = str.substring(0, pos);
			int len = tmp.length();
			if(len >= m) {
				m = len;
				answer=tmp;
			}
			// 이미 적용한 것들을 없앤다.
			str=str.substring(pos+1);
		}
		// 이거 없으면 study 가 안 들어간다.
		if(str.length()>m) answer = str;
		
//		// 띄어쓰기 기준으로 String 배열에 담는다.
//		String[] s = str.split(" ");
//		for(String x : s) {
////			System.out.println(x);
//			if(x.length() >= m) {
//				answer = x;
//			}
//		}
		return answer;
		
	}
	
	public static void main(String[] args) {
		WordInSentence T = new WordInSentence();
		Scanner kb = new Scanner(System.in);
		// 한 줄을 입력 받아야 된다.
		String str = kb.nextLine();
		
		System.out.println(T.solution(str));
	}

}

