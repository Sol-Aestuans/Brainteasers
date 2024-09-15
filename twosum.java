/*
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first. 

Example:
Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
*/

class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> complements = new HashMap(); // Hashmap to store the complements of the indexes
        Integer complement = 0;
        for (int i = 0; i < nums.length; i++) { // loop through the nums
            complement = complements.get(target - nums[i]);

            if (complement != null) { // check if the complement exists in the hash
                return new int[]{complement, i};
            } else { // update the hash with the current value
                complements.put(nums[i], i);
            }
        }
        return new int[]{}; // no sum exists
    }
}