# this is not double pointer solution
class Solution1:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_true_string(prev_string):
            # slow pointer goes back for deleting
            # or use list.append/pop?
            true_string = list()
            for fast_pointer in prev_string:
                if fast_pointer != '#':
                    true_string.append(fast_pointer)
                elif fast_pointer == '#' and true_string:
                    true_string.pop()
            return "".join(true_string)
        
        s_true = get_true_string(s)
        t_true = get_true_string(t)
        if s_true == t_true:
            return True
        else:
            return False
        