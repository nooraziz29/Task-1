def check_application(score, documents, gpa, income_verified):

    if not documents:
        return "Hold", "Documents are incomplete"

    if score < 70:
        return "Hold", "Score is less than 70"

    if gpa < 2.5:
        return "Hold", "GPA is less than 2.5"

    if not income_verified:
        return "Hold", "Income is not verified"

    return "Review", "All conditions are passed"


cases = [
    ("Pass", 82, True, 3.2, True, "Review"),
    ("GPA Check", 85, True, 2.2, True, "Hold"),
    ("Income Check", 88, True, 3.0, False, "Hold"),
    ("Boundary", 70, True, 2.5, True, "Review")
]


for name, score, documents, gpa, income, expected in cases:

    actual, reason = check_application(score, documents, gpa, income)

    print("\nCase:", name)
    print("Input:", score, documents, gpa, income)
    print("Expected:", expected)
    print("Actual:", actual)
    print("Reason:", reason)
    print("Test:", "PASS" if actual == expected else "FAIL")