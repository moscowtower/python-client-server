import subprocess

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 1 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
strings = ['разработка', 'сокет', 'декоратор']
print('Обычные строки:')
for s in strings:
    print(type(s), s)

unicoded = ['\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430',
            '\u0441\u043e\u043a\u0435\u0442',
            '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440']
print('Отюникоженные строки:')
for u in unicoded:
    print(type(u), u)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
byted = [b'class', b'function', b'method']

print('Отбайченные строки: ')
for b in byted:
    print(type(b), len(b), b)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
hmm = [b'attribute', "bytes не прокатит - 'класс'", "bytes не прокатит - 'функция'", b'type']
verdict = 'В байты можно перевести только литералы, чей юникод < 255'

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
to_encode = ['разработка', 'администрирование', 'protocol', 'standard']
for i in to_encode:
    encoded = i.encode('utf-8')
    decoded = encoded.decode('UTF-8')
    print('UTF-8: ', encoded, ' Decoded: ', decoded)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 5 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
args = ['ping', 'yandex.ru']
subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    print(line.decode('utf-8')) # У меня OS X на английском, мне декодинг cp866 не нужен, но я честно шарю за энкодинги

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 6 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
f_n = open('test_file.txt', 'r')
print(f_n)  # encoding='UTF-8', у вас все задание на локализированных русичей нацелено :(
with open('test_file.txt', 'r', encoding='utf-8') as f:
    print(f.read())