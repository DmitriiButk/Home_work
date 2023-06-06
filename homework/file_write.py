texts_files = ["1.txt", "2.txt", "3.txt"]
text_list = []
for text in texts_files:
    with open(text, encoding="utf-8") as file:
        res = file.readlines()
        res.insert(0, text)
        text_list.append(res)

with open("end_file.txt", "w", encoding="utf-8") as file:
    text_list.sort(key=len)
    for text in text_list:
        file.write(text[0])
        file.write("\n")
        file.write(str(len(text[1:])))
        file.write("\n")
        file.writelines(text[1:])
        file.write("\n")