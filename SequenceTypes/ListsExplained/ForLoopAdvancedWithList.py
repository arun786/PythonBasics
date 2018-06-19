menu = []
menu.append(['egg', 'meat', 'chicken'])
menu.append(['egg', 'meat', 'spam', 'chicken'])
menu.append(['egg', 'chicken'])
menu.append(['egg', 'meat', 'chicken', 'spam'])
menu.append(['meat', 'chicken'])
menu.append(['spam', 'egg', 'meat', 'chicken'])
menu.append(['egg', 'meat'])
menu.append(['egg', 'spam', 'meat', 'chicken'])

for meal in menu:
    if not 'spam' in meal:
        print(meal)

        # o/p will be
        # ['egg', 'meat', 'chicken']
        # ['egg', 'chicken']
        # ['meat', 'chicken']
        # ['egg', 'meat']
