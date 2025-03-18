import pandas
from tabulate import tabulate


def currency(x):
    """Formats numbers as currency ($#.##)"""
    return "${:.2f}".format(x)


# Lists for panda
all_items = ['A', 'B', 'C']
all_amounts = [10, 10, 10]
all_dollar_per_item = [1, 2, 3]

# Expenses dictionary
expenses_dict = {
    "Item": all_items,
    "Amount": all_amounts,
    "$ / Item": all_dollar_per_item
}

expense_frame = pandas.DataFrame(expenses_dict)
expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

# Apply currency formatting to currency columns.
add_dollars = ['Amount', '$ / Item', 'Cost']
for var_item in add_dollars:
    expense_frame[var_item] = expense_frame[var_item].apply(currency)

# print(tabulate(expense_frame, headers='keys', tablefmt='psql', showindex=False))

# use tablulate to generate a string instead of printing...
print("=== All Columns ====")
expense_string = tabulate(expense_frame, headers='keys',
                          tablefmt='psql', showindex=False)
print(expense_string)
print()

print("=== Fixed Expenses Columns ===")
fixed_string = tabulate(expense_frame[['Item', 'Cost']], headers='keys',
                        tablefmt='psql', showindex=False)
print(fixed_string)
