class Solution {
    public String solution(String my_string, int[] index_list) {
        String answer = "";
        String[] res = my_string.split("");
        for(int i =0;i<index_list.length;i++){
            answer+=res[index_list[i]];
        }
        return answer;
    }
}