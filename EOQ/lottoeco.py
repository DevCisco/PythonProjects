import tkinter as tk
from tkinter import messagebox
import openpyxl
import datetime
import math
import os

def calculate_eoq(annual_demand, order_cost, holding_cost, product):
    eoq = math.sqrt((2 * annual_demand * order_cost) / holding_cost)
    data = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    save_to_excel(annual_demand, order_cost, holding_cost, eoq, data, product)
    return eoq

def save_to_excel(annual_demand, order_cost, holding_cost, eoq_value, data, product):
    filename = "eoq_calculation.xlsx"
    if os.path.exists(filename):
        wb = openpyxl.load_workbook(filename)
        ws = wb.active
    else:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "EOQ Calculation"
        ws.append(["Annual Demand", "Order Cost", "Holding Cost", "EOQ", "Date", "Product"])
    ws.append([annual_demand, order_cost, holding_cost, eoq_value, data, product])
    wb.save(filename)
    wb.close()

def calculate_and_display():
    try:
        product = product_entry.get()
        annual_demand = float(annual_demand_entry.get())
        order_cost = float(order_cost_entry.get())
        holding_cost = float(holding_cost_entry.get())

        if annual_demand <= 0 or order_cost <= 0 or holding_cost <= 0:
            raise ValueError("All inputs must be positive numbers.")

        eoq_value = calculate_eoq(annual_demand, order_cost, holding_cost, product)
        result_label.config(text=f"Optimal Order Quantity (EOQ): {eoq_value:.2f}")
        messagebox.showinfo("Success", "EOQ calculated and saved to Excel!")
    except ValueError as e:
        messagebox.showerror("Input Error", f"Invalid input: {e}")

# Create the main tkinter window
root = tk.Tk()
root.title("EOQ Calculator")

# Product Name
tk.Label(root, text="Product Name:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
product_entry = tk.Entry(root)
product_entry.grid(row=0, column=1, padx=10, pady=5)

# Annual Demand
tk.Label(root, text="Annual Demand:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
annual_demand_entry = tk.Entry(root)
annual_demand_entry.grid(row=1, column=1, padx=10, pady=5)

# Order Cost
tk.Label(root, text="Order Cost:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
order_cost_entry = tk.Entry(root)
order_cost_entry.grid(row=2, column=1, padx=10, pady=5)

# Holding Cost
tk.Label(root, text="Annual Holding Cost:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
holding_cost_entry = tk.Entry(root)
holding_cost_entry.grid(row=3, column=1, padx=10, pady=5)

# Calculate Button
calculate_button = tk.Button(root, text="Calculate EOQ", command=calculate_and_display)
calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.grid(row=5, column=0, columnspan=2, pady=10)

# Run the tkinter event loop
root.mainloop()