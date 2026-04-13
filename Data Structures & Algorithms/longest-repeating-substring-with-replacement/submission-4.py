from collections import Counter

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_run = 0
        for target_char in alphabet:
            s2 = [(True if s_char == target_char else False) for s_char in s]
            print(s2)
            remaining_k = k
            this_run = 0
            this_run_without_swaps = 0
            swaps = []
            for i in range(len(s)):
                if s2[i]:
                    this_run += 1
                    this_run_without_swaps += 1
                else:
                    swaps.append({ "index": i, "run_before": this_run_without_swaps })
                    this_run += 1
                    if remaining_k > 0:
                        remaining_k -= 1
                    else:
                        # find the earliest swap and remove it
                        earliest_swap = swaps[0]
                        swaps = swaps[1:]
                        this_run -= (earliest_swap["run_before"] + 1)
                    this_run_without_swaps = 0
                if this_run > max_run:
                    max_run = this_run
        return max_run




'''
xxxoxooxxxx
'''