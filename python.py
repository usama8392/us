import pytest

def calculate_shipping_cost(weight, distance, promo_applied=False):
    """Calculates shipping cost based on weight, distance, and promo (optional)."""
    base_cost = 5  # Replace with your base cost calculation
    distance_cost = 0.25 * distance  # Replace with your distance-based cost calculation
    total_cost = base_cost + distance_cost
    if promo_applied:
        total_cost *= 0.9  # Apply 10% discount if promo code is used
    return total_cost

# Test cases with different weight, distance, and promo code values:
@pytest.mark.parametrize("weight, distance, promo_applied, expected_cost", [
    (2, 100, False, 30),  # Lightweight, longer distance, no promo
    (5, 50, True, 11.25),  # Heavier, shorter distance, promo applied
    (10, 200, False, 55),  # Heaviest, longest distance, no promo
])
def test_calculate_shipping_cost(weight, distance, promo_applied, expected_cost):
    """Tests shipping cost calculation for various scenarios."""
    actual_cost = calculate_shipping_cost(weight, distance, promo_applied)
    assert actual_cost == expected_cost
