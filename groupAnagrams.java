import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Arrays;

public class groupAnagrams {
    
    public List<List<String>> groupAnagramsSolution(String[] strs) {
        HashMap<String, List<String>> anagram_groups = new HashMap<>();
    
        for (String s : strs) {
            int[] character_count = new int[26];
    
            for (char c: s.toCharArray()) { // create the count
                character_count[c - 'a']++;
            }
            String key = Arrays.toString(character_count);
    
            if (anagram_groups.containsKey(key)) {
                anagram_groups.get(key).add(s);
            } else {
                anagram_groups.put(key, new ArrayList<>());
                anagram_groups.get(key).add(s);
            }
        }
        return new ArrayList<>(anagram_groups.values());
    }
}
