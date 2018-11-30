import os


# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"
# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class Worker:
    def __init__(self, name, surname, salary, job, normal_hours):
        self.name = name
        self.surname = surname
        self.job = job
        self.salary = int(salary)
        self.normal_hours = int(normal_hours)
        self.job_hours = 0

    def calculation_salary(self):
        for_hour = self.salary // self.normal_hours
        if self.job_hours > self.normal_hours:
            salary = ((self.job_hours - self.normal_hours) * for_hour) * 2
            return (salary + self.salary)
        elif self.job_hours < self.normal_hours:
            salary = (self.normal_hours - self.job_hours) * for_hour
            return (self.salary - salary)
        else:
            return (self.salary)

    def write_salary(self, salary):
        print(self.name + ' ' + self.surname + ' - ' + self.job + ' c заработной платой ' + str(salary) + 'р')

    def read_job_hours(self):
        with open('data\\hours_of', 'r', encoding='UTF-8') as f:
            for i in f.readlines():
                if i.split()[0] == self.name and i.split()[1] == self.surname:
                    self.job_hours = int(i.split()[2])
                    break
                else:
                    continue

def file_handle(file):
    f = open(file, 'r', encoding='UTF-8')
    for i in f.readlines():
        if i.count('Имя') == 1:
            continue
        else:
            name, surname, salary, job, normal_hours = i.split()
            workman = Worker(name, surname, salary, job, normal_hours)
            workman.read_job_hours()
            salary = workman.calculation_salary()
            workman.write_salary(salary)
    f.close()


file_handle('data\\workers')
