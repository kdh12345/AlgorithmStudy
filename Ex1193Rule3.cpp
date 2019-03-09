#include <iostream>
using namespace std;

int main(void){
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int x;
	cin>>x;
	/*int num1=1;
	int num2=1;
	int cnt=0;
	int idx=1;
	bool turn=true;
	int j=0;
	int i=1;
	if(x==1)
		cout<<num1<<"/"<<num2<<"\n";
	for(i=1;i<=x;){
		int tmp=cnt++;
		i+=tmp;
		for(j=i+1;j<i+idx;j++){
			if(x==i+idx&&turn){
				num2++;
				break;
			}else if(x==i+idx&&!turn){
				num1++;
				break;
			}
			if(turn){	
				num1++;
				num2--;
				if(j==x)
					break;
			}else if(!turn){
				num1--;
				num2++;
				if(j==x)
					break;
			}
		}//j
		if(x==i+idx){
			if(x==2){
				cout<<num1<<"/"<<num2+1<<"\n";
				break;
			}	
			cout<<num1<<"/"<<num2<<"\n";
			break;
		}
		idx++;
		if(j==x)
		{
			int swap=num1;
			num1=num2;
			num2=swap;
			cout<<num1<<"/"<<num2<<"\n";
			break;
		}
		if(turn){
			num1++;
			num2=1;
			turn=false;
		}else if(!turn){
			num2++;
			num1=1;
			turn=true;
		}

	}//i*/
	int sum=0;
	int i=0;
	while(sum<x){
		i++;
		sum+=i;
	}
	int num=sum-x;
	if(i%2==0)
		cout<<i-num<<"/"<<num+1<<"\n";
	else
		cout<<num+1<<"/"<<i-num<<"\n";
	return 0;
}