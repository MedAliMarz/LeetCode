class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        
        for index in range(2, numRows+1):
            array = [0 for i in range(index-2)]
            
            if len(array) != 0:
                for i in range(len(array)):
                    array[i] = rows[-1][i]+ rows[-1][i+1]
            array.append(1)
            array.insert(0, 1)
            
            rows.append(array)
        return rows
