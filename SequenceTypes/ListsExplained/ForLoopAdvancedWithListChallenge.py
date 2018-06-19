menu = []
menu.append(['egg', 'meat', 'chicken'])
menu.append(['egg', 'meat', 'spam', 'chicken'])
menu.append(['egg', 'chicken'])
menu.append(['egg', 'meat', 'chicken', 'spam'])
menu.append(['meat', 'chicken'])
menu.append(['spam', 'egg', 'meat', 'chicken'])
menu.append(['egg', 'meat'])
menu.append(['egg', 'spam', 'meat', 'chicken'])

for meals in menu:
    if not 'spam' in meals:
        for meal in meals:
            print(meal, end='|')
        print()
