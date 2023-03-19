result = 0.0
grade_all = 0.0

for i in range(0, 20):
    subject, grade, rating = input().split()
    if rating == "A+":
        result += 4.5 * float(grade)
        grade_all += float(grade)
    if rating == "A0":
        result += 4.0 * float(grade)
        grade_all += float(grade)
    if rating == "B+":
        result += 3.5 * float(grade)
        grade_all += float(grade)
    if rating == "B0":
        result += 3.0 * float(grade)
        grade_all += float(grade)
    if rating == "C+":
        result += 2.5 * float(grade)
        grade_all += float(grade)
    if rating == "C0":
        result += 2.0 * float(grade)
        grade_all += float(grade)
    if rating == "D+":
        result += 1.5 * float(grade)
        grade_all += float(grade)
    if rating == "D0":
        result += 1.0 * float(grade)
        grade_all += float(grade)
    if rating == "F":
        result += 0.0 * float(grade)
        grade_all += float(grade)
    if rating == "P":
        pass

print(result / grade_all)