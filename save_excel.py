#Sample code for Save the file in excel
import re

import pandas as pd

with open("SHT_on_Stream.txt") as data_file:
    data_list = re.findall(r"\d\d\.\d\d", data_file.read())

pd.DataFrame(
    [data_list[i:i + 4] for i in range(0, len(data_list), 4)],
    columns=["T1", "H1", "T2", "H2"],
).to_excel(
    "sht_on_stream.xlsx",
    index=False,
)