#include<iostream>
#include<vector>
#include<unordered_map>
using namespace std;

class Solution {
public:
	vector<int> twoSum(vector<int> &numbers, int target) {
		int n = numbers.size();
		unordered_map<int, int> m;
		for (int i = 0; i < n; i++) {
			m.insert(pair<int, int>(numbers[i], i));
		}
		

		for (int i = 0; i < n; i++) {
			auto find = m.find(target - numbers[i]);
			if (find != m.end()) {
				int mylist[2];
				mylist[0] = i + 1;
				mylist[1] = find->second + 1;
				if (mylist[0] == mylist[1]) {
					continue;
				}
				if (mylist[0] > mylist[1]) {
					int temp = mylist[0];
					mylist[0] = mylist[1];
					mylist[1] = temp;
				}
				return vector<int>(mylist, mylist + sizeof(mylist));
			}
		}
	}
};


int main(void){
	Solution solution;
	int mylist[] = {3, 2, 4};
	vector<int> number_list(mylist, mylist + sizeof(mylist));
	vector<int> out = solution.twoSum(number_list, 6);
	cout << out[0] << " " << out[1] << endl;
	system("pause");
}