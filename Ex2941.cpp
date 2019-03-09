#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main(void){
	cout.tie(0);
	cin.tie(0);
	string input;
	cin>>input;
	int count=0;
	for(int i=0;i<input.size();i++){
		if(input[i]=='c'&&(input[i+1]=='='||input[i+1]=='-')){//c= or c-
			i++;
		}else if(input[i]=='d'){//dz= or d-
			if(input[i+1]=='-'){
				i++;
			}else if(input[i+1]=='z'&&input[i+2]=='='){
				i+=2;
			}
		}else if((input[i]=='l'||input[i]=='n')&&input[i+1]=='j'){//lj or nj
			i++;
		}else if((input[i]=='s'||input[i]=='z')&&input[i+1]=='='){
			i++;
		}
		count++;	
	}//for
	cout<<count<<"\n";
	return 0;
}