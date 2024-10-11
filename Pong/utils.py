def clamp(value, min_value, max_value):
    """Clamp the value between min_value and max_value."""
    return max(min_value, min(value, max_value))

def keep_within_bounds(rect, top_limit, bottom_limit):
    """Keep the item within the specified vertical bounds."""
    rect.top = clamp(rect.top, top_limit, bottom_limit)
    rect.bottom = clamp(rect.bottom, top_limit, bottom_limit)
