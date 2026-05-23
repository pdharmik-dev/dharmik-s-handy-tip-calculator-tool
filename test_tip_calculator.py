"""
Unit tests for tip_calculator.py
Run with: python -m pytest test_tip_calculator.py -v
"""

import pytest
from tip_calculator import calculate_tip


class TestCalculateTip:
    def test_basic_tip_calculation(self):
        result = calculate_tip(100.00, 20)
        assert result["tip_amount"] == 20.00
        assert result["total"] == 120.00

    def test_15_percent_tip(self):
        result = calculate_tip(50.00, 15)
        assert result["tip_amount"] == 7.50
        assert result["total"] == 57.50

    def test_split_between_people(self):
        result = calculate_tip(100.00, 20, 4)
        assert result["per_person_total"] == 30.00
        assert result["per_person_tip"] == 5.00

    def test_single_person(self):
        result = calculate_tip(80.00, 18, 1)
        assert result["per_person_total"] == result["total"]

    def test_zero_tip(self):
        result = calculate_tip(50.00, 0)
        assert result["tip_amount"] == 0.00
        assert result["total"] == 50.00

    def test_zero_bill(self):
        result = calculate_tip(0.00, 20)
        assert result["tip_amount"] == 0.00
        assert result["total"] == 0.00

    def test_negative_bill_raises_error(self):
        with pytest.raises(ValueError):
            calculate_tip(-10.00, 20)

    def test_negative_tip_raises_error(self):
        with pytest.raises(ValueError):
            calculate_tip(50.00, -5)

    def test_zero_people_raises_error(self):
        with pytest.raises(ValueError):
            calculate_tip(50.00, 20, 0)

    def test_rounding(self):
        result = calculate_tip(33.33, 18)
        assert isinstance(result["tip_amount"], float)
        assert isinstance(result["total"], float)

    def test_large_party(self):
        result = calculate_tip(200.00, 20, 10)
        assert result["per_person_total"] == 24.00
        assert result["num_people"] == 10
