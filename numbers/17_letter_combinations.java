// // https://www.youtube.com/watch?v=tWnHbSHwNmA&ab_channel=CodeHelp-byBabbar

// class Solution {
//     public List<String> letterCombinations(String digits) {
//        List<String> ans = new ArrayList<>();
//         if (digits.length() == 0) {
//             return ans;
//         }
//         StringBuilder output = new StringBuilder();
//         int index = 0;
//         String[] mapping = new String[]{"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
//         solve(digits, output, index, ans, mapping);
//         return ans;
//     }

//      public void solve(String digit, StringBuilder output, int index, List<String> ans, String[] mapping) {
//         // Base case
//         if (index >= digit.length()) {
//             ans.add(output.toString());
//             return;
//         }

//         int number = digit.charAt(index) - '0';
//         String value = mapping[number];

//         for (int i = 0; i < value.length(); i++) {
//             output.append(value.charAt(i));
//             solve(digit, output, index + 1, ans, mapping);
//             output.deleteCharAt(output.length() - 1);
//         }

   
// }
// }