package Main2;

import java.util.Scanner;

public class FiboNachi4 {
	
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int T=sc.nextInt();
		int[][] dp=new int[41][2];
		dp[0][0]=1;// 1 0
		dp[1][1]=1;// 0 1
		
		for(int i=0;i<T;i++) {
			FiboShow(dp,sc.nextInt());
		}
		sc.close();
	
	}
	public static void FiboShow(int[][] dp,int n) {
		if(n>=2&&dp[n][0]==0&&dp[n][1]==0) {
			for(int i=2;i<=n;i++) {
				dp[i][0]=dp[i-1][0]+dp[i-2][0];//0°¹¼ö
				dp[i][1]=dp[i-1][1]+dp[i-2][1];//1°¹¼ö
			}
		}
		System.out.println(dp[n][0]+" "+dp[n][1]);
	}

}
