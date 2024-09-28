# Basic salary and grade
basic = 10000  # Example basic salary
grade = 'A'    # Example grade

# Fixed percentages for calculations
hra_percentage = 0.2
da_percentage = 0.5
pf_percentage = 0.11

# Allowances based on grade
allowances = {
    'A': 1700,
    'B': 1500
}

# Get the allowance or use a default for other grades
allowance = allowances.get(grade, 1300)

# Calculate components
hra = hra_percentage * basic
da = da_percentage * basic
pf = pf_percentage * basic

# Calculate gross salary
gross_salary = round(basic + hra + da + allowance - pf)

# Output the result
print(gross_salary)
