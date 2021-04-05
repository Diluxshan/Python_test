#Sample code for Save the file in excel
import itertools
import pandas as pd


with open(SHT_on_Stream.txt) as data:
    lines = [
        [
            i.split(":")[-1].replace("°C", "").replace("%RH", "")
            for i in line.strip().split()
            if i.startswith(("T1", "T2", "H1", "H2"))
        ] for line in data.readlines() if line.strip()
    ]
    flat = list(itertools.chain.from_iterable(lines))
    df = pd.DataFrame(
        [flat[i:i+4] for i in range(0, len(flat), 4)],
        columns=["T1", "H1", "T2", "H2"],
    )
    print(df)
    df.to_excel("your_table.xlsx", index=False)