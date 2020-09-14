
def grades_to_record(n):
    student_record = {}

    for _ in range(n):
        (name , grade) = input().split(' ')
        if name not in student_record.keys():
            student_record[name] = []
        student_record[name].append(float(grade))


    return student_record

def print_record(student_record):
    for (name,grades) in student_record.items():
        print(f"{name} -> {' '.join(f'{grade:.2f}' for grade in grades)} "
              f"(avg: {sum(grades) / len(grades):.2f})")


result = grades_to_record(int(input()))
print_record(result)