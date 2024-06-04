# University Graduation Attendance Problem

## Problem Description

In a university, your attendance record determines whether you will be allowed to attend your graduation ceremony. The rules are as follows:

1. The academic year has N days.
2. You are not allowed to miss classes for four or more consecutive days.
3. Your graduation ceremony is on the last day (day N) of the academic year.

Your task is to determine:
1. The total number of valid attendance patterns over N days.
2. The probability that you will miss your graduation ceremony.

The solution should be represented as a string in the format "X/Y", where:
- X = Number of ways you miss graduation
- Y = Total number of valid attendance patterns

Do not reduce the fraction or convert it to a decimal.

### Examples

- For 5 days: `"14/29"`
- For 10 days: `"372/773"`

## Solutions

We present two solutions to this problem:
1. Optimized Dynamic Programming (DP) Solution(Time Complexity: `O(N)`) `attendance_graduation_prob_optimised.py`
2. Brute Force Solution (Time Complexity: `O(2^N)`)`attendance_graduation_prob_bruteforce.py`

### 1. Optimized Dynamic Programming Solution

The DP solution leverages the problem's structure to efficiently compute the answer in O(N) time.

#### Key Insights
1. State Design: `dp[i][j]` = number of valid patterns for the first `i` days, ending with `j` consecutive absences (0 ≤ j ≤ 3).
2. Constraint as Guide: The "no 4 absences" rule shapes our state design.
3. Order Matters: Building day-by-day respects decision order.
4. End-State Focus: Perfect for questions about the last day.

#### Algorithm
1. Initialize `dp` table: `dp[i][j]` for 0 ≤ i ≤ N, 0 ≤ j ≤ 3.
2. Base case: `dp[0][0] = 1`, others 0.
3. For i = 1 to N:
   a. Attend day i: `dp[i][0] = sum(dp[i-1][j])` for 0 ≤ j ≤ 3
   b. Don't attend:
      - `dp[i][1] = dp[i-1][0]`
      - `dp[i][2] = dp[i-1][1]`
      - `dp[i][3] = dp[i-1][2]`
4. Total patterns: `sum(dp[N][j])` for 0 ≤ j ≤ 3
5. Miss graduation: `sum(dp[N][j])` for 1 ≤ j ≤ 3
