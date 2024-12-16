import numpy as np

scores = np.array([45, 60, 57, 85, 89, 97, 90, 86])
average_scores = np.mean(scores)
print(f"Average Score: {average_scores}")

above_average = scores[scores > average_scores]
print("\nEmployees scoring above average:")
print(above_average)

sorted_scores = np.sort(scores)[::-1]
print("\nsoretd scores (Descending order):")
print(sorted_scores)

highest_scores = np.max(scores)
lowest_scores = np.min(scores)
print(f"\nhighest_scores: {highest_scores}")
print(f"\nlowest_scores: {lowest_scores}")

increase_scores = scores * 1.10
increase_scores = np.round(increase_scores, 2)
print("\nscores after 10%  increase:")
print(increase_scores)
