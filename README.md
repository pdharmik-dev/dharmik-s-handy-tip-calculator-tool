# 💰 Tip Calculator

A clean, command-line tip calculator written in Python. Instantly calculate tips and split bills between any number of people.

## Features

- ✅ Calculate tip for any bill amount and percentage
- ✅ Split the bill between multiple people
- ✅ Input validation with helpful error messages
- ✅ Clean, formatted output
- ✅ Unit tested with pytest

## Demo

```
====================================
        WELCOME TO TIP CALC
====================================

Enter bill amount ($): 85.00
Enter tip percentage (%): 20
Number of people splitting (1 = just you): 4

========================================
         TIP CALCULATOR RESULTS
========================================
  Bill Amount:      $85.00
  Tip (20%):        $17.00
  Total:            $102.00
----------------------------------------
  Split 4 ways:
  Tip per person:   $4.25
  Total per person: $25.50
========================================
```

## Getting Started

### Prerequisites

- Python 3.7+

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/tip-calculator.git
   cd tip-calculator
   ```

2. (Optional) Install dependencies for running tests:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

Run the calculator:
```bash
python tip_calculator.py
```

### Running Tests

```bash
python -m pytest test_tip_calculator.py -v
```

## Project Structure

```
tip-calculator/
├── tip_calculator.py      # Main calculator logic
├── test_tip_calculator.py # Unit tests
├── requirements.txt       # Dependencies
└── README.md
```

## How It Works

The core logic lives in `calculate_tip()`, which takes:
- `bill_amount` — the pre-tip bill total
- `tip_percent` — the tip as a percentage (e.g. `18` for 18%)
- `num_people` — how many people are splitting the bill (default: 1)

It returns a dictionary with the tip amount, total, and per-person breakdowns.

## License

MIT License — feel free to use and modify.
