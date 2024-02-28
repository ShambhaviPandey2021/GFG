//{ Driver Code Starts
#include<iostream>
#include<string.h>
using namespace std;


// } Driver Code Ends
/*Complete the function below*/

class Solution {
public:
    int isPalindrome(int num) {
        int temp = num, reverse = 0;
        while (temp > 0) {
            int digit = temp % 10;
            reverse = reverse * 10 + digit;
            temp /= 10;
        }
        return reverse == num ? 1 : 0;
    }
    
    int PalinArray(int a[], int n) {
        for (int i = 0; i < n; i++) {
            if (!isPalindrome(a[i]))
                return 0;
        }
        return 1;
    }
     
};

//{ Driver Code Starts.

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;
		int a[n];
		for(int i = 0; i < n; i++)
			cin>>a[i];
		Solution obj;
		cout<<obj.PalinArray(a,n)<<endl;
	}
}
// } Driver Code Ends