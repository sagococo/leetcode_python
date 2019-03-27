class Solution:
    def __init__(self):
        string = '.-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..'
        self.list = string.split('","')

    def word2morse(self, word):
        mor = ''
        for y in word:
            order = ord(y) - ord('a')
            mor += self.list[order]
        return mor

    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = set()
        for x in words:
            m = self.word2morse(x)
            morse.add(m)

        return len(morse)