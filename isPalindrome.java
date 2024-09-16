/*
Given a string s, return true if it is a palindrome, otherwise return false.

A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

Example 1:

Input: s = "Was it a car or a cat I saw?"

Output: true
 */
class Solution {
    public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "").toLowerCase(); // remove all non alphanumeric chars
        char[] charArray = s.toCharArray();

        int last_index = s.length();
        
        for (int i = 0; i < (last_index/2); i++) {
            if (charArray[i] != charArray[last_index - 1 - i]) {
                return false;
            }
        }
        return true;
    }
}