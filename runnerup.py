'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given
n scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains n. The second line contains an array A[ ] of n integers each separated by a space.

Constraints

. 2< n ≤ 10

· -100 ≤ A[i] ≤ 100

Output Format

Print the runner-up score.

Sample Input O

5

23665

Sample Output O

5

Explanation O

Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.'''

#method1
n = int(input())
scores = list(map(int, input().split()))

unique_scores = set(scores)
unique_scores.remove(max(unique_scores))

print(max(unique_scores))

#method 2
n = int(input())
scores = list(map(int, input().split()))

scores = list(set(scores))
scores.sort()

print(scores[-2])


#method 3
n = int(input())
scores = list(map(int, input().split()))

max_score = -101
runner_up = -101

for s in scores:
    if s > max_score:
        runner_up = max_score
        max_score = s
    elif max_score > s > runner_up:
        runner_up = s

print(runner_up)

#method 4
n = int(input())
scores = list(map(int, input().split()))

max_score = max(scores)
filtered = [s for s in scores if s != max_score]

print(max(filtered))
