class Solution {
    public int lengthOfLongestSubstring(String s) {
        

        HashMap<Character, Integer> map = new HashMap<>();

        
        int left =0;
        int right = 0;

        int res=0;

        for(right=0;right<s.length();right++)
        {
            char ch = s.charAt(right);
            if(map.containsKey(ch))
            {
                left = Math.max(map.get(ch)+1,left);
            }
            map.put(ch,right);
            res= Math.max(res,right-left+1);
        }
        return res;
    }
}
