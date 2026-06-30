from typing import Optional


def parse_cart_count(raw_text: Optional[str]) -> int:
    if not raw_text:
        return 0
    try:
        return int(str(raw_text).replace(",", "").strip())
    except ValueError:
        return 0
