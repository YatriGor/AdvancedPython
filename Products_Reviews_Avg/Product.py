import csv
from collections import defaultdict

csv_files = [
    'file1.csv', 'file2.csv', 'file3.csv', 'file4.csv', 'file5.csv',
    'file6.csv', 'file7.csv', 'file8.csv', 'file9.csv', 'file10.csv'
]

product_ratings = defaultdict(lambda: {'total_rating': 0.0, 'count': 0})

total_reviews_processed = 0
valid_reviews = 0
invalid_reviews = 0

for file_name in csv_files:
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        for row in reader:
            total_reviews_processed += 1
            if len(row) != 5:
                invalid_reviews += 1
                continue
            customer_id, product_id, review_date, rating, text = [item.strip() for item in row]
            try:
                rating = float(rating)
                product_ratings[product_id]['total_rating'] += rating
                product_ratings[product_id]['count'] += 1
                valid_reviews += 1
            except ValueError:
                invalid_reviews += 1
            except KeyError:
                invalid_reviews += 1

average_ratings = {}
for product_id, data in product_ratings.items():
    if data['count'] > 0:
        average_ratings[product_id] = data['total_rating'] / data['count']

sorted_products = sorted(average_ratings.items(), key=lambda x: x[1], reverse=True)
top_3_products = sorted_products[:3]

with open('output.txt', mode='w') as file:
    file.write("Total Reviews Processed: {}\n".format(total_reviews_processed))
    file.write("Total Valid Reviews: {}\n".format(valid_reviews))
    file.write("Total Invalid Reviews: {}\n".format(invalid_reviews))
    file.write("\nAverage Ratings:\n")
    for product_id, avg_rating in average_ratings.items():
        file.write(f"Product ID: {product_id}, Average Rating: {avg_rating:.2f}\n")
    
    file.write("\nTop 3 Products with Highest Average Ratings:\n")
    for product_id, avg_rating in top_3_products:
        file.write(f"Product ID: {product_id}, Average Rating: {avg_rating:.2f}\n")

print("Results written to output.txt")