import csv
import os
from collections import defaultdict

def read_sales_data(directory):
    """
    Reads sales data from all CSV files in a given directory and its subdirectories.
    Returns a dictionary with product IDs as keys and total quantity sold as values.
    """
    sales_data = defaultdict(int)
    months = set()  # To track the number of unique months

    # Traverse through all CSV files in the directory and subdirectories
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv') and file != 'product_names.csv':
                file_path = os.path.join(root, file)
                with open(file_path, mode='r') as f:
                    reader = csv.DictReader(f)
                    for row in reader:
                        product_id = row['Product ID']
                        quantity_sold = int(row['Quantity sold'])
                        date = row['Date']
                        # Extract the month-year part from the date
                        month_year = date[:7]
                        months.add(month_year)
                        sales_data[product_id] += quantity_sold

    return sales_data, len(months)

def load_product_names(product_file):
    """
    Loads product names from the product_names.csv file and returns a dictionary mapping Product IDs to Product Names.
    """
    product_names = {}
    with open(product_file, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            product_id = row['Product ID']
            product_name = row['Produc   t Name']
            product_names[product_id] = product_name

    return product_names

def write_sales_summary(sales_data, product_names, months, output_file):
    """
    Writes the sales summary to a CSV file, including the product ID, product name, total quantity sold,
    and average quantity sold per month.
    """
    # Calculate total and average quantities sold
    sales_summary = []
    for product_id, total_quantity in sales_data.items():
        average_quantity_per_month = total_quantity / months
        product_name = product_names.get(product_id, "Unknown")
        sales_summary.append({
            'Product ID': product_id,
            'Product Name': product_name,
            'Total Quantity Sold': total_quantity,
            'Average Quantity Sold per Month': round(average_quantity_per_month, 2)
        })

    # Sort by total quantity sold in descending order
    sales_summary.sort(key=lambda x: x['Total Quantity Sold'], reverse=True)

    # Write the top 5 best-selling products to the output CSV file
    with open(output_file, mode='w', newline='') as f:
        fieldnames = ['Product ID', 'Product Name', 'Total Quantity Sold', 'Average Quantity Sold per Month']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in sales_summary[:5]:
            writer.writerow(row)

def main():
    directory = 'sales_data'  # Specify the directory containing sales data
    product_file = 'product_names.csv'
    output_file = 'sales_summary.csv'

    # Read sales data from all files in the directory
    sales_data, months = read_sales_data(directory)

    # Load product names from the product_names.csv file
    product_names = load_product_names(product_file)

    # Write the sales summary to the output CSV file
    write_sales_summary(sales_data, product_names, months, output_file)

    print(f"Sales summary has been written to {output_file}.")

if __name__ == "__main__":
    main()
