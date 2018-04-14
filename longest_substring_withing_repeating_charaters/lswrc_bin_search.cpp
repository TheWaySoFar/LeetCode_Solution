#include<iostream>
#include<cstring>
#include<string>
using namespace std;

class Solution {
public:
    bool judge(int mid, string s){
        int a[128];
        for(int i=0; i+mid-1<s.size(); i++){
            int flag = 0;
            memset(a, -1, sizeof(a));
            for(int j=i; j<i+mid; j++){
                if(a[s[j]] != -1){
                    flag = 1;
                    break;
                }
                a[s[j]] = 1;
            }
            if(flag == 0){
                return true;
            }
        }
        return false;
    }
    int lengthOfLongestSubstring(string s) {
        int l = 0, r = s.size();
        int mid = 0;
        while(l<r){
            mid = l + (r - l + 1) / 2;
            if(judge(mid, s)){
                l = mid;
            } else {
                r = mid - 1;
            }
        }
        return l;
    }
};
int main(){
    Solution s;
    cout<<s.lengthOfLongestSubstring("abcabcbb")<<endl;
    cout<<s.lengthOfLongestSubstring("bbbbb")<<endl;
    cout<<s.lengthOfLongestSubstring("pwwkew")<<endl;
    cout<<s.lengthOfLongestSubstring("c")<<endl;
    cout<<s.lengthOfLongestSubstring("")<<endl;
    return 0;
}