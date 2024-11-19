original = open("", 'r', encoding="utf8")
lines = original.readlines()
output = open("", 'w', encoding="utf8")
specials = {}
with open("HTML special characters.txt", 'r', encoding="utf8") as f:
    for line in f:
        line = line.replace("=", "")
        (key, val) = line.rstrip("\n").split()
        specials[key] = val

for line in lines:
    number_part, text_part = line.split('\t')
    words = text_part.split()
    for i in range(len(words)):
        for key in specials:
            if key in words[i]:
                words[i] = words[i].replace(key, specials[key])
    updated_text_part = ' '.join(words)
    updated_line = f"{number_part}\t{updated_text_part}"
    output.write(updated_line + '\n')
    


