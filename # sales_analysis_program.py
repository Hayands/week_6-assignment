# sales_analysis_program

import csv
from collections import defaultdict

# Function to read the CSV file and convert it into a list of dictionaries
def read_csv_to_dict(filename):
    data = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Read CSV as a dictionary
        for row in reader:
            row['product'] = row['product'].capitalize()  # Standardize product names (e.g., "widgets" -> "Widgets")
            data.append(row)
    return data

# Function to analyze sales data
def analyze_sales(data):
    total_sales = 0  # Total number of sales
    region_sales = defaultdict(int)  # Dictionary to store sales per region
    product_sales = defaultdict(int)  # Dictionary to store sales per product
    region_product_sales = defaultdict(lambda: defaultdict(int))  # Nested dictionary for region-wise product sales
    
    for row in data:
        region = row['region']  # Extract region
        product = row['product']  # Extract product name
        sales = int(row['sales'])  # Convert sales from string to integer
        
        total_sales += sales  # Accumulate total sales
        region_sales[region] += sales  # Update sales per region
        product_sales[product] += sales  # Update sales per product
        region_product_sales[region][product] += sales  # Update sales for a specific product in a region
    
    # Determine the top 3 regions by total sales
    top_regions = sorted(region_sales.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Define product prices
    prices = {'Bobbles': 10.99, 'Widgets': 15.99}
    
    # Calculate revenue for each product
    revenue = {product: product_sales[product] * prices[product] for product in product_sales}
    
    # Determine which product generated the highest revenue
    highest_revenue_product = max(revenue, key=revenue.get)
    
    # Find the region-product combination with the lowest sales
    min_region_product = min(((r, p, s) for r, products in region_product_sales.items() for p, s in products.items()), key=lambda x: x[2])
    
    return total_sales, top_regions, product_sales, revenue, highest_revenue_product, min_region_product

# Example Usage
filename = r"C:\Users\quinn\Desktop\sales_data (2).csv"  
data = read_csv_to_dict(filename)
results = analyze_sales(data)

total_sales, top_regions, product_sales, revenue, highest_revenue_product, min_region_product = results

# Print results
print("\nSales Analysis Report")
print("----------------------")
print(f"Total Sales: {total_sales}")
print("Top 3 Regions by Sales:")
for region, sales in top_regions:
    print(f"  - {region}: {sales}")
print("\nProduct Sales:")
for product, sales in product_sales.items():
    print(f"  - {product}: {sales}")
print("\nRevenue Generated:")
for product, rev in revenue.items():
    print(f"  - {product}: ${rev:.2f}")
print(f"\nHighest Revenue Product: {highest_revenue_product}")
print(f"Least Sold Product: Region={min_region_product[0]}, Product={min_region_product[1]}, Sales={min_region_product[2]}")
