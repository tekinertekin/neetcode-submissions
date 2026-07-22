class Solution:
    special_char = "\b"

    def encode(self, strs: List[str]) -> str:
        return "".join([x+self.special_char for x in strs])

    def decode(self, s: str) -> List[str]:
        return s.split(self.special_char)[:-1]
