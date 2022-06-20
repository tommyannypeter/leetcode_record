class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p_array = []
        for ch in p:
            if ch == '*':
                p_array[-1].set_wildcard()
            else:
                p_array.append(Pattern(ch))
        p_index = 0
        p_array_len = len(p_array)
        cursor = 0
        wildcard_indices = []
        wildcard_cursors = []
        while p_index >= 0:
            if p_index >= p_array_len:
                if cursor == len(s):
                    return True
                else:
                    if len(wildcard_cursors) != 0:
                        p_index = wildcard_indices[-1]
                        cursor = wildcard_cursors[-1]
                        wildcard_indices.pop()
                        wildcard_cursors.pop()
                        continue
                    else:
                        return False
            else:
                pattern = p_array[p_index]
                if cursor >= len(s):
                    if pattern.is_wildcard():
                        pass
                    else:
                        return False
            offset = pattern.get_num_of_ch()
            if pattern.accept(s[cursor:cursor+offset]):
                if pattern.is_wildcard():
                    wildcard_indices.append(p_index)
                    wildcard_cursors.append(cursor)
                p_index += 1
                cursor += offset
            else:
                if len(wildcard_cursors) != 0:
                    p_index = wildcard_indices[-1]
                    cursor = wildcard_cursors[-1]
                    wildcard_indices.pop()
                    wildcard_cursors.pop()
                    continue
                else:
                    return False
        return False

class Pattern:
    def __init__(self, pattern_ch: str) -> None:
        self.pattern_ch = pattern_ch
        self.num_of_ch = 1
        self.wildcard = False

    def set_wildcard(self) -> None:
        self.wildcard = True
        self.num_of_ch = 0

    def is_wildcard(self) -> bool:
        return self.wildcard

    def get_num_of_ch(self) -> int:
        return self.num_of_ch

    def accept(self, s: str) -> bool:
        if self.wildcard:
            if self.pattern_ch != '.':
                for ch in s:
                    if ch != self.pattern_ch:
                        self.num_of_ch = 0
                        return False
            self.num_of_ch += 1
            return True
        else:
            if self.pattern_ch == '.':
                if len(s) == 1:
                    return True
                else:
                    return False
            else:
                if self.pattern_ch == s:
                    return True
                else:
                    self.num_of_ch = 1
                    return False
