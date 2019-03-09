#include <cstdio>
using namespace std;
int cnt[10001];
int main(void){
	int n;
	scanf("%d",&n);
	for(int i=0;i<n;i++){
		int v;
		scanf("%d",&v);
		cnt[v]++;
	}
	for(int i=1;i<=10000;i++){
		for(int j=0;j<cnt[i];j++)
				printf("%d\n",i);
	}
	return 0;

}