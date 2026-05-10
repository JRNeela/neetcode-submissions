class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        curr = n
        while curr != 1:
            str_n = str(curr)
            total = 0
            for num in str_n:
                total += int(num)**2
            if total in seen:
                return False
            seen.add(total)
            curr = total
        return True

        