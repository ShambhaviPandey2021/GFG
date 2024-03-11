//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String input[] = read.readLine().split(" ");
            
            int n = Integer.parseInt(input[0]);
            int x = Integer.parseInt(input[1]);
            
            int mat1[][] = new int[n][n];
            
            for(int i = 0;i<n;i++){
                input = read.readLine().split(" ");
                for(int j = 0;j<n;j++){
                    mat1[i][j] = Integer.parseInt(input[j]);
                }
            }
            
            int mat2[][] = new int[n][n];
            
            for(int i = 0;i<n;i++){
                input = read.readLine().split(" ");
                for(int j = 0;j<n;j++){
                    mat2[i][j] = Integer.parseInt(input[j]);
                }
            }
            
        
            
            Solution ob = new Solution();
            System.out.println(ob.countPairs(mat1,mat2,n,x));
        }
    }
}
// } Driver Code Ends


//User function Template for Java

class Solution {
    int countPairs(int mat1[][], int mat2[][], int n, int x) {
        int row1 = 0, col1 = 0;
        int row2 = n - 1, col2 = n - 1;
        int count = 0;
        while (row1 < n && row2 >= 0) {
            int sum = mat1[row1][col1] + mat2[row2][col2];

            if (sum == x) {
                count++;
                col1++;
                col2--;
            } else if (sum < x) {
                col1++;
            } else {
                col2--;
            }
            
            if (col1 == n) {
                col1 = 0;
                row1++;
            }
            if (col2 < 0) {
                col2 = n - 1;
                row2--;
            }
        }
        return count;
    }
}
