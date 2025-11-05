# Q4. Lexicographically Smallest Palindromic Permutation Greater Than Target
# Hard
# 6 pt.
# You are given two strings s and target, each of length n, consisting of lowercase English letters.

# Return the lexicographically smallest string that is both a palindromic permutation of s and strictly greater than target. If no such permutation exists, return an empty string.

#  

# Example 1:

# Input: s = "baba", target = "abba"

# Output: "baab"

# Explanation:

# The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
# The lexicographically smallest permutation that is strictly greater than target is "baab".
# Example 2:

# Input: s = "baba", target = "bbaa"

# Output: ""

# Explanation:

# The palindromic permutations of s (in lexicographical order) are "abba" and "baab".
# None of them is lexicographically strictly greater than target. Therefore, the answer is "".
# Example 3:

# Input: s = "abc", target = "abb"

# Output: ""

# Explanation:

# s has no palindromic permutations. Therefore, the answer is "".

# Example 4:

# Input: s = "aac", target = "abb"

# Output: "aca"

# Explanation:

# The only palindromic permutation of s is "aca".
# "aca" is strictly greater than target. Therefore, the answer is "aca".
#  

# Constraints:

# 1 <= n == s.length == target.length <= 300
# s and target consist of only lowercase English letters.

##########################################################################

# # make the counts dictionary 
# s = 'baba'
# target = 'abba'


# dict_s = {} 
# for i in s: 
#     if i not in dict_s.keys():
#         dict_s[i] = 1 
#     else: 
#         dict_s[i] += 1 

# # check for palindromic possibility 
# odd_flag = 0
# for i in dict_s.values(): 
#     if i%2 == 1: # odd 
#         odd_flag += 1 
#         if odd_flag >= 2: 
#             print("") 
#             break

# # adding the even-count characters 
# output = ""
# for i in sorted(list(dict_s.keys())):
#     if dict_s[i] % 2 == 0 and len(output) <= len(s)//2: 
#         if i == 0 and i > target[0]:
#             output += i

# # adding the middle odd-count character 
# for i in list(dict_s.keys()): 
#     if dict_s[i] % 2 == 1:
#         output += i 

# # for i in range(len(s)//2 - 1, -1, -1):
# #     output += output[i]

# print(output) 

print('b' > 'a')
