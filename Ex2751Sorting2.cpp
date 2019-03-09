#include <cstdio>
#include <iostream>
using namespace std;
////퀵소트
#define qSWAP(x,y) {int t=x;x=y;y=t;}
#define MAX 1000000
int N,arr[MAX];
void qSort(int array[],int left,int right){
	int mLeft=left,mRight=right;
	int pivot=array[(left+right)/2];

	while(mLeft<=mRight){
		while(pivot>array[mLeft])mLeft++;
		while(pivot<array[mRight])mRight--;
		if(mLeft<=mRight){
			qSWAP(array[mLeft],array[mRight]);
			mLeft++;mRight--;
		}
	}
	if(left<mRight)qSort(arr,left,mRight);
	if(mLeft<right)qSort(arr,mLeft,right);
}
int main(void)
{
	cin.tie(0);
	cout.tie(0);
	int idx;
	cin>>N;
	for(idx=0;idx<N;idx++){
		cin>>arr[idx];
	}
	qSort(arr,0,N-1);

	for(idx=0;idx<N;idx++){
		cout<<arr[idx]<<"\n";
	}
	return 0;
}
///합병정렬
/*#include <vector>
int n,tmp;
vector<int> v;
void merge(vector<int> arr,int left,int mid,int right);
void mergesort(vector<int> arr,int left,int right);
void merge(vector<int> arr,int left,int mid,int right){
	int len1=mid-left+1;
	int len2=right-mid;
	vector<int> L(len1);
	vector<int> R(len2);
	int i,j,k;
	for(i=0;i<len1;i++)
		L[i]=arr[left+i];
	for(j=0;j<len2;j++)
		R[j]=arr[mid+j+1];
	i=0;j=0;k=left;
	while(i<len1&&j<len2){
		if(L[i]<=R[j]){arr[k]=L[i];i++;}
		else{arr[k]=R[j];j++;}
		k++;
	}
	while(i<len1){arr[k]=L[i];i++;k++;}
	while(j<len2){arr[k]=R[j];j++;k++;}
}
void mergesort(vector<int> arr,int left,int right){
	if(left>=right)return;
	int mid=(left+right)/2;
	mergesort(arr,left,mid);
	mergesort(arr,mid+1,right);
	merge(arr,left,mid,right);

}
int main(void){
	cin.tie(0);
	cout.tie(0);
	cin>>n;
	vector<int> arr(n);
	for(int i=0;i<n;i++){
		cin>>arr[i];
	}
	mergesort(arr,0,n-1);
	for(int i=0;i<n;i++){
		cout<<arr[i]<<"\n";
	}
	return 0;


}*/