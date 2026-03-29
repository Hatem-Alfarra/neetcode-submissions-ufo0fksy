class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += "THEN" + word
        return encoded

    def decode(self, s: str) -> List[str]:
        return s.split("THEN")[1:]
