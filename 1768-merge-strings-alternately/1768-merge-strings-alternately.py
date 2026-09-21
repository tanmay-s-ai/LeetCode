class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        newList = []

        def strMerge1():
            for i in range(0, len1):
                newList.append(word1[i])
                if i < len2:
                    newList.append(word2[i])
            
            return "".join(newList)

        def strMerge2():
            itr = 0
            for i in range(0, len1):
                newList.append(word1[i])
                if i < len2:
                    newList.append(word2[i])
                itr = i + 1
            for i in range(itr, len2):
                newList.append(word2[i])
            
            return "".join(newList)
        
        if len1 >= len2:
            return strMerge1()
        else:
            return strMerge2()
        