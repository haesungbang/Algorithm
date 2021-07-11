package practice;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class Person{
	int id;
	int priority;
	public Person(int id, int priority) {
		this.id = id;
		this.priority = priority;
	}
}

public class EmergencyRoom {
	public int solution(int n, int m, int[] arr) {
		int answer = 0;
		Queue<Person> q = new LinkedList<>();
		for(int i=0; i<n; i++) {
			// 아예 Person 을 넣는다.
			q.offer(new Person(i, arr[i]));
		}
		while(!q.isEmpty()) {
			// 맨 앞에 것을 꺼낸다.
			Person tmp = q.poll();
			for(Person x: q) {
				if(x.priority>tmp.priority) {
					q.offer(tmp);
					tmp=null;
					break;
				}
			}
			// null 값이 아니면 얘가 최우선 순위! 
			// 횟수 1 늘리고, 만약 m 이라면 return 끝!
			if(tmp!=null) {
				answer++;
				if(tmp.id==m) return answer;
			}
		}
		return answer;
		
	}
	public static void main(String[] args) {
		EmergencyRoom T = new EmergencyRoom();
		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		int m = kb.nextInt();
		
		int[] arr = new int[n];
		for(int i=0; i<n; i++) {
			arr[i] = kb.nextInt();
		}
		System.out.println(T.solution(n, m, arr));
	}

}
