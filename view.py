import os
def input_class():
    
    while True:
      class1 = input('С каким классом работаем?: ').upper()
      path1 = 'Class/'+ class1 + '.txt'
      check_file = os.path.exists(path1)
      if check_file == False:
        print('Такого класса нету')
      else:
         return class1

def input_subject(path: str): 
  valid=False
  while True:
       subject=input('Какой предмет?: ').lower()
       with open(path, 'r', encoding='UTF-8') as data:
          file = data.readlines()
       for sub in file:
           if sub.split(';')[0] == subject:
              valid=True
              return subject
       if not valid:
            print('Такого предмета нет.Проверьте введеное слово на опечатки.')
            continue

def who_answer():
   return input('Кто будет отвечать?')

def check_student(journal, student):
    valid=False
    while True:  
       for study in journal:
           if study==student:
               valid=True
               print(f'Вы выбрали студента {student}')
               return student
       if not valid:  
        print('Такого стутенда нет.Попробуйте ввести имя студента еще раз')
        student = input('Кто будет отвечать?: ')
        continue   

def what_mark():
    while True:
       gradess =  input('На какую оценку ответил ученик?: ')
       try:
           int(gradess)
       except:
         print('Введите целое число')
         continue
       if int(gradess) > 5 or int(gradess)<1:
         print('Оценка не может быть больше 5 и меньше 1')
       else:
           return gradess

def list_of_child(journal: str):
    for i, child in enumerate(journal, 1):
        print(f'{i}. {child:20} {journal.get(child)}')


  