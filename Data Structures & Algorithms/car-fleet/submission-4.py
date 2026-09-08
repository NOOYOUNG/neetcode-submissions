class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        match = {}
        for i in range(len(position)):
            match[position[i]] = speed[i]
        position.sort()

        time = []
        for i in range(len(position)):
            h = (target - position[i]) / match[position[i]]
            time.append(h)
        
        ans = []
        for i in reversed(time):
            if not ans or i > ans[-1]:
                ans.append(i)
        return len(ans)