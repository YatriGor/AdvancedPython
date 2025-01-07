import csv
from fpdf import FPDF
from PyPDF2 import PdfMerger
from datetime import date

def create_invoice(order):
    # Prepare invoice data
    order_id = order['Order ID']
    customer_name = order['Customer Name']
    product_name = order['Product Name']
    quantity = int(order['Quantity'])
    unit_price = float(order['Unit Price'])
    total_amount = quantity * unit_price


    pdf_file = f"invoice_{order_id}.pdf"
    
 
    pdf = FPDF()
    pdf.add_page()


    pdf.set_font("Arial", "B", 16)
    pdf.cell(200, 10, f"Invoice Number: {order_id}", ln=True, align="C")

    pdf.ln(10)

    pdf.set_font("Arial", "B", 12)
    pdf.set_fill_color(169, 169, 169)  # Gray background for headers
    pdf.cell(90, 10, "Field", 1, 0, "C", fill=True)
    pdf.cell(100, 10, "Value", 1, 1, "C", fill=True)

    pdf.set_font("Arial", "", 12)
    pdf.set_fill_color(245, 245, 245)  # Light fill for rows

    # cell(width, height, text, border, ln, align, fill)
    pdf.cell(90, 10, "Date of Purchase:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, str(date.today()), 1, 1, "L")

    pdf.cell(90, 10, "Customer Name:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, customer_name, 1, 1, "L")

    pdf.cell(90, 10, "Product Name:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, product_name, 1, 1, "L")

    pdf.cell(90, 10, "Quantity:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, str(quantity), 1, 1, "L")

    pdf.cell(90, 10, "Unit Price:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, f"${unit_price:.2f}", 1, 1, "L")

    pdf.cell(90, 10, "Total Amount:", 1, 0, "L", fill=True)
    pdf.cell(100, 10, f"${total_amount:.2f}", 1, 1, "L")
    
    
    pdf.output(pdf_file)


def combine_invoices(order_ids):
    merger = PdfMerger()
    for order_id in order_ids:
        merger.append(f"invoice_{order_id}.pdf")
    merger.write("merged_invoices.pdf")
    merger.close()


def process_csv(csv_file):
    order_ids = []
    
    with open(csv_file, newline='') as file:
        reader = csv.DictReader(file)
        for order in reader:
            create_invoice(order)
            order_ids.append(order['Order ID'])
    
    combine_invoices(order_ids)

csv_file = input("Enter the CSV file name (e.g., orders.csv): ")

process_csv(csv_file)
