class Solution:
    def isValid(self, s: str) -> bool:
        p = ""
        for i in s:
            if i in ["(", "[", "{"]:
                p += i
            elif i in [")", "]", "}"]:
                if not p:
                    return False
                if (i == ")" and p[-1] == "(") or (i == "]" and p[-1] == "[") or (i == "}" and p[-1] == "{"):
                    p = p[0:len(p)-1]
                else:
                    return False
        return not p

        