

def normalize_country(code: str) -> str|None:
    clean_code = code.strip().upper()
    if len(clean_code) != 2:
        raise ValueError
    return clean_code if clean_code in {"US", "IN", "DE"} else None