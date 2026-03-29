class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded += str(len(word))+ "#" + word
        encoded += " "
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        word = ""
        number = ""
        n = 0
        is_encode = False

        for character in s:
            if is_encode == True:
                if n == 0:
                    decoded.append(word)
                    word = ""
                    number += character
                    is_encode = False
                else:
                    word += character
                    n -= 1
            elif character == '#':
                n = int(number)
                number = ""
                is_encode = True
            else:
                number += character
        return decoded
            
            
                
