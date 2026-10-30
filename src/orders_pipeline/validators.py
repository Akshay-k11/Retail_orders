

def normalize_country(code: str) -> str|None:
    if not code:
        return None
    clean_code = code.strip().upper()
    if clean_code == "":
        return None
    if len(clean_code) != 2:
        raise ValueError
    return clean_code if clean_code in {"US", "IN", "DE"} else None


def is_valid_amount(value)->bool:
    try:
        if not value or value == "inf":
            return False
        val = float(value)
    except ValueError or TypeError as e:
        return False
    else:
        return True if val >= 0 else False
    

def normalize_status(s)->str:
    status = s.strip().upper()
    valid = {"PLACED", "SHIPPED", "COMPLETED", "CANCELLED"}
    if status in valid:
        return status
    else:
        raise ValueError(f"Invalid status: {s}")
    


