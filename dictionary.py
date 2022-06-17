import requests
import json

print("             English Dictionary")
lang_list = {1:"en-ru",2:"en-de",3:"en-fr",4:"en-es",5:"en-it",6:"en-tr"}

def lang_show(lang):
    for x, y in lang.items():
        print(f"{x}. {y}")

def lang_select(lang, select_one):
    for x, y in lang.items():
        if select_one == x:
            return y

lang_show(lang_list)
select_one = int(input("Select the languege: "))

selected_lang = lang_select(lang_list, select_one)
print(selected_lang)

response = requests.get(f"https://dictionary.yandex.net/api/v1/dicservice.json/lookup?", params={
    "key": "dict.1.1.20210912T100036Z.6cc31f04cd2e24f3.bfcae70a2579c824bf8d2563ebf0b24d6e752077",
    "lang": selected_lang,
    "text": input("Enter the word: ")
})

data = response.json()
translated_text = data["def"][0]["tr"][0]["text"]

print(translated_text)
