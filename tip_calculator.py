"""
Tip Calculator
A simple command-line and GUI tip calculator that splits bills easily.
"""


def calculate_tip(bill_amount: float, tip_percent: float, num_people: int = 1) -> dict:
    """
    Calculate tip and total for a given bill.

    Args:
        bill_amount: The original bill amount in dollars
        tip_percent: The tip percentage (e.g., 15 for 15%)
        num_people: Number of people splitting the bill

    Returns:
        Dictionary with tip amount, total, and per-person amounts
    """
    if bill_amount < 0:
        raise ValueError("Bill amount cannot be negative.")
    if tip_percent < 0:
        raise ValueError("Tip percentage cannot be negative.")
    if num_people < 1:
        raise ValueError("Number of people must be at least 1.")

    tip_amount = bill_amount * (tip_percent / 100)
    total = bill_amount + tip_amount
    per_person = total / num_people
    tip_per_person = tip_amount / num_people

    return {
        "bill_amount": round(bill_amount, 2),
        "tip_percent": tip_percent,
        "tip_amount": round(tip_amount, 2),
        "total": round(total, 2),
        "num_people": num_people,
        "per_person_total": round(per_person, 2),
        "per_person_tip": round(tip_per_person, 2),
    }


def display_results(results: dict) -> None:
    """Print formatted results to the console."""
    print("\n" + "=" * 40)
    print("         TIP CALCULATOR RESULTS")
    print("=" * 40)
    print(f"  Bill Amount:      ${results['bill_amount']:.2f}")
    print(f"  Tip ({results['tip_percent']}%):         ${results['tip_amount']:.2f}")
    print(f"  Total:            ${results['total']:.2f}")
    print("-" * 40)
    if results["num_people"] > 1:
        print(f"  Split {results['num_people']} ways:")
        print(f"  Tip per person:   ${results['per_person_tip']:.2f}")
        print(f"  Total per person: ${results['per_person_total']:.2f}")
    print("=" * 40 + "\n")


def get_float_input(prompt: str) -> float:
    """Prompt user for a float value with validation."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("  Please enter a valid number.")


def get_int_input(prompt: str) -> int:
    """Prompt user for an integer value with validation."""
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("  Please enter a valid whole number.")


def main():
    print("\n====================================")
    print("        WELCOME TO TIP CALC")
    print("====================================\n")

    while True:
        try:
            bill = get_float_input("Enter bill amount ($): ")
            tip = get_float_input("Enter tip percentage (%): ")
            people = get_int_input("Number of people splitting (1 = just you): ")

            results = calculate_tip(bill, tip, people)
            display_results(results)

        except ValueError as e:
            print(f"\n  Error: {e}\n")

        again = input("Calculate another? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for using Tip Calc! 👋\n")
            break


if __name__ == "__main__":
    main()
