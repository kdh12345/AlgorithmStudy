package Main2;

import java.util.Scanner;

public class Fibonachi3 {
	public long Fibo(long n) {
		long a=0;
		long b=1;
		long tmp;
		for(int i=1;i<n%1500000;i++) {//��° �Ǻ���ġ ��
			tmp=b;
			b=a+b;
			a=tmp;
			b=b%1000000;
				
		}
		return b%1000000;
	}
	public static void main(String[] args) {
		Fibonachi3 f=new Fibonachi3();
		Scanner sc=new Scanner(System.in);
		long n=sc.nextLong();
		long result=f.Fibo(n);
		System.out.println(result);
		

	}

}
