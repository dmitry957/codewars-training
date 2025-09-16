from datetime import datetime
import re

class Mongo:
    @staticmethod
    def is_valid(s) -> bool:
        if not isinstance(s, str):
            return False
        return bool(re.fullmatch(r'[0-9a-f]{24}$', s))
    
    @staticmethod
    def get_timestamp(s) -> datetime | bool:
        if not Mongo.is_valid(s):
            return False
        ts = int(s[:8], 16)
        return datetime.fromtimestamp(ts)