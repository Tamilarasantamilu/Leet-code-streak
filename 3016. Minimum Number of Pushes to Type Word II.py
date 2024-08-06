from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        # 📊 Calculate frequency of each character
        cnt = Counter(word)
        
        # 📈 Sort characters by their frequency in descending order
        sorted_chars = sorted(cnt, key=lambda x: -cnt[x])
        
        total_pushes = 0
        push_count = 1
        assigned_keys = 0
        
        # 🔢 Distribute characters to keys
        for char in sorted_chars:
            # 🚀 Add the number of pushes for this character
            total_pushes += cnt[char] * push_count
            assigned_keys += 1
            
            # ⏭️ After every 8 characters, increment the push count
            if assigned_keys == 8:
                push_count += 1
                assigned_keys = 0
        
        # 🎯 Return the total number of pushes
        return total_pushes
