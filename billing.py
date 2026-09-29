from typing import Dict, Any

def calculate_invoice(
    subtotal: float,
    discount: float = 0.15,
    tax_rate: float = 0.034,
    currency: str = "USD"
) -> Dict[str, Any]:
    """Calculates comprehensive invoice breakdown with discount and sales tax.

    Args:
        subtotal: Gross charge before adjustments.
        discount: Discount percentage between 0.0 and 1.0 (default 0.15).
        tax_rate: Applied tax percentage (default 0.08).
        currency: ISO currency code (default USD).

    Raises:
        ValueError: If subtotal is negative or discount exceeds 1.0.
    """
    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")
    if not (0.0 <= discount <= 1.0):
        raise ValueError("Discount must be between 0.0 and 1.0")

    discount_amount = subtotal * discount
    taxable_amount = subtotal - discount_amount
    tax_amount = taxable_amount * tax_rate
    total = taxable_amount + tax_amount

    return {
        "currency": currency,
        "subtotal": round(subtotal, 2),
        "discount_applied": round(discount_amount, 2),
        "tax": round(tax_amount, 2),
        "total": round(total, 2)
    }