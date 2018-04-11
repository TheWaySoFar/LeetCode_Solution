#include<iostream>
#include<vector>
#include<unordered_map>
#include<iterator>
using namespace std;


class Solution{
public:
    vector<int> twoSum(vector<int>& nums, int target){
        unordered_map<int, int> mp;
        for(int i = 0; i < nums.size(); i++){
            unordered_map<int, int>::iterator it = mp.find(target - nums[i]); 
            if(it != mp.end()){
               return vector<int> {it->second, i}; 
            }
            mp[nums[i]] = i; 
        }
    } 
};

int main(){
    Solution s;
    int a[4] = {2, 7, 11, 5};
    vector<int> b(a, a + 4);
    vector<int> ans = s.twoSum(b, 9);
    for(auto x : ans){
        cout<<x<<" ";
    }
    cout<<endl;
    return 0;
}