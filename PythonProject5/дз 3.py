import requests

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
response_text = response.text

res_parse_list = []
response_parse = response_text.split("<td>")
for parse_elem_1 in response_parse:
    if parse_elem_1.startswith("USD"):
        for parse_elem_2 in parse_elem_1.split("</td>"):
            if parse_elem_2.replace('.', '', 1).isdigit():
                res_parse_list.append(parse_elem_2)

if res_parse_list:
    usd_exchange_rate = res_parse_list[0]
    print(f"Курс долара США (USD) - {usd_exchange_rate} UAH")
else:
    print("Не вдалося отримати курс долара США.")