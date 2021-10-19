#Have the function LongestWord(sen) take the sen parameter being passed and return the longest word in the string. 
#If there are two or more words that are the same length, return the first word from the string with that length. 
#Ignore punctuation and assume sen will not be empty. Words may also contain numbers, for example "Hello world123 567"
#Use the Parameter Testing feature in the box below to test your code with different arguments.

def LongestWord(sen): 
  # code goes here
  import string
  for char in string.punctuation:
    sen = sen.replace(char,' ')
  text = sen.split()
  text.sort(key = lambda x: len(x))
  return text[-1]

# keep this function call here  
# to see how to enter arguments in Python scroll down
print( LongestWord(input()) )
