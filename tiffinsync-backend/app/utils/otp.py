import random
from datetime import datetime, timedelta

otp_store = {}  # temporary in-memory store {phone: {"otp": ..., "expires_at": ..., "verified": bool}}

def generate_mock_otp(phone: str) -> str:
    otp = str(random.randint(1000, 9999))
    otp_store[phone] = {
        "otp": otp,
        "expires_at": datetime.utcnow() + timedelta(minutes=5),
        "verified": False
    }
    print(f"Mock OTP for {phone}: {otp}")  # You may log this for debugging
    return otp

def verify_mock_otp(phone: str, otp: str = None, check_only: bool = False) -> bool:
    data = otp_store.get(phone)
    if not data:
        return False

    # Check expiry
    if datetime.utcnow() > data["expires_at"]:
        del otp_store[phone]
        return False

    # If just checking whether OTP was verified earlier
    if check_only:
        return data.get("verified", False)

    # Normal verification flow
    if data["otp"] != otp:
        return False

    # Mark as verified instead of deleting (so register can check later)
    data["verified"] = True
    return True