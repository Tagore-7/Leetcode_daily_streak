class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        current_cost = 0
        left = 0
        largest_sub_string_value = 0
        for charc in range(len(s)):
            # print(charc)
            current_cost += abs(ord(s[charc]) - ord(t[charc]))
            # print(current_cost)
            while current_cost > maxCost:
                # print(current_cost)
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                # print(left)
                left += 1
            largest_sub_string_value = max(largest_sub_string_value, charc - left + 1)
        return largest_sub_string_value
