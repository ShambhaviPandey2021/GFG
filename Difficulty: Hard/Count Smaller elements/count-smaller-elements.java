//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] s = br.readLine().trim().split(" ");
            int arr[] = new int[s.length];
            for (int i = 0; i < s.length; i++) {
                arr[i] = Integer.parseInt(s[i]);
            }

            int[] ans = new Solution().constructLowerArray(arr);
            for (int i = 0; i < arr.length; i++) {
                System.out.print(ans[i] + " ");
            }
            System.out.println();
        }
    }
}

// } Driver Code Ends


// User function Template for Java

class Solution {
    int[] constructLowerArray(int[] arr) {
        // code here
        int n = arr.length;
        int[] result = new int[n];
        Pair[] pairs = new Pair[n];

        for (int i = 0; i < n; i++) {
            pairs[i] = new Pair(arr[i], i);
        }

        mergeSort(pairs, 0, n - 1, result);
        return result;
    }

    private void mergeSort(Pair[] pairs, int left, int right, int[] result) {
        if (left >= right) return;

        int mid = left + (right - left) / 2;
        mergeSort(pairs, left, mid, result);
        mergeSort(pairs, mid + 1, right, result);

        merge(pairs, left, mid, right, result);
    }

    private void merge(Pair[] pairs, int left, int mid, int right, int[] result) {
        Pair[] temp = new Pair[right - left + 1];
        int i = left, j = mid + 1, k = 0;
        int rightCounter = 0;

        while (i <= mid && j <= right) {
            if (pairs[i].value <= pairs[j].value) {
                result[pairs[i].index] += rightCounter;
                temp[k++] = pairs[i++];
            } else {
                rightCounter++;
                temp[k++] = pairs[j++];
            }
        }

        while (i <= mid) {
            result[pairs[i].index] += rightCounter;
            temp[k++] = pairs[i++];
        }

        while (j <= right) {
            temp[k++] = pairs[j++];
        }

        for (int p = left, q = 0; p <= right; p++, q++) {
            pairs[p] = temp[q];
        }
    }

    private static class Pair {
        int value;
        int index;

        Pair(int value, int index) {
            this.value = value;
            this.index = index;
        }
    }
}

