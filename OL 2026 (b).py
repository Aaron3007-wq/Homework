#Author:Aaron Mclynn
#Date:21/4/26
#Desc:2026 OL Exaxm Question 1: (b)

print("Welcome to my weekly step tracker!")

total = 0

steps = []

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in days:
    step = int(input(f"Please enter the steps you did on {day}: "))
    steps.append(step)

print("The list of steps is:", steps)

total_steps = sum(steps)
print("The total steps taken this week was:", total_steps)

average_steps = total_steps / len(steps)
print("The average number of steps is:", round(average_steps, 2))

max_steps = max(steps)
print("The largest number of steps you took this week was:", max_steps)

min_steps = min(steps)
print("The smallest number of steps you took this week was:", min_steps)