import employee_data

employee_data.basic_salary 
employee_data.ot_hours       
employee_data.ot_rate   

total_salary = employee_data.basic_salary + (employee_data.ot_hours * employee_data.ot_rate)
deduc = (total_salary + (total_salary * (0.11 + 0.005 + 0.0020))) + 50 + 30
net_salary = total_salary - deduc
print(f"Net Salary: {net_salary} (Type: {float(net_salary)})")
print(f"Total Salary: {total_salary} (Type: {float(total_salary)})")
print(f"Deductions: {deduc} (Type: {float(deduc)})")

