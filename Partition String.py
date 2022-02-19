Given a lowercase alphabet string s, partition s into as many pieces as possible such that 
each letter appears in at most one piece and return the sizes of the partitions as a list.

Constraints
0 ≤ n ≤ 100,000 where n is the length of s
Input
s = "cocoplaydae"
Output
[4, 1, 1, 4, 1]
Explanation
The string is split to["coco", "p", "l", "ayda", "e"]

class Solution:
    def process(self, s,curr, last_index_map):
        last_index = last_index_map[s[curr]]
        ans = last_index
        for i in range(curr+1, last_index+1):
            ans = max(ans, last_index_map[s[i]])
        return ans

    def solve(self, s):
        last_index_map={}
        index = len(s)-1
        for i in s[::-1]:
            if i not in last_index_map:
                last_index_map[i] = index
            index -= 1
        ans = []
        last_index = None
        for index,char in enumerate(s):
            if last_index is not None and index <= last_index:
                continue
            if index == last_index_map[char]:
                ans.append(char)
                last_index = index
                continue

            last_index = self.process(s, index, last_index_map)
            ans.append(s[index: last_index+1])
        # print(ans)
        return list(map(lambda x: len(x), ans))
