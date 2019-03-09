#include <iostream>
using namespace std;

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int x,y;// x는 월 y는 일
	cin>>x>>y;
	int day=0;
	for(int i=1;i<=x;i++){
		if(i==2||i==4||i==6||i==8||i==9||i==11)
			day+=31;
		else if(i==5||i==7||i==10||i==12)
			day+=30;
		else if(i==3)
			day+=28;
	}
	int date=(day+y)%7;
	if(date==0)
		cout<<"SUN"<<"\n";
	else if(date==1)
		cout<<"MON"<<"\n";
	else if(date==2)
		cout<<"TUE"<<"\n";
	else if(date==3)
		cout<<"WED"<<"\n";
	else if(date==4)
		cout<<"THU"<<"\n";
	else if(date==5)
		cout<<"FRI"<<"\n";
	else if(date==6)
		cout<<"SAT"<<"\n";
	return 0;
}