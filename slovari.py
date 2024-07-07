otryad = {'chepushila':13, 'gremlin':'medic', 'mikura':(1,2,3)} #словарь с разнотипными значениями
print(otryad)
print(otryad['gremlin']) #значение по существующему ключу
print(otryad.get('prometey','alien')) #значение по НЕ существующему ключу
otryad.update({'tankist':56, 'lotus':54}) #добавил пополнение )))
print(otryad)
print(otryad.pop('mikura')) #удаление пары с отображением её значения
print(otryad)
#----------------------------------------------------------------------
brothers = {13,'medic',13.4,True,13,} #множество с разнотипными частично повторяющимися значениями
print(brothers)
brothers.add('mikura') #добавил строку
brothers.add(False) #добавил boolean
print(brothers)
brothers.remove(True) #удалил элемент
print(brothers)