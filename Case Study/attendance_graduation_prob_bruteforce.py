'''
Time complexity: 2^N
Space complexity: 2^N
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
Generate all possible sequences of attendance and missing over N days.
Filter out invalid sequences where there are four or more consecutive missed days.
Count valid sequences and specifically count those that end in one, two, or three consecutive 'M's,
indicating missing the graduation ceremony.
'''

from itertools import product


class GraduationCounter:
    def __init__(self):
        pass

    def _is_valid_sequence(self, sequence):
        max_consecutive_misses = 0
        current_misses = 0

        for char in sequence:
            if char == 'M':
                current_misses += 1
                max_consecutive_misses = max(max_consecutive_misses, current_misses)
            else:
                current_misses = 0

            if max_consecutive_misses >= 4:
                return False

        return True

    def _count_ways(self, N):
        sequences = product('AM', repeat=N)

        total_valid_sequences = 0
        miss_graduation_count = 0

        for sequence in sequences:
            sequence_str = ''.join(sequence)
            if self._is_valid_sequence(sequence_str):
                total_valid_sequences += 1
                if sequence_str.endswith('M') or sequence_str.endswith('MM') or sequence_str.endswith('MMM'):
                    miss_graduation_count += 1

        return miss_graduation_count, total_valid_sequences

    def graduation_probability(self, N):
        miss_graduation, total_valid = self._count_ways(N)
        return f"{miss_graduation}/{total_valid}"


counter = GraduationCounter()
print(counter.graduation_probability(5))
print(counter.graduation_probability(10))
