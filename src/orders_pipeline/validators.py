import math

def normalize_country(code: str|None) -> str|None:
    if not code:
        return None
    clean_code = code.strip().upper()
    if clean_code == "":
        return None
    if len(clean_code) != 2 or not clean_code.isalpha():
        raise ValueError(f"Invalid country_code {code}")
    return clean_code 


def is_valid_amount(value)->bool:
    try:
        val = float(value)
    except (ValueError, TypeError):
        return False
    else:
        return val >= 0 and math.isfinite(val)
    

def normalize_status(s)->str:
    if not isinstance(s, str):
        raise ValueError(f"Invalid status: {s!r}")
    status = s.strip().upper()
    valid = {"PLACED", "SHIPPED", "COMPLETED", "CANCELLED"}
    if status in valid:
        return status
    raise ValueError(f"Invalid status: {s!r}")
    
    


