import csv
def read_csv(file_path):
    students = []  
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)  
        for row in reader:
            students.append({'name': row['name'],'cgpa': float(row['cgpa']),  'gender': row['gender'],'major': row['major']})
    return students  
def group_students(students, group_size):
    sorted_students = sorted(students,x: x['cgpa'], reverse=True)  
    groups = [] 
    while sorted_students:  
        group = sorted_students[:group_size]  
        groups.append(group)  
        sorted_students = sorted_students[group_size:]  
    return groups
def calculate_average_cgpa(groups):
    return [sum(student['cgpa'] for student in group) / len(group) for group in groups]  
def main(file_path, group_size):
    students = read_csv(file_path)  
    groups = group_students(students, group_size) 
    averages = calculate_average_cgpa(groups)  
    for i, group in enumerate(groups):
        print(f"Group {i + 1}:")
        for student in group:
            print(f"  Name: {student['name']}, CGPA: {student['cgpa']}")
        print(f"  Average CGPA: {averages[i]:.2f}\n")  

