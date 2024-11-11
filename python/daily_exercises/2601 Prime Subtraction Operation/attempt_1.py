import math


class Solution(object):
    def primeSubOperation(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_element = max(nums)
        sieve = [True for _ in range(max_element + 1)]
        sieve[0] = False

        for i in range(2, int(math.sqrt(max_element + 1)) + 1):
            if (sieve[i] == True):
                for j in range(i * i, max_element + 1, i):
                    sieve[j] = False

        next_smallest_prime_dic = {}
        next_smallest_prime_dic[0] = 0
        next_smallest_prime_dic[1] = 0
        previous_prime = 1
        for i, is_prime in enumerate(sieve):
            if i > 1:
                if is_prime:
                    next_smallest_prime_dic[i] = i
                    previous_prime = i
                else:
                    next_smallest_prime_dic[i] = previous_prime

        prev_number = 0
        for num in nums:
            if prev_number >= num:
                return False
            max_new_num = num - prev_number - 1
            print(max_new_num)
            next_smallest_prime = next_smallest_prime_dic[max_new_num]
            new_num = num - next_smallest_prime

            prev_number = new_num

        return True
