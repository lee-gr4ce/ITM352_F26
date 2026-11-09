# REQUIRMENET 1

import pandas as pd
import pyarrow as pa
import time
from pathlib import Path


ORIGINAL_CSV = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
SAMPLE_CSV = Path(__file__).with_name("sales_data_sample.csv")
SAMPLE_MAX_ROWS = 1000

def load_csv(filepath):
    print(f"Loading CSV file from: {filepath}")
    start_time = time.time()

    try:
        df = pd.read_csv(filepath, engine = 'pyarrow', on_bad_lines='skip')
        end_time = time.time()
        load_time = end_time - start_time
        print(f"CSV file loaded successfully in {load_time:.2f} seconds.") 
        print(f"Number of rows: {len(df)}")
        print(f"Columns: {list(df.columns)}")
        return df

    except Exception as e:
        print(f"Error occurred while reading the CSV file: {e}")
        return None


def choose_sales_data():
    print("\nSelect sales data to load:")
    print("1. Original dataset")
    print("2. Sample dataset (created from the original if needed)")

    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice == "1":
            return load_csv(ORIGINAL_CSV)
        if choice == "2":
            if SAMPLE_CSV.exists():
                return load_csv(SAMPLE_CSV)

            print("Creating a sample from the original dataset...")
            original_data = load_csv(ORIGINAL_CSV)
            if original_data is None:
                return None
            if original_data.empty:
                print("Cannot create a sample because the original dataset is empty.")
                return None

            sample_size = min(SAMPLE_MAX_ROWS, len(original_data))
            sample_data = original_data.sample(
                n=sample_size,
                random_state=42,
            )
            sample_data.to_csv(SAMPLE_CSV, index=False)
            print(
                f"Saved dataset with {sample_size} rows "
                f"to {SAMPLE_CSV.name}."
            )
            return sample_data
        print("Choose 1 or 2.")


pd.set_option('display.max_columns', None)
# Call load_csv to load the data into a dataframe
sales_data = choose_sales_data()
# fake_data = None

if sales_data is None:
    raise SystemExit("Could not load the selected sales dataset.")

# Check if the dataframe was loaded successfully
if sales_data is not None:
    # Checking for missing fields in the loaded data
    required_fields = ['order_number', 'employee_id', 'employee_name', 'job_title', 'sales_region', 'order_date', 
                       'order_type', 'customer_type', 'customer_name', 'customer_state', 'product_category', 'product_number', 
                       'produce_name', 'quantity', 'unit_price']
    missing_fields = []

    for field in required_fields:
        if field not in sales_data.columns:
            missing_fields.append(field)

    if missing_fields:
        print("Missing required fields:", ", ".join(missing_fields))
        print("Warning: Some dashboard analytics may not work.")

    # load_csv(fake) CHECKING WITH FAKE DATA
    # print(sales_data.head()) CHECKING FOR DATA LOADED SUCCESSFULLY


def show_data_summary(df):
    print("\n--- Sales Data Summary ---")

    count_fields = {
        "Total orders": "order_number",
        "Number of employees": "employee_id",
        "Number of unique customers": "customer_name",
    }
# STRING FIELD TYPES THAT ARE COUNTED
    for label, field in count_fields.items():
        if field in df.columns:
            values = df[field].dropna()
            print(f"{label}: {values[values != 0].nunique():,}")
        else:
            print(f"{label}: Unavailable")

    list_fields = {
        "Sales regions": "sales_region",
        "Product categories": "product_category",
        "Unique states": "customer_state",
    }
# VALUE FIELD TYPES THAT ARE LISTED
    for label, field in list_fields.items():
        if field in df.columns:
            values = df[field].dropna()
            names = sorted(values[values != 0].astype(str).unique())
            print(f"{label} ({len(names)}): {', '.join(names)}")
        else:
            print(f"{label}: Unavailable")

    if "order_date" in df.columns:
        # INTERPRETING DATES IN STRING FORMAT
        dates = pd.to_datetime(
            df["order_date"].astype("string"),
            format="mixed",
            dayfirst=True,
            errors="coerce",
        ).dropna()

        if not dates.empty:
            print(f"Order dates: {dates.min():%Y-%m-%d} to {dates.max():%Y-%m-%d}")
        else:
            print("Order dates: Unavailable")
    else:
        print("Order dates: Unavailable")
# INTEGER FIELD TYPES THAT CAN BE SUMMED
    if "quantity" in df.columns:
        quantities = pd.to_numeric(df["quantity"], errors="coerce").fillna(0)
        print(f"Total quantities sold: {quantities.sum():,}")
    else:
        print("Total quantities sold: Unavailable")

    if "quantity" in df.columns and "unit_price" in df.columns:
        prices = pd.to_numeric(df["unit_price"], errors="coerce").fillna(0)
        print(f"Total sales amount: ${(quantities * prices).sum():,.2f}")
    else:
        print("Total sales amount: Unavailable")

show_data_summary(sales_data)

# REQUIREMENT 2/3: INTERACTIVE DASHBOARD
sales_data['sales'] = sales_data['quantity'] * sales_data['unit_price']

def show_grouped(df, group_fields, value_fields, operation): # BASICALLY A PIVOT TABLE FUNCTION THAT ORGANIZES THE VARIABLE NAMES FOR READABILITY
    grouped_data = df.groupby(group_fields)[value_fields]
    result = grouped_data.agg(operation)
    print(result.to_string())

