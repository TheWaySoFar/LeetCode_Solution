#include<iostream>
using namespace std;
class Solution {
    public:
        bool isPalindrome(int x) {
            if(x==0)return true;
            if(x<0 || x%10==0)return false;
            int re=0;
            while(x>re){
                re=re*10+x%10;
                x/=10;
            }
            if(x==re||x==re/10)return true;
            return  false;
                        
        }
};
int main(){
    Solution s;
    cout<<s.isPalindrome(12)<<endl;
    cout<<s.isPalindrome(1221)<<endl;
    cout<<s.isPalindrome(-1221)<<endl;
    return 0;
}
