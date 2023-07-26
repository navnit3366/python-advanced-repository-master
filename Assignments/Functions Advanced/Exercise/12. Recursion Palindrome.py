def palindrome(word, ind):
    if word == word[::-1]:
        return f"{word} is a palindrome"
    if word[ind] != word[len(word) - 1 - ind]:
        return f"{word} is not a palindrome"
    return palindrome(word, ind + 1)


print(palindrome("abcba", 0))
print(palindrome("peter", 0))
