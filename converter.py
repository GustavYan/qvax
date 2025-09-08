import requests

def get_exchange_rate(base_currency: str, target_currency: str) -> float:
    """
    Получает курс обмена между двумя валютами через API.
    """
    url = f"https://api.exchangerate.host/latest?base={base_currency}&symbols={target_currency}"
    response = requests.get(url)
    data = response.json()
    
    if "rates" in data and target_currency in data["rates"]:
        return data["rates"][target_currency]
    else:
        raise ValueError("Не удалось получить курс валют.")


def convert_currency(amount: float, base_currency: str, target_currency: str) -> float:
    """
    Конвертирует сумму из одной валюты в другую.
    """
    rate = get_exchange_rate(base_currency, target_currency)
    return amount * rate


if __name__ == "__main__":
    # Ввод данных
    amount = float(input("Введите сумму: "))
    base_currency = input("Из какой валюты (например, USD): ").upper()
    target_currency = input("В какую валюту (например, EUR): ").upper()

    try:
        result = convert_currency(amount, base_currency, target_currency)
        print(f"{amount} {base_currency} = {result:.2f} {target_currency}")
    except Exception as e:
        print("Ошибка:", e)
