import re
import sys


errors = []

with open("main.csv", "r", encoding="UTF-8") as f:
    lines = f.readlines()

lines = [l.rstrip() for l in lines]

if lines[0] != "orig,read,kind":
    errors.append((1, "ヘッダー業を編集してはいけません。"))

words = {}
pattern = re.compile(r"[a-zａ-ｚＡ-Ｚ]")
pattern = re.compile(r"[A-Zａ-ｚＡ-Ｚ]")

for i in range(len(lines)):
    if i == 0:
        continue
    if lines[i] == "":
        continue
    ls = lines[i].split(",")
    if len(ls) != 3:
        errors.append((i, "要素の数が合いません。"))
        continue
    if re.search(pattern, ls[0]):
        errors.append((i, "単語にアルファベットを使う場合は、半角の小文字にしてください。"))
        continue
    if ls[0] in words:
        errors.append((i, "同じ単語がすでに登録されています。"))
    words[ls[0]] = True


if len(errors) == 0:
    print("自動でチェックしました。特に問題なさそうです。")
    sys.exit(0)
# end no error
errors.sort(key=lambda x: x[0])
errors_display = "\n".join(["- %d行目: %s" % x for x in errors])
print("自動でチェックしました。以下を修正してください。\n\n%s" % errors_display)
sys.exit(1)
