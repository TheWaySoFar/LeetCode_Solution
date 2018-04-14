#include<iostream>
#include<cstring>
#include<string>
using namespace std;

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        if(s.size() == 0)return 0;
        int last[128];
        memset(last, -1, sizeof(last));
        int ans = 0;
        int l = 0;
        for(int i=0; i<s.size(); i++){
            if(last[s[i]] != -1 && last[s[i]] >= l){
                ans = max(ans, i-last[s[i]]);
                l = last[s[i]] + 1;
            } else {
                ans = max(ans, i - l + 1);
            }
            last[s[i]] = i;
        }
        ans = max(ans, int(s.size()) - l);
        return ans;
    }
};
int main(){
    Solution s;
    cout<<s.lengthOfLongestSubstring("abcabcbb")<<endl;
    cout<<s.lengthOfLongestSubstring("bbbbb")<<endl;
    cout<<s.lengthOfLongestSubstring("pwwkew")<<endl;
    cout<<s.lengthOfLongestSubstring("c")<<endl;
    cout<<s.lengthOfLongestSubstring("")<<endl;
    cout<<s.lengthOfLongestSubstring("cdd")<<endl;
    return 0;
}