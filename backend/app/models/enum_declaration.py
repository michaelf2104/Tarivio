from enum import Enum

class TariffLevel(str, Enum):
    basic = "basic"
    comfort = "comfort"
    premium = "premium"


class ValueType(str, Enum):
    percent = "percent"
    numeric = "numeric"
    bool = "bool"
    text = "text"


