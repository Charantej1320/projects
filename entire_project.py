import csv

APP_NAME = "Instagram"
time_spent = []


with open("projects/digital_behaviour.csv", "r", encoding="utf-8") as f1:
    reader = csv.DictReader(f1)
    for row in reader:
        time_spent.append(int(row["Instagram_Minutes"]))
print(time_spent[:])
total_time=sum(time_spent)
highest_time=max(time_spent)
lowest_time=min(time_spent)
average_time=total_time/len(time_spent)
print(f"App Name: {APP_NAME}")
print(f"Total time spent on {APP_NAME} is {total_time} minutes.")
print(f"Average time spent on {APP_NAME} is {average_time:.2f} minutes.")
print(f"Highest time spent on {APP_NAME} is {highest_time} minutes.")
print(f"Lowest time spent on {APP_NAME} is {lowest_time} minutes.")
#above Average time spent on Instagram
#Above_average_time = [time for time in time_spent if time > average_time]
#print(f"Number of days spent above average time on {APP_NAME} is {len(Above_average_time)} days.")
count=0
for value in time_spent:
    if value>average_time:
        count+=1
print(f"Number of days spent above average time on {APP_NAME} is {count} days.")
