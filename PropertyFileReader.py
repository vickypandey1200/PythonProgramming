from jproperties import Properties
p = Properties()
with open("sample.properties", "rb") as f:
    p.load(f, "utf-8")
print(p["name_1"])
