import requests
from datetime import datetime, timedelta


def cotar():
def cotar_dia(data):
url = (
"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
f"CotacaoDolarDia(dataCotacao=@dataCotacao)?@dataCotacao='{data}'"
"&$top=1&$format=json&$select=cotacaoCompra"
)
res = requests.get(url).json()
if res["value"]:
return res["value"][0]["cotacaoCompra"]
dia_anterior = datetime.strptime(data, "%m-%d-%Y") - timedelta(1)
dia_anterior = datetime.strftime(dia_anterior, "%m-%d-%Y")
return cotar_dia(dia_anterior)

hoje = datetime.today()
datas = [
datetime.strftime(hoje - timedelta(i), "%m-%d-%Y") for i in range(365)
]
return [cotar_dia(d) for d in datas]


if __name__ == "__main__":
print(cotar())
