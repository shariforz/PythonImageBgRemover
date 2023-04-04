from pathlib import Path

p = Path('Exam') # ваша "корневая папка"
sstring = "http://server1.com/exam/index.html"       # строка для поиска

for f in p.rglob('test.txt'):
    outdata = []                                     # создаем пустой список для хранения исправленных данных
    with f.open(encoding='utf8', mode='r') as ifile: # открываем на чтение
        indata = ifile.readlines()                   # читаем файл построчно в список
        for i in content:                            # проходимся по списку, меняя искомую строку на нужную
            i = i.replace(sstring, f"http://server2.com/exam/{Path(f).parent.name}/index.html")
            outdata.append(i)                        # ^ здесь поставляется имя родительской папки
    with f.open(encoding='utf8', mode='w') as ofile: # открываем тот же файл на запись
        ofile.writelines(outdata)                    # пишем в него измененные данные.