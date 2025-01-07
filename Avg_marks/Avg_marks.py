import csv

def calculate_average_marks(input_file, output_file):
    with open(input_file, mode='r') as infile:
        reader = csv.DictReader(infile)
        student_averages = []

        for row in reader:
            student_name = row['student_name']
            total_marks = 0
            num_subjects = 0
            
            try:
                for i in range(1, 6):
                    marks = int(row[f'subject{i}'])
                    
                    # Check for negative marks
                    if marks < 0:
                        raise ValueError(f"Negative marks found for {student_name} in subject{i}: {marks}")
                    elif marks>100:
                        raise ValueError(f"Marks greater than 100 for {student_name} in subject{i}: {marks}")


                    total_marks += marks
                    num_subjects += 1
                
                average_marks = total_marks / num_subjects
                
                # Store the result
                student_averages.append({
                    'student_name': student_name,
                    'average_marks': average_marks
                })
            
            except ValueError as e:
                print("Error:", e)
                continue  # Skip to the next student in case of an error

    with open(output_file, mode='w', newline='') as outfile:
        fieldnames = ['student_name', 'average_marks']
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(student_averages)

input_csv = 'student.csv'
output_csv = 'average.csv'

calculate_average_marks(input_csv, output_csv)

print("Average marks have been calculated and written to", output_csv)
