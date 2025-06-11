from datetime import datetime
import pytz

IST = pytz.timezone('Asia/Kolkata')

def convert_utc_to_ist(utc_dt: datetime) -> datetime:
    return utc_dt.replace(tzinfo=pytz.utc).astimezone(IST)

def convert_ist_to_utc(ist_dt: datetime) -> datetime:
    return IST.localize(ist_dt).astimezone(pytz.utc)
