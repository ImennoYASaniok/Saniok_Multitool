from decouple import config

TYPE_TOKEN = 'EXTRA_TOKEN' # TOKEN
TOKEN = config(TYPE_TOKEN)
ADMINS = list(map(int, config('ADMINS').split(',')))

def get_readme_text():
    with open("README.md", "r", encoding="utf-8") as readme:
        info_text = readme.read().strip()

    info_text = info_text.replace("---\n", "")

    info_text = info_text.split("\n")
    info_text = list(map(lambda s: "<i>"+" ".join(s.split()[1:]).strip()+"</i>" if len(s.split()) > 0 and s.split()[0] == "#"*len(s.split()[0]) else s, info_text))
    info_text = list(map(lambda s: " ".join(list(map(lambda w: w.split("[")[0] + f'<a href="{w[w.index("(")+1:w.index(")")].strip()}">'+w[w.index("[")+1:w.index("]")].strip()+"</a>" + w.split(")")[1] if len(s.split()) > 0 and "".join(list(filter(lambda x: x in "[]()", w))) == "[]()" else w, s.split()))), info_text))
    info_text = "\n".join(info_text)

    type_tag = 0
    while info_text.find("**") != -1:
        info_text = info_text.replace("**", "<b>" if type_tag == 0 else "</b>", 1)
        type_tag = not type_tag

    contacts_text = "сбой в программе, контакты не определись :(.\nАдмин уже всё чинит"
    info_text_readlines = info_text.split("\n")
    for i in range(len(info_text_readlines)):
        if "Ссылки и контакты" in info_text_readlines[i]:
            contacts_text = "\n".join(info_text_readlines[i:])
            break

    return info_text, contacts_text
MESSAGE_INFO, MESSAGE_CONTACTS = get_readme_text()