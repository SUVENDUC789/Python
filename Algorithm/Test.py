class Solution:
    def __senToList(self,sen: str) -> list:
        d = {}
        for i in sen:
            d[i] = 0
        charlist = list(d.keys())
        charlist.sort()
        return charlist

    def __foundAllCharacter(self) -> list:
        sen = "thequickbrownfoxjumpsoverthelazydog"
        return self.__senToList(sen)

    def __ExtractCharToSentence(self, sen: str) -> list:
        return self.__senToList(sen)

    def checkIfPangram(self, sen: str) -> bool:
        a = self.__foundAllCharacter()
        b = self.__ExtractCharToSentence(sen)
        return a == b