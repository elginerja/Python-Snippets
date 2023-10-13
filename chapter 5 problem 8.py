square_feet = float(input("please enter the square feet of wall space to be painted: "))
paint_price_per_gallon = float(input("please enter the price of paint per gallon: "))
SQUARE_FEET_PER_GALLON = 112  
LABOR_HOURS_PER_GALLON = 8  
LABOR_RATE_PER_HOUR = 35.00
gallons_required = square_feet / SQUARE_FEET_PER_GALLON
labor_hours_required = gallons_required * LABOR_HOURS_PER_GALLON
paint_cost = gallons_required * paint_price_per_gallon
labor_charges = labor_hours_required * LABOR_RATE_PER_HOUR
total_cost = paint_cost + labor_charges
print("the number of gallons of paint required is", gallons_required, 'gallons. ')
print("the hours of labor required for the job is", labor_hours_required, 'hours. ' )
print(f"the cost for all of the paint is", paint_cost, 'dollars. ')
print("the labor charges will be ", labor_charges, 'dollars. ')
print("the total cost for the whole paint job is", total_cost, 'dollars. ')





