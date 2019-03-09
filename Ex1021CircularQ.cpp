#include <cstdio>
#include <iostream>
#include <deque>
using namespace std;
///mid보다 크면 back, 작거나 같으면 front
deque<int> input;

int n,m;
int getIndex(int n){
	int ret=0;
	for(int i=0;i<input.size();i++){
		if(input[i]==n){
			ret=i;
			break;
		}
	}
	return ret;
}
void Circular(deque<int> num){
	int count=0;
	while(!num.empty()){
		if(num.front()==input.front()){
			num.pop_front();
			input.pop_front();
		}else if(getIndex(num.front())>input.size()/2){
			int pre=input.back();
			input.pop_back();
			input.push_front(pre);
			count++;
		}else {
			int pre=input.front();
			input.pop_front();
			input.push_back(pre);
			count++;

		}

	}
	printf("%d\n",count);

}
int main(void){
	scanf("%d %d",&n,&m);
	for(int i=0;i<n;i++){
		input.push_back(i+1);
	}
	deque<int> v;
	for(int i=0;i<m;i++){
		int num;
		scanf("%d",&num);
		v.push_back(num);
	}
	Circular(v);
	
	return 0;
}
