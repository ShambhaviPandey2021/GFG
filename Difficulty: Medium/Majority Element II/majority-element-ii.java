//{ Driver Code Starts
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine(); // Consume the newline character

        while (t-- > 0) {
            String s = sc.nextLine();
            String[] parts = s.split(" ");
            int[] nums = new int[parts.length];
            for (int i = 0; i < parts.length; i++) {
                nums[i] = Integer.parseInt(parts[i]);
            }
            Solution ob = new Solution();
            List<Integer> ans = ob.findMajority(nums);

            if (ans.size() == 0) {
                System.out.println("[]");
            } else {
                for (int i : ans) {
                    System.out.print(i + " ");
                }
                System.out.println();
            }
        }
        sc.close();
    }
}

// } Driver Code Ends


class Solution {
    // Function to find the majority elements in the array
    public List<Integer> findMajority(int[] nums) {
        // Your code goes here.
        int max=Integer.MAX_VALUE, a=max, b=a;
        int c1=0,c2=0, n=nums.length;
        for(int i:nums){
            if(a==i){
                c1++;
            }else if(b==i){
                c2++;
            }else if(c1==0){
                a=i;
                c1=1;
            }else if(c2==0){
                b=i;
                c2=1;
            }else{
                c1--;
                c2--;
            }
        }
        
        c1=0;
        c2=0;
        ArrayList<Integer> ans = new ArrayList<>();
        for(int i:nums){
            if(i==a)    c1++;
            else if(i==b)   c2++;
        }
        
        if(c1>n/3)  ans.add(a);
        if(c2>n/3)  ans.add(b);
        
        if(ans.size()==0)   return ans;
        Collections.sort(ans);
        return ans;
    }
}
