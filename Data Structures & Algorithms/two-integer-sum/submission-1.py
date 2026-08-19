class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}
        
        # enumerate(): 리스트나 튜플 같은 순회 가능한(iterable) 객체를 넣었을 때, 
        #              (인덱스 번호, 요소 값) 형태의 짝(tuple)으로 묶어서 꺼내주는 파이썬 내장 함수
        # i : 현재 요소의 위치 번호
        # n : 해당 위치에 들어있는 실제 값
        for i, n in enumerate(nums):
            diff = target - n
            if diff in answer:
                return [answer[diff], i]
            answer[n] = i