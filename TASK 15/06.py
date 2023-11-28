def print_document(pages):
    podkup = False
    for i in pages:
        if "Секретно" in i:
            podkup = True
            print('Дальнейшие материалы засекречены')
            break
        else:
            print(i)
    if not podkup:
        print('Напечатано без купюр')

print_document(["Обычная страница", "И еще страница", "Секретно Вот этот вот текст не показывать", "Никому", "Никогда"])
print()
print_document(["Пустой трёп", "который", "никому не интересен"])