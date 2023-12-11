import json

# Dışarıdan metin listesini içeren dosyanın adı
input_file = "BADlist.txt"

# Dosyadan metinleri okuyun
with open(input_file, "r", encoding="utf-8") as file:
    text_list = file.read().splitlines()

# Boş bir sözlük oluşturun
data = {"c2dictionary": True, "data": {}}

# Metinleri sözlüğe ekleyin
for idx, text in enumerate(text_list):
    data["data"][str(idx)] = text

# JSON dosyasına yazın
output_file = "BADlist_Output.json"
with open(output_file, "w") as json_file:
    json.dump(data, json_file, ensure_ascii=False, indent=2)

print("JSON dosyası oluşturuldu: " + output_file)
