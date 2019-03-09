/*
import java.util.ArrayDeque;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;
import java.util.Stack;
import java.util.Vector;

public class Main {

public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
Queue<Integer> q=new LinkedList<>();
int num=0;
int N = sc.nextInt();
sc.nextLine();
for (int i = 0; i < N; i++) {
String command = sc.next();
if (command.equals("push")) {
num=sc.nextInt();
q.add(num);
} else if (command.equals("pop")) {
if (q.isEmpty()) {
System.out.println(-1);
} else {
System.out.println(q.poll());
}
} else if (command.equals("size")) {
System.out.println(q.size());
} else if (command.equals("empty")) {
if (q.isEmpty()) {
System.out.println(1);
} else {
System.out.println(0);
}

} else if (command.equals("front")) {
if (q.isEmpty())
System.out.println(-1);
else
System.out.println(q.peek());
}else if(command.equals("back")) { 
if(q.isEmpty())
System.out.println(-1);
else {
System.out.println(num);
}

}
else {
System.out.println("잘못입력하였습니다.");
}

}

}

}*/
#include <cstdio>
#include <deque>
#include <string>
#include <iostream>
using namespace std;

int main(void){
	cout.tie(0);
	cin.tie(0);
	int n;
	deque<int> d;
	cin>>n;
	int num=0;
	for(int i=0;i<n;i++){
		string command;
		cin>>command;
		if(command=="push_front"){
			cin>>num;
			d.push_front(num);
		}else if(command=="push_back"){
			cin>>num;
			d.push_back(num);
		}else if(command=="pop_front"){
			if(!d.empty()){
				cout<<d.front()<<"\n";
				d.pop_front();
			}else if(d.empty()){
				cout<<"-1"<<"\n";
			}
		}else if(command=="pop_back"){
			if(!d.empty()){
				cout<<d.back()<<"\n";
				d.pop_back();
			}else if(d.empty()){
				cout<<-1<<"\n";
			}
		}else if(command=="size"){
			cout<<d.size()<<"\n";
		}else if(command=="empty"){
			if(d.empty())
				cout<<1<<"\n";
			else if(!d.empty()){
				cout<<0<<"\n";
			}
		}else if(command=="front"){
			if(!d.empty()){
				cout<<d.front()<<"\n";
			}else if(d.empty()){
				cout<<-1<<"\n";
			}
		}else if(command=="back"){
			if(!d.empty()){
				cout<<d.back()<<"\n";
			}else if(d.empty()){
				cout<<-1<<"\n";
			}
		}

	}

}