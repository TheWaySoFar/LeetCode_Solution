#include<iostream>
#include<string>
#include<limits.h>
using namespace std;
class Solution {
public:
    int myAtoi(string str) {
        int len = str.size();
        if(str.size() == 0){
            return 0;
        }
        int i = 0;
        while(i<len && str[i] == ' ')i++;
        if(i>=len)return 0;
        int sign = 1;
        if(str[i] == '-'){
            sign = -1;
            i++;
        } else if(str[i]=='+'){
            i++;
        }
        if(str[i]<'0' || str[i]>'9'){
            return 0;
        }
        int num = 0;
        while(i<len && str[i]>='0' && str[i]<='9'){
            int add=str[i]-'0';
            //cout<<str<<' '<<add<<endl;
            if(sign == 1){
                if((INT_MAX-add)/10.0<num)return INT_MAX;
                //cout<(INT_MAX-add)/num<<endl;
            } else {
                if((-INT_MIN+add)/10.0>-num)return INT_MIN;
            }
            num = num*10 + add;
            i++;
        }
        return sign*num;
    }
};
int main(){
    Solution s;
    cout<<s.myAtoi("42")<<endl;
    cout<<s.myAtoi("   -42")<<endl;
    cout<<s.myAtoi("42 with world")<<endl;
    cout<<s.myAtoi("with world 42")<<endl;
    cout<<s.myAtoi("-91283472332")<<endl;

    return 0;
}