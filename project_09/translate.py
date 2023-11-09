import googletrans  # pip install googletrans==4.0.0-rc1

translator = googletrans.Translator()
lang = googletrans.LANGUAGES
print(lang)
str1 = "행복하세요"
res1 = translator.translate(str1, dest="en", src="ko")
print(f"행복하세요 => {res1.text}")

str2 = "I am happy"
res2 = translator.translate(str2, dest="ko", src="en")
print(f"I am happy => {res2.text}")

org_path = r"text.txt"
translated_path = r"translated.txt"
with open(org_path, "r") as f:
    lines = f.readlines()

r = ""
for l in lines:
    res = translator.translate(l, dest="ko")
    r += f"{res.text}\n"
    print(res.text)
    # If you want to append a single line when it reads a line, then use the below 2 lines
    # Otherwise you want to write whole lines with a single time for every execution of the file,
    # leave them alone.

    # with open(save_path, "a", encoding="utf-8") as f:
    # f.write(res.text + "\n")
with open(translated_path, "w", encoding="utf-8") as f:
    f.write(r + "\n")
