class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = 0
        current_time = 0
        for arr, ord in customers:
            if current_time < arr:
                current_time = arr
            waiting_time = current_time - arr + ord
            total_time += waiting_time
            current_time += ord
        return total_time / len(customers)
