import itertools

class Solution:
    def get_digits(self, numero: int) -> list[int]:
        return [int(digito) for digito in str(numero)]
    
    def separateDigits(self, nums: list[int]) -> list[int]:
        return list(itertools.chain.from_iterable(map(self.get_digits, nums)))
    

if __name__ == "__main__":
     nums = [13,25,83,77]
     answer = Solution()
     print(answer.separateDigits(nums))
