class Solution:
    def average(self, salary: List[int]) -> float:
        max_sal = max(salary)
        min_sal = min(salary)
        sal = 0
        for i in range(len(salary)):
            sal += salary[i]
        return (sal - max_sal - min_sal) / (len(salary) - 2)
