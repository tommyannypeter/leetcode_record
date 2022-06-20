import time

from math import sqrt

class SolutionOld:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        all_numbers = list(range(2, n))
        check_limit = sqrt(n)
        check_num = 2
        while check_num < check_limit:
            remove_list = []
            for ite in range(len(all_numbers)):
                number = all_numbers[ite]
                if number % check_num == 0 and number != check_num:
                    remove_list.append(number)
            all_numbers = list(set(all_numbers) - set(remove_list))
            all_numbers.sort()
            check_num = all_numbers[all_numbers.index(check_num) + 1]
        return len(all_numbers)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n == 0 or n == 1:
            return 0
        tags = []
        for _ in range(n):
            tags.append(True)
        count = 0
        for iii in range(2, n):
            if tags[iii]:
                count += 1
                for jjj in range(iii * iii, n, iii):
                    tags[jjj] = False
        return count

solution = Solution()
print(solution.countPrimes(0))
print(solution.countPrimes(1))
print(solution.countPrimes(2))
print(solution.countPrimes(3))
print(solution.countPrimes(4))
print(solution.countPrimes(5))
print(solution.countPrimes(6))
print(solution.countPrimes(7))
print(solution.countPrimes(8))
print(solution.countPrimes(9))
print(solution.countPrimes(10))
print(solution.countPrimes(100))
print(solution.countPrimes(1000))
print(solution.countPrimes(10000))
print(solution.countPrimes(100000))
start_time = time.time()
print(solution.countPrimes(1000000))
end_time = time.time()
print("It takes", end_time - start_time, "seconds")
