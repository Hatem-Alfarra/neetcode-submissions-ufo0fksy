class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        int n = nums.size();
        int newLength = n*2;
        vector<int> ans;
        ans.resize(newLength);

        for (int i = 0; i < n; i++){
            ans[i] = nums[i];
            ans[n+i] = nums[i];
        }

        return ans;
    }
};