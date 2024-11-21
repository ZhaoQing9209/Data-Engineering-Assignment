import requests

S = requests.Session()
URL = "https://b.cari.com.my/forum.php?mod=viewthread&tid=5379190"
PARAMS = {
    "title": "Rugi RM789 juta",
    "content": "[TERKINI] Petronas Chemicals Group catat kerugian bersih RM789 juta pada suku ketiga 2024 berbanding keuntungan bersih RM424 juta direkodkan tahun lepas."
}

R = S.get(url=URL, params=PARAMS)


# Print only title and content
print(PARAMS["title"])
print(PARAMS["content"])
