#include<iostream>
#include<string>
using namespace std;


class Solution {
public:
    string longestPalindrome(string s) {
        int len = s.size();
        int ans = 1, ansl = 0; 
        for(int i=0; i<len; i++){
            extend(i, i, s, ans, ansl);
            extend(i, i+1, s, ans, ansl);
        }
        //return string(s.begin()+ansl, s.begin()+ansl+ans);
        return s.substr(ansl, ans);
    }
    void extend(int l, int r, string s,int & ans, int & ansl){
        int len = s.size();
        while(l>=0&&r<len){
            if(s[l] == s[r]){
                l--,r++;
            } else {
                if(r-l-1>ans){
                    ans = r-l-1;
                    ansl = l+1;
                }
                return;
            }
        }
        if(ans < r-l-1){
            ans = r-l-1;
            ansl = l+1;

        }
    }
};
int main(){
    Solution s;
    cout<<s.longestPalindrome("babad")<<endl;
    cout<<s.longestPalindrome("cbbd")<<endl;
    cout<<s.longestPalindrome("abcddcba")<<endl;
    return 0;
}