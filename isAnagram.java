import java.util.Arrays;
/*
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
 */

 class Solution {
    public boolean isAnagram(String s, String t) {
        // sort and compare
        char sTemp[] = s.toCharArray();
        char tTemp[] = t.toCharArray();
        Arrays.sort(sTemp);
        Arrays.sort(tTemp);

        s = new String(sTemp);
        t = new String(tTemp);

        return s.equals(t);
    }
}