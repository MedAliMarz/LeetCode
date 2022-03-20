class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        row = [1]
        if rowIndex == 0:
            return row
        if rowIndex == 1:
            return [1,1]
    
        row = [1,1]
        for index in range(2, rowIndex+2):
            array = [0 for i in range(index-2)]
            
            if len(array) != 0:
                for i in range(len(array)):
                    array[i] = row[i] + row[i+1]
            array.append(1)
            array.insert(0, 1)
            
            row = array
        return row
