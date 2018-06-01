word = str(input('Word to check if palindrome: '))
word_list = [x for x in word]
# print(word_list)
# print(list(reversed(word_list)))
if word_list == list(reversed(word_list)):
    print('Word is palindromic')
else:
    print('Word is not palindromic')
