def longestSubstrDitinctChars(S):
    # Time Complexity required is O(N) where N is length of string
    # Space Complexity required is O(1) here only unique characters are stored which are constant i.e. 26 alphabets only
    try:
        length = len(S)
        left = right = result = 0
        uniqueChar = set()  # it will contain only constant unique characters i.e. constant size 26 for alphabets

        if length<1 or length>105:
            raise Exception('Size Constraint Error: Length of string is less than 1 or greater than 105')
        while right < length:
            if S[right] in uniqueChar:
                uniqueChar.remove(S[left])
                left += 1
            else:
                uniqueChar.add(S[right])
                right += 1
                result = max(result, right - left)

        return result
    except Exception as e:
        return 'Exception Occured ' + str(e)
