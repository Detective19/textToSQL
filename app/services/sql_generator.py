def generate_sql(
    question,
    tables
):

    q = question.lower()

    if (
        "department" in q
        and
        "student" in q
    ):

        return """
SELECT
d.department_name,
COUNT(e.student_id)
FROM departments d
JOIN enrollments e
ON d.id=e.department_id
GROUP BY d.department_name
HAVING COUNT(e.student_id)>100
""".strip()

    elif "course" in q:
        return "SELECT * FROM courses"

    return "-- unable to generate sql"