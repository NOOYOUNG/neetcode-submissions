class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashDict = {}

        for strr in strs:
            countDict = {}
            for s in strr:
                countDict[s] = countDict.get(s, 0) + 1

            # tuple key change
            # sort를 하지 않는 경우
            # "cat" 처리 시 -> (('c', 1), ('a', 1), ('t', 1))
            # 이 경우 act와 달라지므로 같은 키(라벨)에 들어가지 않는다.
            key = tuple(sorted(countDict.items()))

            # 존재하지 않는 키에 곧바로 .append()로 값을 넣으려고 하면 KeyError 에러 발생
            # 키(라벨)가 없다면 키(라벨)를 먼저 부여해야 한다.
            if key not in hashDict:
                hashDict[key] = []
            hashDict[key].append(strr)
        
        return list(hashDict.values())
            