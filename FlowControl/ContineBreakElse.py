items = ["football", "cricket", "basketball", "hockey", "table tennis", "lawn tennis"]

for item in items:
    if item == 'hockey':
        continue
    print(item)

# football
# cricket
# basketball
# table tennis
# lawn tennis

for item in items:
    if item == 'hockey':
        break
    print(item)

# football
# cricket
# basketball

print('============')
nast_game = ''
for item in items:
    if item == 'hockey':
        nast_game = item
        break
else:
    print(item)

if nast_game:
    print("Its a nasty game")
else:
    print("its not a nasty game")

# Its a nasty game