class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word))+ "#" + word
        encoded += " "
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        sLength = len(s)

        while (i < sLength-1):
            j = i
            while s[j] != "#":
                j += 1
            
            wordLength = int("".join(s[i:j]))
            word = s[j+1 : j+wordLength+1]
            i = j = j+wordLength+1

            decoded.append(word)
        return decoded