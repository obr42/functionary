from rich.console import Console
from rich.table import Table


def format_results(results, title=""):
    """
    Helper function to organize table results using Rich

    Args:
        results: Results to format as a List
        title: Optional table title as a String

    Returns:
        None
    """
    table = Table(title=title)
    console = Console()
    first_row = True
    EXCLUDED_FIELDS = ["environment"]

    for item in results:
        row_data = []
        for key, value in item.items():
            if key in EXCLUDED_FIELDS:
                continue
            if first_row:
                table.add_column(key.capitalize())
            row_data.append(str(value) if value else None)
        table.add_row(*row_data)
        first_row = False
    console.print(table)