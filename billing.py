def calculate_invoice(subtotal: float, discount: float = 0.10) -> float:
    """Calculates final invoice amount after applying discount."""
    return subtotal * (1 - discount)