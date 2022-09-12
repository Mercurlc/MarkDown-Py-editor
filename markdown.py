UserTxt = ""

def header():
    while True:
        level = int(input("Level:"))
        if 0 < level < 7:
            text = input("Text:")
            return f"{'#' * level} {text}\n"
        else:
            print("The level should be within the range of 1 to 6")


def bold():
    text = input("Text:")
    return f"**{text}**"


def italic():
    text = input("Text:")
    return "*" + text + "*"


def plain():
     text = input("Text:")
     return text


def new_line():
    return "\n"


def link():
    Label = input("Label:")
    Url = input("URL:")
    return f"[{Label}]({Url})"


def inline_code():
    text = input("Text:")
    return f'`{text}`'


def unordered_list():
    while True:
        rows_num = int(input("Number of rows:"))
        if rows_num > 0:
            txt = ["*" + input(f"Row #{i}: ") for i in range(1, rows_num + 1)]
            text = "\n".join(txt)+"\n"
            return text
        else:
            print("The number of rows should be greater than zero")


def ordered_list():
    while True:
        rows_num = int(input("Number of rows:"))
        if rows_num > 0:
            txt = [str(i)+". "+input(f"Row #{i}: ") for i in range(1, rows_num + 1)]
            text = "\n".join(txt)+"\n"
            return text
        else:
            print("The number of rows should be greater than zero")

def txt_file(text):
    f = open('output.md', 'w+')
    f.write(text)
    f.close()

formatters = {'plain': plain, 'bold': bold, 'italic': italic, 'inline-code': inline_code, 'link': link, 'header': header, 'new-line': new_line, 'unordered-list':unordered_list, 'ordered-list':ordered_list}
start = True
while start:
    format = input("Choose a formatter:")
    if format in formatters:
        UserTxt += formatters[format]()
        txt_file(UserTxt)
        print(UserTxt)
    elif format == "!Help":
        print('Available formatters: plain bold italic header link inline-code new-line\n' \
            'Special commands: !help !done')
    elif format == "!done":
        break
    else:
        print('Unknown formatting type or command')
