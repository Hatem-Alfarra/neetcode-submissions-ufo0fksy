public class Solution {
    public int RemoveElement(int[] nums, int val) {
        int k = 0;
        int length = nums.Length;
        for (int i = 0; i < length; i++){
            if (nums[i] != val){
                if (i != k){
                    nums[k] = nums[i];
                }
                k++;
            }
        }
        return k;
    }
}