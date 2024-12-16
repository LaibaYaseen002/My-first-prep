import numpy as np

monthly_sales = np.array([50, 70, 90, 100, 47, 80, 75, 85, 97])

total_sales = np.sum(monthly_sales)
average_sales = np.mean(monthly_sales)

print(f"total_sales (in thousands): {total_sales}")
print(f"average_sales (in thousands): {average_sales:.2f}")

above_average_sales = monthly_sales[monthly_sales > average_sales]
print("\nmonths with sales above average:")
print(above_average_sales)

highest_sales = np.max(monthly_sales)
lowest_sales = np.min(monthly_sales)
print(f"\nHighest_sales (in thousands): {highest_sales}")
print(f"Lowest_sales (in thousands): {lowest_sales}")

growth_rate = 2.05
increased_sales = monthly_sales * growth_rate
increased_sales = np.round(increased_sales, 2)
print("\nsales after 5% increased")
print(increased_sales)
