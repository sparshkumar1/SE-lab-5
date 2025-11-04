"""
Inventory Management System

This module provides functions to manage inventory stock data including
adding items, removing items, checking quantities, and persisting data to JSON.
"""

import json
from datetime import datetime


# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to the inventory or update its quantity.

    Args:
        item: Name of the item to add
        qty: Quantity to add (must be non-negative)
        logs: List to append log messages to

    Returns:
        bool: True if successful, False otherwise
    """
    if logs is None:
        logs = []

    # Input validation
    if not item or not isinstance(item, str):
        print("Error: Item must be a non-empty string")
        return False

    if not isinstance(qty, int) or qty < 0:
        print("Error: Quantity must be a non-negative integer")
        return False

    stock_data[item] = stock_data.get(item, 0) + qty
    log_message = f"{datetime.now()}: Added {qty} of {item}"
    logs.append(log_message)
    return True


def remove_item(item, qty):
    """
    Remove a specified quantity of an item from inventory.

    Args:
        item: Name of the item to remove
        qty: Quantity to remove

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        if item not in stock_data:
            raise KeyError(f"Item '{item}' not found in inventory")

        if not isinstance(qty, int) or qty < 0:
            raise ValueError("Quantity must be a non-negative integer")

        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
        return True
    except (KeyError, ValueError) as e:
        print(f"Error removing item: {e}")
        return False


def get_qty(item):
    """
    Get the current quantity of an item.

    Args:
        item: Name of the item

    Returns:
        int: Quantity of the item, or 0 if not found
    """
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file: Path to the JSON file

    Returns:
        bool: True if successful, False otherwise
    """
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        return True
    except FileNotFoundError:
        print(f"Warning: File '{file}' not found. "
              f"Starting with empty inventory.")
        stock_data = {}
        return False
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{file}': {e}")
        return False


def save_data(file="inventory.json"):
    """
    Save inventory data to a JSON file.

    Args:
        file: Path to the JSON file

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=2)
        return True
    except IOError as e:
        print(f"Error saving data: {e}")
        return False


def print_data():
    """
    Print a formatted report of all items in inventory.
    """
    print("Items Report")
    print("-" * 30)
    if not stock_data:
        print("No items in inventory")
    else:
        for item, quantity in stock_data.items():
            print(f"{item} -> {quantity}")
    print("-" * 30)


def check_low_items(threshold=5):
    """
    Check for items that are below a specified threshold.

    Args:
        threshold: Minimum quantity threshold (default: 5)

    Returns:
        list: List of items below the threshold
    """
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """
    Main function to demonstrate inventory system functionality.
    """
    # Test adding items with validation
    add_item("apple", 10)
    add_item("banana", -2)  # Will be rejected - negative qty
    add_item(123, "ten")  # Will be rejected - wrong types

    # Test removing items
    remove_item("apple", 3)
    remove_item("orange", 1)  # Will print error - doesn't exist

    # Check quantities
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")

    # Save and load data
    save_data()
    load_data()

    # Print final report
    print_data()

    # Removed dangerous eval() function
    print("System demonstration completed successfully")


if __name__ == "__main__":
    main()
# End of inventory.py
