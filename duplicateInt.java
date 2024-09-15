/*
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
 */
 class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> seenValues = new HashSet(); // hashset to store seen values
        
        for (int i = 0; i < nums.length; i++) { // loop through the list
            if (seenValues.contains(nums[i])){ // we've seen this value
                return true;
            } else { // add the value to the hash
                seenValues.add(nums[i]);
            }
        }
        return false;
    }
}