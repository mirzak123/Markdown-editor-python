def plain():
    text = input("Text: ")
    return text


def bold():
    text = input("Text: ")
    return f"**{text}**"


def italic():
    text = input("Text: ")
    return f"*{text}*"


def header():
    level = int(input("Level: "))
    while level not in range(1, 7):
        print("The level should be within the range of 1 to 6.")
        level = int(input("Level: "))

    text = input("Text: ")
    return f"{'#' * level} {text}\n"


def link():
    label = input("Label: ")
    url = input("URL: ")
    return f"[{label}]({url})"


def inline_code():
    text = input("Text: ")
    return f"`{text}`"


def new_line():
    return '\n'


def ordered_list():
    rows = int(input("Number of rows: "))
    while rows < 1:
        print("The number of rows should be greater than zero")
        rows = int(input("Number of rows: "))
    text = ''

    for i in range(1, rows + 1):
        line = input(f'Row #{i}: ')
        text = text + f'{i}. {line}\n'
    return text


def unordered_list():
    rows = int(input("Number of rows: "))
    while rows < 1:
        print("The number of rows should be greater than zero")
        rows = int(input("Number of rows: "))
    text = ''

    for i in range(1, rows + 1):
        line = input(f'Row #{i}: ')
        text = text + f'* {line}\n'
    return text


def write_to_file(text):
    with open('output.md', 'w') as markdown_file:
        markdown_file.write(text)


def main():
    complete_text = ''
    available_formatters = {'plain': plain, 'bold': bold, 'italic': italic, 'header': header, 'link': link,
                            'inline-code': inline_code, 'new-line': new_line, 'ordered-list': ordered_list,
                            'unordered-list': unordered_list}
    while True:
        formatter = input("Choose a formatter: ")
        if formatter == '!help':
            print("Available formatters:", ' '.join(available_formatters.keys()))
            print("Special commands: !help !done")
            continue
        elif formatter == '!done':
            write_to_file(complete_text)
            quit()
        elif formatter not in available_formatters:
            print("Unknown formatting type or command")
            continue
        complete_text += available_formatters[formatter]()
        print(complete_text)


if __name__ == "__main__":
    main()
