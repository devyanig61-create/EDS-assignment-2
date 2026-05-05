# write your code here# Input
n = int(input())
marks = list(map(int, input().split()))

# Check fail condition
if any(mark < 40 for mark in marks):
    print("Fail")
else:
    # Calculate aggregate
    aggregate = sum(marks) / n

    # Print aggregate
    print(f"Aggregate Percentage: {aggregate:.2f}")

    # Determine grade
    if aggregate > 75:
        print("Grade: Distinction")
    elif aggregate >= 60:
        print("Grade: First Division")
    elif aggregate >= 50:
        print("Grade: Second Division")
    elif aggregate >= 40:
        print("Grade: Third Division")