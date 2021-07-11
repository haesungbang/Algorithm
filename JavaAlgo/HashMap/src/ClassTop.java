import java.util.HashMap;
import java.util.Scanner;

public class ClassTop {

	public char solution(int n, String s) {
		char answer=' ';
		
		// 딕셔너리 같다.
		// <Key, Value>
		HashMap<Character, Integer> map = new HashMap<>();
//		 HashMap 에 넣는 방법 map.put('A', 3);
		
		for(char x: s.toCharArray()) {
			// get 하면 키에 value 값을 가져온다.
			// getOrDefault(key, default value)
			map.put(x, map.getOrDefault(x, 0) + 1);
		}
		
		int max = Integer.MIN_VALUE;
		// keySet 존재하는 키 다 탐색
		for(char x : map.keySet()) {
			if(map.get(x)>max) {
				max=map.get(x);
				answer = x;
			}
		}
		
		return answer;
	}
	
	public static void main(String[] args) {
		ClassTop T = new ClassTop();
		Scanner kb = new Scanner(System.in);
		int n=kb.nextInt();
		String str = kb.next();
		System.out.println(T.solution(n, str));
	}

}
