# pylint: disable=missing-docstring

RATES = {
    "USDEUR": 0.85,
    "GBPEUR": 1.13,
    "CHFEUR": 0.86,
    "EURGBP": 0.885,
}

def display_rates():
    for currency_pair in RATES:
        print(currency_pair, RATES[currency_pair])

def display_base_currencies():
    for currency_pair in RATES:
        print(currency_pair[:3])

def convert(amount, target_currency):
    original_amount, original_currency = amount

    for currency_pair, rate in RATES.items():
        base_currency, quote_currency = currency_pair[:3], currency_pair[3:]

        if original_currency == base_currency and target_currency == quote_currency:
            return round(original_amount * rate)

        if original_currency == quote_currency and target_currency == base_currency:
            return round(original_amount / rate)

    return None

display_rates()
display_base_currencies()
print(convert((100, "GBP"), "EUR"))
