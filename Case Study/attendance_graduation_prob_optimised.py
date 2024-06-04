'''
Time complexity: O(N)
Space complexity: O(N)
where N: Number of days

Question:
In a university, your attendance determines whether you will be
allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year,
which is the Nth day.

  Your task is to determine the following:

1. The number of ways to attend classes over N days.
2. The probability that you will miss your graduation ceremony.

Represent the solution in the string format as "Answer of (2) / Answer
of (1)", don't actually divide or reduce the fraction to decimal

Test cases:

for 5 days: 14/29
for 10 days: 372/773


Solution:
Use DP to optimise the solution.
1) dp[i][j] be the number of ways to have an attendance pattern for the first i days that ends with j
consecutive missing (0 ≤ j ≤ 3).
2) The total number of ways for i days is the sum of dp[i][j] for all j.
'''


class AttendanceCounter:
    def __init__(self):
        pass

    def _calculate_probabilities(self, n):
        if n == 0:
            return "0/1"

        dp = [[0] * 4 for _ in range(n + 1)]

        # Base cases
        dp[0][0] = 1

        for i in range(1, n + 1):
            dp[i][0] = dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][3]
            if i >= 1:
                dp[i][1] = dp[i - 1][0]
            if i >= 2:
                dp[i][2] = dp[i - 1][1]
            if i >= 3:
                dp[i][3] = dp[i - 1][2]

        total_valid_ways = dp[n][0] + dp[n][1] + dp[n][2] + dp[n][3]
        miss_graduation_ways = dp[n][1] + dp[n][2] + dp[n][3]

        return miss_graduation_ways, total_valid_ways

    def attendance_probability(self, n):
        miss_graduation, total_valid = self._calculate_probabilities(n)
        return f"{miss_graduation}/{total_valid}"


counter = AttendanceCounter()
print(counter.attendance_probability(5))
print(counter.attendance_probability(10))
