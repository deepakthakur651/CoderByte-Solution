#Have the function MinWindowSubstring(strArr) take the array of strings stored in strArr, which will contain only two strings, 
#the first parameter being the string N and the second parameter being a string K of some characters, 
#and your goal is to determine the smallest substring of N that contains all the characters in K. 
#For example: if strArr is ["aaabaaddae", "aed"] then the smallest substring of N that contains the characters a, e, and d is "dae" located at the end of the string. 
# So for this example your program should return the string dae.

#Another example: if strArr is ["aabdccdbcacd", "aad"] then the smallest substring of N that contains all of the characters in K is "aabd" which is located at the beginning of the string.
#Both parameters will be strings ranging in length from 1 to 50 characters and all of K's characters will exist somewhere in the string N. Both strings will only contains lowercase alphabetic characters.

#Use the Parameter Testing feature in the box below to test your code with different arguments.

def MinWindowSubstring(strArr):

  # code goes here
  containing_string = strArr[0]
  search_string = ''.join(sorted(strArr[1]))
  
  min_chars_required = len(search_string)
  
  solution = ''
  solution_array = []
  
  cnt = 1
  for x in containing_string:
    solution += x
    total_cnt = 0
    # print(solution)
    for c in search_string:
      found_cnt = solution.count(c)
      needed_cnt = search_string.count(c)
      if found_cnt >= needed_cnt:
        total_cnt += 1
    # print(total_cnt)
    if (total_cnt == min_chars_required and cnt == 1):
      solution_array.append(solution)
      cnt += 1
      
  # print(solution_array)
  
  solution = ''
  actual_solution_array = []
  for word in solution_array:
    word = word [::-1]
    for x in word:
      solution += x
      total_cnt = 0
      # print(solution)
      for c in search_string:
        found_cnt = solution.count(c)
        needed_cnt = search_string.count(c)
        if found_cnt >= needed_cnt:
          total_cnt += 1
      # print(total_cnt)
      if total_cnt == min_chars_required:
        actual_solution_array.append(solution)
      
      
  answer = min((word for word in actual_solution_array if word), key=len)
  answer = answer [::-1]
  
  return answer

# keep this function call here 
print(MinWindowSubstring(input()))