import os
import requests

pat = os.environ.get("TREASURE_PAT")
url = "https://raw.githubusercontent.com/iyad-obeid/secret-message/main/treasure.txt"

response = requests.get(url, headers={"Authorization": f"Bearer {pat}"})
print(response.text)