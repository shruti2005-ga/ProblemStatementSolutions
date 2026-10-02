import matplotlib.pyplot as plt
import requests

# Step 1: Fetch mock student score data from an API

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
users = response.json()

# Step 2: Prepare fake test scores for each student

students = []
scores = []

# Giving each student a score out of 100 for demonstration
sample_scores = [85, 92, 78, 88, 95, 70, 82, 90, 87, 94]

for i, user in enumerate(users[:6]):  # Take first 6 students
    students.append(user["name"])
    scores.append(sample_scores[i])

# Step 3: Calculate the average score
average_score = sum(scores) / len(scores)
for i in range(len(students)):
    print(students[i], ":", scores[i])

print("Average Score:", average_score)
# Step 4: Create a Bar Chart using matplotlib
plt.bar(students, scores, color="skyblue")

# Add a horizontal line showing the average score
plt.axhline(
    average_score,
    color="red",
    linestyle="--",
    label=f"Average: {average_score:.1f}",
)

# Chart styling
plt.xlabel("Student Name")
plt.ylabel("Test Score")
plt.title("Student Test Scores")
plt.xticks(rotation=30)  # Tilt student names so they don't overlap
plt.legend()
plt.tight_layout()

# Display the chart
plt.show()