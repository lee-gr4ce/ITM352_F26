from io import StringIO

import requests as req
import pandas as pd

url = "https://www.hicentral.com/hawaii-mortgage-rates.php"
response = req.get(url)
response.raise_for_status()
df = pd.read_html(StringIO(response.text))[0]
# print(df)

df = df[["Lender", "Term/Type", "Interest Rate", "% *APR"]]
df = df.set_index("Lender")
print(df.to_string())