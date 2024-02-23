//{ Driver Code Starts
#include<bits/stdc++.h>

using namespace std;


// } Driver Code Ends


class twoStacks
{

public:
    stack<int> s1, s2;
    
    twoStacks() {}
 

    void push1(int x) {
        s1.push(x);
    }
 
    void push2(int x) {
        s2.push(x);
    }
    
   
    int pop1() {
        if (s1.empty()) return -1;
        int top = s1.top();
        s1.pop();
        return top;
    }
    

    int pop2() {
        if (s2.empty()) return -1;
        int top = s2.top();
        s2.pop();
        return top;
    }
};


//{ Driver Code Starts.

int main()
{

    int T;
    cin>>T;
    while(T--)
    {
        twoStacks *sq = new twoStacks();

        int Q;
        cin>>Q;
        while(Q--){
        int stack_no;
        cin>>stack_no;
        int QueryType=0;
        cin>>QueryType;
        
        if(QueryType==1)
        {
            int a;
            cin>>a;
            if(stack_no ==1)
            sq->push1(a);
            else if(stack_no==2)
            sq->push2(a);
        }else if(QueryType==2){
        	if(stack_no==1)
            cout<<sq->pop1()<<" ";
            else if(stack_no==2)
            cout<<sq->pop2()<<" ";

        }
        }
        cout<<endl;
    }
}

// } Driver Code Ends