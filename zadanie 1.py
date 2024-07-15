# Входные данные

grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]] #оценки в алфавитном порядке
students = {'Sasha','Andrey','Alex','Dima','Lena'} #имена студентов не упорядоченно

# Алгоритм

list_students = list(students) #преобразование множества имён студентов в список
list_students.sort() #сортировка списка имён студентов по алфавиту
para = zip(list_students,grades) #создание пар элементов из списков имён и оценок
st_di = {student:sum(grade)/len(grade) for student,grade in para} #создание целевого словаря при помощи генератора словарей
print(st_di)
