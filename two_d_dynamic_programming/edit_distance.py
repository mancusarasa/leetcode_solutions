class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        C = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            C[i][0] = i
        for j in range(1, n+1):
            C[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    C[i][j] = C[i-1][j-1]
                else:
                    C[i][j] = min(
                        C[i-1][j] + 1,
                        C[i][j-1] + 1,
                        C[i-1][j-1] + 1
                    )
        return C[-1][-1]
