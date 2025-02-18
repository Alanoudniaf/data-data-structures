# pylint: disable=missing-docstring

RATES = {
    "USDEUR": 0.85,
    "GBPEUR": 1.13,
    "CHFEUR": 0.86,
    "EURGBP": 0.885,
    }

# First step
for key, value in RATES.items():
    print(key, value)

# Second step
# amount is a tuple, amount[0] is the value I have, amount[1] is the currency of the money I have
# Third step
for key, value in RATES.items():
    print(key[0:3])

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    for key, value in RATES.items():

        if amount[1] == key[0:3] and currency == "EUR":
            return round(value * amount[0])

        if  amount[1] == key[3:6] and currency == key[0:3]:
            return round(amount[0] / value)

    return None

print(convert((100, "GBP"), "EUR"))
