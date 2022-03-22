class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        parts = dict.fromkeys(set(s), 0)
        occ = collections.Counter(s)
        
        part = 1
        parts[s[0]] = 1
        indexes = {
            1: 0
        }
        for index, char in enumerate(s):
            if parts[char] != 0:
                for i in range(indexes[parts[char]], index+1):
                    parts[s[i]] = parts[char]
                part = parts[char]
            else:
                part += 1
                parts[char] = part
                indexes[part] = index
        
        rdict = dict.fromkeys(set(parts.values()), 0)
        for key in parts:
            rdict[parts[key]] += occ[key]
        
        return [tpl[1] for tpl in sorted(rdict.items(), key= lambda x:x[0])] 
