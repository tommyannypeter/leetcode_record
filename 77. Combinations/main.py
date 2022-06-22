class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.n = n
        self.ans = []
        self.loop(1, n - k + 1, [])
        return self.ans
            
    def loop(self, start: int, end: int, previous_elements: list) -> None:
        for iii in range(start, end + 1):
            current_elements = previous_elements.copy()
            if end == self.n:
                final_elements = current_elements.copy()
                final_elements.append(iii)
                self.ans.append(final_elements)
            else:
                current_elements.append(iii)
                self.loop(iii + 1, end + 1, current_elements)
