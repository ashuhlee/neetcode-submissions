class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for char in s:
            if char in mp:
                if not st:
                    return False
                if st[-1] != mp[char]:
                    return False
                else:
                    st.pop()
            else:
                st.append(char)
        if not st:
            return True
        return False