def validPalindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return self.is_palidin(s, left + 1, right) or self.is_pladin(s, left, right - 1)

        else:
            left += 1
            right -= 1

    return True

def is_pladin(self, s, right, left):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left +=1
            right +=1

    return True



if __name__ == '__main__':
    print(validPalindrome("abca"))