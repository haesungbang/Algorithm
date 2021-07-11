package practice;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Course {
	public String solution(String need, String plan) {
		String answer = "YES";
		Queue<Character> q = new LinkedList<>();
		
		for(char x: need.toCharArray()) q.offer(x);
		for(char x: plan.toCharArray()) {
			// x 가 q 안에 있는데 첫 번째 뽑은 값이랑 같은지 비교한다.
			if(q.contains(x)) {
				if(x!=q.poll()) return "NO";
			}
		}
		// 다 돌았는데 비지 않았다? 실패다!
		if(!q.isEmpty()) return "NO";
		return answer;
	}
	public static void main(String[] args){
		Course T = new Course();
		Scanner kb = new Scanner(System.in);
		String a=kb.next();
		String b=kb.next();
		System.out.println(T.solution(a, b));
	}

}