def show_first_rows(df): # MENU ITEM 1
    total_rows = len(df)

    if total_rows == 0:
        print("No sales data rows are available.")
        return

    print("\nEnter rows to display:")
    print(f"- Enter a number 1 to {total_rows}")
    print("- To see all rows, enter 'all'")
    print("- To skip preview, press Enter")

    while True:
        choice = input("\nYour choice: ").strip().lower()

        if choice == "":
            return

        if choice == "all":
            n = total_rows
            break

        try:
            n = int(choice)
        except ValueError:
            print(f"Enter a whole number from 1 to {total_rows}, or enter 'all'.")
            continue

        if 1 <= n <= total_rows:
            break

        print(f"Enter a number from 1 to {total_rows}.")

    with pd.option_context("display.max_rows", None):
        print(df.head(n))


def sales_by_region_and_order(df): # MENU ITEM 2
    print("\nTotal sales by region and order type")
    show_grouped(df, ['sales_region', "order_type"], ['sales'], "sum")

def average_sales(df): # MENU ITEM 3
    print("\nAverage sales by region")
    show_grouped(df, ['sales_region', 'customer_state', 'order_type'], ['sales'], "mean")

def sales_by_customer_and_order(df):  # MENU ITEM 4
    print("\nTotal sales by customer type and order type by state")
    show_grouped(df, ['customer_state', 'customer_type', 'order_type'], ['sales'], "sum")


def quantity_and_price_by_region(df): # MENU ITEM 5
    print("\nTotal sales quantity and price by region and product")
    show_grouped(df, ['sales_region', 'produce_name'], ['quantity', 'unit_price'], "sum")


def quantity_and_price_by_customer(df): # MENU ITEM 6
    print("\nTotal sales quantity and price by customer type")
    show_grouped(df, ['customer_type'], ['quantity', 'unit_price'], "sum")


def price_range_by_category(df): # MENU ITEM 7
    print("\nMaximum and minimum sales price by category")
    show_grouped(df, ['product_category'], ['unit_price'], ["max", "min"])

def unique_employees_by_region(df): # MENU ITEM 8
    print("\nNumber of unique employees by region")
    employees = df[df["employee_id"] != 0]
    counts = employees.groupby("sales_region")["employee_id"].nunique()
    counts = counts.reindex(df["sales_region"].unique(), fill_value=0)
    print(counts.rename("Unique employees").to_string())

# REQUIREMENT 4: CUSTOM PIVOT TABLE
def select_pivot_options(title, options, optional=False): #
    print(f"\n{title}")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    prompt = "Enter the number(s) of your choice(s), separated by commas"
    if optional:
        prompt += " (press Enter for no grouping)"

    while True:
        answer = input(prompt + ": ").strip()

        if optional and answer == "":
            return []

        try:
            choices = [int(part.strip()) for part in answer.split(",")]
        except ValueError:
            print("Enter whole numbers separated by commas.")
            continue

        if any(number < 1 or number > len(options) for number in choices):
            print(f"Choose numbers from 1 to {len(options)}.")
            continue

        selected = []
        for number in choices:
            option = options[number - 1]
            if option not in selected:
                selected.append(option)

        return selected


def custom_pivot_table(df):
    rows = select_pivot_options(
        "Select rows:",
        ["employee_name", "sales_region", "product_category"],
    )

    columns = select_pivot_options(
        "Select columns (optional):",
        ["order_type", "customer_type"],
        optional=True,
    )

    values = select_pivot_options(
        "Select values:",
        ["quantity", "sales"],
    )

    operations = select_pivot_options(
        "Select aggregation function:",
        ["sum", "mean", "count"],
    )

    pivot_table = df.pivot_table(
        index=rows,
        columns=columns or None,
        values=values,
        aggfunc=operations,
        fill_value=0,
    )

    print("\n--- Custom Pivot Table ---")
    print(pivot_table.to_string())


def exit_dashboard(df):
    print("Exiting the Sales Data Dashboard.")
    return False


MENU = ( # TUPLE OF MENU OPTIONS WITH LABELS AND CORRESPONDING FUNCTIONS
    ("Show the first n rows of sales data", show_first_rows),
    ("Total sales by region and order type", sales_by_region_and_order),
    ("Average sales by region and by state and sale type", average_sales),
    ("Sales by customer type and order type by state", sales_by_customer_and_order),
    ("Total sales quantity and price by region and product", quantity_and_price_by_region),
    ("Total sales quantity and price by customer type", quantity_and_price_by_customer),
    ("Maximum and minimum sales price by category", price_range_by_category),
    ("Number of unique employees by region", unique_employees_by_region),
    ("Create a custom pivot table", custom_pivot_table),
    ("Exit", exit_dashboard),
)


def run_dashboard(df):
    while True:
        print("\n--- Sales Data Dashboard ---")

        for number, (label, function) in enumerate(MENU, start=1): # STARTS LIST OF NUMBERS AT 1 INSTEAD OF 0
            print(f"{number}. {label}")

        try:
            choice = int(input("\nChoose a menu option: "))
        except ValueError:
            print("Enter a menu option number.")
            continue

        if not 1 <= choice <= len(MENU):
            print(f"Enter a number from 1 to {len(MENU)}.")
            continue

        label, function = MENU[choice - 1]

        if function(df) is False:
            break

run_dashboard(sales_data)