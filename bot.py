import requests
import datetime
import json

dni = "70778615"
codigo = "2021101370I"

url = "https://comensales.uncp.edu.pe/api/registros"

# El payload real en JSON
payload_json = {
    "t1_id": None,
    "t1_dni": dni,
    "t1_codigo": codigo,
    "t1_nombres": "",
    "t1_escuela": "",
    "t1_estado": None,
    "t3_periodos_t3_id": None
}

# Lo metemos como campo "data" en form-data
files = {
    "data": (None, json.dumps(payload_json))
}

headers = {
    "Origin": "https://comedor.uncp.edu.pe",
    "Referer": "https://comedor.uncp.edu.pe/",
    "User-Agent": "Mozilla/5.0"
}

response = requests.post(url, files=files, headers=headers)

print(f"📩 Código HTTP: {response.status_code}")
print(f"📄 Respuesta: {response.text}")

with open("registro_log.txt", "a", encoding="utf-8") as f:
    f.write(f"[{datetime.datetime.now()}] {response.status_code} - {response.text}\n")
