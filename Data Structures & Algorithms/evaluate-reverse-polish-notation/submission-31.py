class Solution:
    def _helper(self, tokens):
        if len(tokens) == 1:
            return [int(tokens[0])]
        if len(tokens) == 2:
            return tokens
        last_char = tokens[-1]
        if last_char in "+-/*":
            tokens = self._helper(tokens[0:len(tokens)-1])
            if last_char == "+":
                new_val = int(int(tokens[-2]) + int(tokens[-1]))
            elif last_char == "*":
                new_val = int(int(tokens[-2]) * int(tokens[-1]))
            elif last_char == "-":
                new_val = int(int(tokens[-2]) - int(tokens[-1]))
            elif last_char == "/":
                new_val = int(int(tokens[-2]) / int(tokens[-1]))
            return tokens[:-2] + [new_val]
        else:
            return self._helper(tokens[0:len(tokens)-1]) + [tokens[-1]]

    def evalRPN(self, tokens: List[str]) -> int:
        return int(self._helper(tokens)[0])
        
        