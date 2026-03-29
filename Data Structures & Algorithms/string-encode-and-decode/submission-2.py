class Solution:
    # using digits count of count before count of word then letters count of word then word
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            wordLength = len(word)
            lengthOfWordLength = len(str(wordLength))

            encoded_string += str(lengthOfWordLength)
            encoded_string += str(wordLength)
            encoded_string += word 
        return encoded_string

    def decode(self, s: str) -> List[str]:
        encoded_list = list(s)
        messageLength = len(encoded_list)
        decoded_list = []

        i = 0
        while (i < messageLength):
            digitslength = int(encoded_list[i])
            wordlengthList = encoded_list[i+1: i+digitslength+1]
            wordlength = str()
            for digit in wordlengthList:
                wordlength += str(digit)
            wordlength = int(wordlength)
            # wordlength = int("".join(wordlengthList))
            # i = 0
            # digitslength = 1
            # wordlengthList = [4]
            # wordlength = 4
            # word = 
            # [1, 4, w, o, r, d]
            word = "".join(encoded_list[i+1+digitslength : i+1+digitslength+wordlength])
            decoded_list.append(word)

            i += 1+digitslength+wordlength

        return decoded_list

        


