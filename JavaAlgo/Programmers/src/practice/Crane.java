package practice;

import java.util.Scanner;
import java.util.Stack;

public class Crane {
	public int solution(int[][] arr, int[] order) {
		int answer = 0;
		// 인형을 담을 공간 
		Stack<Integer> stack = new Stack<>();
		
		for(int x : order) {
			for(int i=0; i<arr.length; i++) {
				// 비어있지 않다면
				if(arr[i][x-1]!=0) {
					int tmp = arr[i][x-1];
					arr[i][x-1] = 0;
					// 스택이 비어있지 않고 윗 값과 값이 같다면
					if(!stack.isEmpty() && tmp==stack.peek()) {
						answer+=2;
						stack.pop();
					}
					// 나머지의 경우 추가한다.
					else stack.push(tmp);
					break;
				}
			}
		}
		return answer;
	}
	public static void main(String[] args) {
		Crane T = new Crane();
		Scanner kb = new Scanner(System.in);
		
		int n = kb.nextInt();
		int[][] arr = new int[n][n];
		for(int i=0; i<n; i++) {
			for(int j=0; j<n; j++) {
				arr[i][j] = kb.nextInt();
			}
		}
		int k = kb.nextInt();
		int[] order = new int[k];
		for(int i=0; i<k; i++) {
			order[i] = kb.nextInt();
		}
		System.out.println(T.solution(arr,  order));
	}

}
