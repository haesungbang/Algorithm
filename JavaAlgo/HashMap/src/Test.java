import java.util.*;
public class Test {
	public void DFS(int n){
		if(n==0) return;
		else{
			DFS(n/2);
			System.out.print(n%2);
		}
	}

	public void solution(int n){
		DFS(n);
	}
	public static void main(String[] args){
		Test T = new Test();
		T.solution(11);
		//System.out.println(T.solution(3));
	}	
}
