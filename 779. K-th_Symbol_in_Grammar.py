class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if k <= 4:
            return int((k % 4) / 2)
        
        def final_out(base, transform):
            if base == 0:
                if transform == 0:
                    return 0
                return 1
            else:
                if transform == 0:
                    return 1
                return 0
        
        start_power = 0
        k_div = k
        while k_div > 1:
            k_div /= 2
            start_power += 1
        
        current_val = k
        transform = 0
        for power in range(start_power, 1, -1):
            prev_val = current_val
            two_power = 2 ** power
            if prev_val <= two_power:
                current_val = prev_val
            else:
                current_val = two_power - ((prev_val - 1) % two_power)
            if power % 2 == 0 and current_val != prev_val:
                transform += 1

        base = int((k % 4) / 2)

        return final_out(base, transform % 2)
