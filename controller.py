import view
import model

def start():
    model.set_class(view.input_class())
    model.set_subject(view.input_subject(model.get_path()))
    model.open_file()
    while True:
        journal= model.get_journal()
        view.list_of_child(journal)
        student = view.who_answer()
        if student == 'exit':
            break
        student=view.check_student(model.get_journal(),student)
        mark= int(view.what_mark())
        model.student_mark(student,mark)
    model.save_file()