# longestCommonSubstring(s1, s2)[20 pts]
# Write the function, longestCommonSubstring(s1, s2), that takes two possibly-empty strings and returns the longest 
# string that occurs in both strings (and returns the empty string if either string is empty). For example:
# longestCommonSubstring("abcdef", "abqrcdest") returns "cde"
# longestCommonSubstring("abcdef", "ghi") returns "" (the empty string)
# If there are two or more longest common substrings, return the lexicographically smaller one (ie, just use "<" to 
# compare the strings). So, for example:
# longestCommonSubstring("abcABC", "zzabZZAB") returns "AB" and not "ab"

def longestcommonsubstring(s1, s2):
    answer=""
    len1=len(s2)
    len2=len(s1)
    for i in range(len1):
        match=""
        for j in range(len2):
            if (i+j<len1 and s2[i+j]==s1[j]):
                match+=s1[j]
            else:
                if (len(match)>=len(answer)):
                    answer=match
                    match = ""
    return answer

print(longestcommonsubstring("abcdef", "abqrcdest"))
print(longestcommonsubstring("abcdef", "ghi")) 
print(longestcommonsubstring("abABC", "abcAB"))
print(longestcommonsubstring("abcdef", "abqrcdest"))
print(longestcommonsubstring("abcdef", "ghi"))
print(longestcommonsubstring("", "abqrcdest"))
print(longestcommonsubstring("abcdef", ""))
print(longestcommonsubstring("abcABC", "zzabZZAB"))