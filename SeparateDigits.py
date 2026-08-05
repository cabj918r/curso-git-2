class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        nums_txt = ""
        digits_list = []
        for num in nums:
          nums_txt = nums_txt+str(num)
        for digit in nums_txt:
            digits_list.append(int(digit))
        return digits_list
    

if __name__ == "__main__":
     nums = [13,25,83,77]
     answer = Solution()
     print(answer.separateDigits(nums))

        

            