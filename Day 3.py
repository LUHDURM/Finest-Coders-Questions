import random
from typing import List, Tuple

class Codec:

    def encode(self, strs: List[str]) -> str:
       
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> Tuple[bool, List[str]]:
        
        res = []
        i = 0
        while i < len(s):
            j = i
          
            while j < len(s) and s[j] != '#':
                if not s[j].isdigit():  
                    return False, res
                j += 1
            if j == len(s):  
                return False, res

            length_str = s[i:j]
            try:
                length = int(length_str)
            except:
                return False, res

            j += 1
            word = s[j:j+length]
            if len(word) != length: 
                return False, res
            res.append(word)
            i = j + length
        return True, res

    def noisy_channel(self, encoded: str) -> str:
       
        if random.random() < 0.7:
            return encoded  
        idx = random.randint(0, len(encoded)-1)
        tampered = list(encoded)
        tampered[idx] = '@' 
        return ''.join(tampered)

    def transmit(self, strs: List[str]) -> List[str]:
      
        while True:
            encoded = self.encode(strs)
            received = self.noisy_channel(encoded)
            ok, result = self.decode(received)
            if ok:
                return result
            else:
                print("Transmission tampered! Retrying...")
