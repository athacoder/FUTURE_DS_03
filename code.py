# =====================================================
# STUDENT FEEDBACK ANALYSIS (RATING-BASED)
# Internship Final Task
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------
# 1. Load Dataset
# -------------------------------
df = pd.read_csv("student_feedback.csv")

df.head()


# -------------------------------
# 2. Data Cleaning
# -------------------------------

# Drop unnecessary index column
df = df.drop(columns=["Unnamed: 0"])

# Rename columns
df = df.rename(columns={
    "Student ID": "student_id",
    "Well versed with the subject": "subject_knowledge",
    "Explains concepts in an understandable way": "concept_clarity",
    "Use of presentations": "presentation_quality",
    "Degree of difficulty of assignments": "assignment_difficulty",
    "Solves doubts willingly": "doubt_resolution",
    "Structuring of the course": "course_structure",
    "Provides support for students going above and beyond": "extra_support",
    "Course recommendation based on relevance": "course_recommendation"
})


# -------------------------------
# 3. Overall Satisfaction Score
# -------------------------------

# Calculate average feedback score per student
df["overall_rating"] = df.drop(columns=["student_id"]).mean(axis=1)

df.head()


# -------------------------------
# 4. Average Rating per Parameter
# -------------------------------

avg_scores = df.drop(columns=["student_id", "overall_rating"]).mean()

print("Average Ratings:")
print(avg_scores)


# -------------------------------
# 5. Visualization
# -------------------------------

# Bar chart: Average rating per parameter
plt.figure(figsize=(10,5))
avg_scores.sort_values().plot(kind="barh")
plt.title("Average Rating by Feedback Parameter")
plt.xlabel("Average Score")
plt.ylabel("Feedback Area")
plt.show()


# -------------------------------
# 6. Overall Satisfaction Distribution
# -------------------------------

plt.figure(figsize=(6,4))
df["overall_rating"].plot(kind="hist", bins=10)
plt.title("Overall Student Satisfaction Distribution")
plt.xlabel("Overall Rating")
plt.ylabel("Number of Students")
plt.show()


# -------------------------------
# 7. Identify Strengths & Weaknesses
# -------------------------------

strengths = avg_scores[avg_scores >= avg_scores.mean()]
weaknesses = avg_scores[avg_scores < avg_scores.mean()]

print("\nStrength Areas:")
print(strengths)

print("\nImprovement Areas:")
print(weaknesses)
