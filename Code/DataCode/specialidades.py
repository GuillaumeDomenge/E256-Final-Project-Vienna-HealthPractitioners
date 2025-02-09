import pandas as pd
from googletrans import Translator
translator = Translator()

table = pd.read_csv("../Data/CSV/doc_in_dist.csv")
df = pd.DataFrame(table)

subs = list(df["FACH"].unique())
subsen = []
dictsubs = {}
for word in subs:
    a = translator.translate(word, dest="en").text
    subsen.append(a)
    print(a)
    dictsubs[word] = a

def gettrans(a):
    return dictsubs[a["FACH"]]
df2 = df
df2["FACH_en"] = df.apply(gettrans, axis=1)
# a = translator.translate("spring",dest="en").text
df2.to_csv("../Data/CSV/doc_in_dist_enspec.csv",index=False)

