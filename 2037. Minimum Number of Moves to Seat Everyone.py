class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        min_score = 0
        for i in range(len(seats)):
            min_score += abs(seats[i] - students[i])
        return min_score
