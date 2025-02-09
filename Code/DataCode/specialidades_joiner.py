import pandas as pd


table = pd.read_csv("Data/CSV/doc_in_dist_enspec.csv")
df = pd.DataFrame(table)



def changespecs(a):
    enval = a["FACH_en"]
    if "Internal medicine" in enval:
        val = "Internal Medicine"
    else:
        if "Children" in enval:
            val = "Child and youth healing"
        else:
            if "Allgemeine" in enval:
                val = "General surgery"
            else:
                if "Radiology" in enval:
                    val = "Radiology"
                else:
                    if "Psychiatry" in enval:
                        val = "Psychiatry"
                    else:
                        if "Orthopedics" in enval:
                            val = "Orthopedics"
                        else:
                            if "Neuro" in enval:
                                val = "Neurology"
                            else:
                                val = enval
    return val

def countpopcov(x):
    y = 0
    return y



df2 = df
df2["FACH_en_2"] = df.apply(changespecs, axis=1)
print(len(df.index))
df3 = df2.groupby(["FACH_en_2"]).size()
df4 = df3[df3 > 100]
print(df4)
suma = 0
for row in df4:
    suma += row
print(suma)
# a = translator.translate("spring",dest="en").text
#df2.to_csv("../Data/CSV/doc_in_dist_enspec.csv",index=False)

