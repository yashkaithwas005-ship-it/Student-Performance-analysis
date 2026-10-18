import pandas as pd
import matplotlib.pyplot as plt

# Load student data
df = pd.read_csv("students.csv")

# Calculate average marks for each student
subjects = ["Python", "DBMS", "Networking"]
df["Average"] = df[subjects].mean(axis=1).round(2)

# Calculate result: pass if every subject is at least 40
df["Result"] = (df[subjects].ge(40).all(axis=1)
                .map({True: "Pass", False: "Fail"}))

print("\nSTUDENT PERFORMANCE REPORT")
print(df.to_string(index=False))

# Subject-wise average
subject_average = df[subjects].mean()

print("\nAverage marks by subject:")
print(subject_average.round(2))

# Top performer
top_student = df.loc[df["Average"].idxmax()]
print("\nTop Performer:", top_student["Name"])
print("Average Marks:", top_student["Average"])

# Pass percentage
pass_percentage = (
    df["Result"].eq("Pass").mean() * 100
)
print(f"\nPass Percentage: {pass_percentage:.2f}%")

# Create subject-wise chart
subject_average.plot(
    kind="bar",
    title="Average Marks by Subject",
    xlabel="Subject",
    ylabel="Average Marks",
    ylim=(0, 100),
    rot=0
)
plt.tight_layout()
plt.savefig("subject_analysis.png", dpi=150)
plt.show()

# Create student comparison chart
df.plot(
    x="Name",
    y="Average",
    kind="bar",
    title="Student Average Marks",
    legend=False,
    xlabel="Student",
    ylabel="Average Marks",
    ylim=(0, 100),
    rot=0
)
plt.tight_layout()
plt.savefig("student_comparison.png", dpi=150)
plt.show()