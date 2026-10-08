# Shopping Bill Generator

A menu-driven Python mini project that adds shopping items to a cart and prints a bill with an automatic discount. Prices are displayed in Indian rupees (INR).

## Features

- Add items with a name, quantity, and unit price.
- View the shopping cart and item totals.
- Calculate a subtotal and apply a discount.
- Generate a dated bill for ABC GENERAL STORE.
- Clear the cart after confirmation.
- Check for empty names, non-positive quantities/prices, and invalid numeric input.

## Requirements

- Python 3.6 or newer (Python 3.12 recommended).
- A terminal that supports the rupee symbol (₹).
- No third-party packages are required.

## Run the project

Download or clone this repository, open a terminal in its folder, and run:

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```

## Menu

```text
1. Add Item
2. View Cart
3. Generate Bill
4. Clear Cart
5. Exit
```

Choose an option and follow the prompts. For example, add 2 units of Rice at ₹300 each, then choose Generate Bill. The subtotal is ₹600, the discount is ₹30 (5%), and the grand total is ₹570.

## Discount rules

| Subtotal | Discount |
| --- | --- |
| Below ₹500 | 0% |
| ₹500 to below ₹1,000 | 5% |
| ₹1,000 or more | 10% |

## Python concepts used

Functions, lists, dictionaries, loops, conditional statements, exception handling, formatted strings, and the standard-library `datetime` module.

## Project files

```text
shopping-bill-generator/
├── main.py
├── README.md
└── .gitignore
```

## Notes

This is an educational command-line project. The cart is kept in memory and is lost when the program exits. Bills are displayed in the terminal; they are not saved to a file. Generating a bill does not clear the cart. The program uses floating-point numbers for prices.

## Upload to GitHub

1. Extract the ZIP file on your computer.
2. Open or create your GitHub repository.
3. Select **Add file → Upload files** (or **uploading an existing file** in an empty repository).
4. Upload the files inside `shopping-bill-generator`, including `.gitignore`.
5. Enter a commit message such as `Add Shopping Bill Generator mini project`, then select **Commit changes**.

Upload the extracted files so GitHub can display the Python source and README directly.
