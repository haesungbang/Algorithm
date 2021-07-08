

import java.util.ArrayList;
import java.util.Scanner;

public class ReverseWord {

	public ArrayList<String> solution(int n, String[] str) {
		// <String> 은 <> 로 생략가능
		ArrayList<String> answer = new ArrayList<>();
	
		for(String x : str) {
			// StringBuilder 음... 메모리 효율적으로 쓰기 위해, 문자가 더하는 것 과 같은 행위에 좋다.
			// append(값), insert(index, 값), delete(index1, index2), reverse()
			// indexOf(값), substring(index, index), replace(index, index, 값)
			String tmp = new StringBuilder(x).reverse().toString();
			answer.add(tmp);
		}
		
		
		return answer;
		
	}
	
	public static void main(String[] args) {
		ReverseWord T = new ReverseWord();
		Scanner kb = new Scanner(System.in);
		
		// 횟수 
		int n = kb.nextInt();
		// 문자들은 배열로 받아올 것이다.
		String[] str = new String[n];
		for(int i = 0; i<n; i++) {
			str[i]=kb.next();
		}
		for(String x: T.solution(n, str)) {
			System.out.println(x);
		}
	}

}

