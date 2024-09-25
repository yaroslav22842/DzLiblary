from colorama import init, Fore, Back, Style
init()


                          #Запусти код







print(Fore.MAGENTA + 'Colorama это плагин для того чтобы менять цвет и яркость текста в консоли.' + Style.RESET_ALL)
print(Fore.CYAN + Back.BLACK + 'Этот плагин используеться с Print. Основными атрибутами этого плагина являються: Fore, Back, Style' + Style.RESET_ALL)
print(Style.BRIGHT + Fore.RED + 'Тут есть конструктор init()' + Style.RESET_ALL)
print(Style.BRIGHT + 'В конце надо сбросить стиль командой Style.RESET_ALL если надо на каждой строчке писать другим стилем' + Style.RESET_ALL)
print('Снизу примеры')
print(Fore.RED + 'Красный текст' + Style.RESET_ALL)
print(Back.GREEN + 'Зеленый фон' + Style.RESET_ALL)
print(Fore.YELLOW + Back.BLUE + 'Желтый текст на синем фоне' + Style.RESET_ALL)
print(Fore.GREEN + 'зеленый текст')
print(Back.YELLOW + 'на желтом фоне' + Style.RESET_ALL)
print(Style.BRIGHT + 'стал жырнее' + Style.RESET_ALL)
print('обычный текст')
