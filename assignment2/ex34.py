import pandas as pd


def display_initial_rows(data: pd.DataFrame) -> None:
    while True:
        available_rows = len(data)
        print(f"\nEnter rows to display (1 to {available_rows})")
        print("To see all rows, enter 'all'")
        print("To skip preview, press Enter")
        selection = input("Your choice: ").strip()

        if not selection:
            return

        if selection.lower() == "all":
            print(data)
            return

        if not selection.isdecimal():
            print(f"Invalid input. Enter a number from 1 to {available_rows}, 'all', or press Enter.")
            continue

        row_count = int(selection)
        if not 1 <= row_count <= available_rows:
            print(f"Invalid input. Enter a number from 1 to {available_rows}, 'all', or press Enter.")
            continue

        print(data.head(row_count))
        return


def _data_with_sales(data: pd.DataFrame) -> pd.DataFrame | None:
    columns = {
        str(column).strip().casefold().replace("_", " "): column
        for column in data.columns
    }
    if "sales" in columns:
        return data

    quantity_column = columns.get("quantity")
    unit_price_column = columns.get("unit price")
    if quantity_column is None or unit_price_column is None:
        print("Cannot analyze sales: the data must include Sales or both Quantity and Unit Price columns.")
        return None

    sales_data = data.copy()
    sales_data["sales"] = data[quantity_column] * data[unit_price_column]
    return sales_data


def total_sales_by_region_and_order_type(data: pd.DataFrame) -> None:
    sales_data = _data_with_sales(data)
    if sales_data is None:
        return

    columns = {
        str(column).strip().casefold().replace("_", " "): column
        for column in sales_data.columns
    }
    region_column = columns.get("sales region") or columns.get("region")
    order_type_column = columns.get("order type")
    sales_column = columns["sales"] if "sales" in columns else None
    if region_column is None or order_type_column is None or sales_column is None:
        print("Cannot create the pivot table: the data must include Region, Order Type, and Sales.")
        return

    pivot_table = pd.pivot_table(
        sales_data,
        index=region_column,
        columns=order_type_column,
        values=sales_column,
        aggfunc="sum",
        fill_value=0,
    )
    print(pivot_table)


def average_sales_by_region_state_and_order_type(data: pd.DataFrame) -> None:
    sales_data = _data_with_sales(data)
    if sales_data is None:
        return

    columns = {
        str(column).strip().casefold().replace("_", " "): column
        for column in sales_data.columns
    }
    region_column = columns.get("sales region") or columns.get("region")
    state_column = columns.get("customer state") or columns.get("state")
    order_type_column = columns.get("order type")
    sales_column = columns["sales"] if "sales" in columns else None
    if (
        region_column is None
        or state_column is None
        or order_type_column is None
        or sales_column is None
    ):
        print(
            "Cannot create the pivot table: the data must include Region, State, "
            "Order Type, and Sales."
        )
        return

    pivot_table = pd.pivot_table(
        sales_data,
        index=region_column,
        columns=[state_column, order_type_column],
        values=sales_column,
        aggfunc="mean",
    )
    print(pivot_table)


def show_employees_by_region(data: pd.DataFrame) -> None:
    columns = {
        str(column).strip().casefold().replace("_", " "): column
        for column in data.columns
    }
    region_column = next(
        (columns[name] for name in ("region", "sales region") if name in columns),
        None,
    )
    employee_column = next(
        (
            columns[name]
            for name in ("employee", "employees", "employee name", "salesperson", "sales representative", "rep")
            if name in columns
        ),
        None,
    )

    if region_column is None or employee_column is None:
        print(
            "Cannot count employees by region: the data must include a Region column "
            "and an Employee, Employee Name, Salesperson, Sales Representative, or Rep column."
        )
        return

    counts = data.groupby(region_column)[employee_column].nunique().sort_index()
    print(counts.to_string())


def exit_program(data: pd.DataFrame) -> None:
    print("Exiting the program.")


def get_user_selection(options: list, prompt: str) -> list:
    while True:
        print(prompt)
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")

        choice = input("Enter the number(s) of your choice(s), separated by commas: ").strip()
        if not choice:
            return []

        try:
            indices = [int(item.strip()) for item in choice.split(",")]
        except ValueError:
            print("Invalid selection. Enter menu numbers separated by commas.")
            continue

        if any(index < 1 or index > len(options) for index in indices):
            print(f"Invalid selection. Choose numbers between 1 and {len(options)}.")
            continue

        return [options[index - 1] for index in dict.fromkeys(indices)]


def generate_custom_pivot_table(data: pd.DataFrame) -> None:
    row_options = list(data.columns)
    if not row_options:
        print("Cannot create a pivot table because the data has no columns.")
        return

    while True:
        rows = get_user_selection(row_options, "Select rows (required):")
        if rows:
            break
        print("Select at least one row dimension.")

    col_options = row_options
    col_options = [col for col in col_options if col not in rows]
    cols = get_user_selection(col_options, "Select columns (optional):")

    value_options = list(data.select_dtypes(include=["number"]).columns)
    if not value_options:
        print("Cannot create a pivot table because the data has no numeric columns.")
        return

    while True:
        values = get_user_selection(value_options, "Select values to aggregate (required):")
        if values:
            break
        print("Select at least one numeric value.")

    agg_options = ["sum", "mean", "count"]
    while True:
        agg_func = get_user_selection(agg_options, "Select aggregation function(s) (required):")
        if agg_func:
            break
        print("Select at least one aggregation function.")

    pivot_table = pd.pivot_table(
        data,
        index=rows,
        columns=cols if cols else None,
        values=values,
        aggfunc=agg_func,
    )
    print(pivot_table)


menu_options = (
    ("Show the first n rows of sales data", display_initial_rows),
    ("Show total sales by region and order type", total_sales_by_region_and_order_type),
    ("Show average sales by region, state, and order type", average_sales_by_region_state_and_order_type),
    ("Show the number of employees by region", show_employees_by_region),
    ("Generate a custom pivot table", generate_custom_pivot_table),
    ("Exit the program", exit_program),
)


def display_menu() -> int:
    """Show the menu and return a valid selection as an index menu_options"""
    while True:
        print("\nAvailable actions:")
        for index, (description, _) in enumerate(menu_options, start=1):
            print(f"{index}: {description}")

        choice = input(f"Enter the number of your choice (1-{len(menu_options)}): ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(menu_options):
            return int(choice) - 1
        print(f"Invalid choice. Please enter a number between 1 and {len(menu_options)}.")


def main() -> None:
    csv_file = "https://drive.google.com/uc?export=download&id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
    data = pd.read_csv(csv_file, engine="pyarrow", on_bad_lines="skip")

    while True:
        choice = display_menu()
        action = menu_options[choice][1]
        action(data)
        if action is exit_program:
            return

if __name__ == "__main__":
    main()