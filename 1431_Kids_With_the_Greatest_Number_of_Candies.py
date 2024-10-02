class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = []
        sum = 0
        maxNum = 0

        for kid in range(len(candies)):
            if candies[kid] > maxNum:
                maxNum = candies[kid] 
            sum = candies[kid] + extraCandies
            maxCandies.append(sum)
        
        for i in range(len(candies)):
            if maxCandies[i] >= maxNum:
                result.append(True)
            else:
                result.append(False)
                   
        return result