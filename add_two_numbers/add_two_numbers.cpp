#include<iostream>
using namespace std;

 struct ListNode {
     int val;
     ListNode *next;
     ListNode(int x) : val(x), next(NULL) {}
 };
 
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode * result = NULL, *p = NULL, *p1 = NULL;
        int jinwei = 0;
        while(l1 != NULL || l2 != NULL || jinwei != 0){
            int l1val = 0, l2val = 0;
            if(l1 != NULL){
                l1val = l1->val;
                l1 = l1->next;
            }
            if(l2 != NULL){
                l2val = l2->val;
                l2 = l2->next;
            }
            int x = (l1val + l2val + jinwei);
            jinwei = x/10;
            x %= 10;
            p1 = new ListNode(x);
            if(p == NULL){
                p = p1;
            } else {
                p->next = p1;
                p = p->next;
            }
            if(result == NULL){
                result = p;
            }  
        }
        return result;
    }
};

ListNode* createList(int a[], int n){
    ListNode* res = NULL, *p = NULL, *p1 = NULL;
    for(int i=0; i<n; i++){
        p1 = new ListNode(a[i]);
        if(p == NULL){
            p = p1;
        } else{
            p->next = p1;
            p = p->next;
        }
        if(res == NULL){
            res = p;
        }
    }
    return res;
}
void printList(ListNode* list){
    if(list == NULL){
        return;
    }
    printList(list->next);
    cout<<list->val;
}
int main(){
    int a[] = {2, 4, 3};
    int b[] = {5, 6, 4};
    ListNode* l1 = createList(a, 3);
    printList(l1);
    ListNode* l2 = createList(b, 3);
    printList(l2);
    Solution s;
    ListNode* l3 = s.addTwoNumbers(l1, l2);
    printList(l3);
    return 0;
}