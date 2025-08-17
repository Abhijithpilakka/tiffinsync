import random
from datetime import datetime, timedelta

otp_store = {}  # temporary in-memory store {phone: {"otp": ..., "expires_at": ...}}

def generate_mock_otp(phone: str) -> str:
    otp = str(random.randint(1000, 9999))
    otp_store[phone] = {"otp": otp, "expires_at": datetime.utcnow() + timedelta(minutes=5)}
    print(f"Mock OTP for {phone}: {otp}")  # You may log this for debugging
    return otp

def verify_mock_otp(phone: str, otp: str) -> bool:
    data = otp_store.get(phone)
    if not data:
        return False
    if datetime.utcnow() > data["expires_at"]:
        del otp_store[phone]
        return False
    if data["otp"] != otp:
        return False
    del otp_store[phone]
    return True
