class Solution:
    def countConsistentStrings(allowed, words):
        for word in words:
            for char in word:
                if char in allowed:
                    return True
                return False
    
