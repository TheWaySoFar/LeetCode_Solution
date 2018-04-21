#include<iostream>
using namespace std;

class Solution {
public:
    string convert(string s, int numRows) {
        int len = s.size();
        if(len == 0)return s;
        int cnt = 2*numRows - 2;
        if(numRows == 1)cnt = 1;
        int grp = (len % cnt != 0)?len/cnt+1:len/cnt;
        char ans[len+1];
        int total = 0;
        for(int i=1; i<=numRows; i++){
            for(int j=0; j<grp; j++){
                if(j*cnt+i-1 < len)
                    ans[total++] = s[j*cnt+i-1];
                if(i != 1 && i != numRows){
                    if(j*cnt+i-1+2*(numRows-i) < len) ans[total++] = s[j*cnt+i-1+2*(numRows-i)];
                }
            }
        }
        ans[total] = 0;
        return string(ans);
    }
};
int main(){
    Solution s;
    cout<<s.convert("PAYPALISHIRING", 3)<<endl;
    cout<<s.convert("PAYPALISHIRING", 1)<<endl;
    cout<<s.convert("P", 1)<<endl;
    cout<<s.convert("PAYPALISHIRING", 4)<<endl;
    return 0;
}