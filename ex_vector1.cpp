#include <iostream>
#include <vector>
using namespace std;
int ex(vector<int> v){
	int sum=0;
	for(int i=0;i<v.size();i++)
		sum+=v[i];
	return sum;

}
int main(void){
	vector<int> v;
	v.push_back(1);
	v.push_back(2);
	v.erase(v.begin());
	v.push_back(3);
	v.push_back(5);
	cout<<ex(v)<<'\n';
	return 0;
}
