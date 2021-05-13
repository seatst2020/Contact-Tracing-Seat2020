import db, random

db.initialize_db()


data = db.sql_statement("SELECT * FROM students;")


def contact_tracing(data_input, infected_student):
  infected_lst = []
  def compare_schedules(Sch1, Sch2):
    xsch = Sch1.split()
    ysch = Sch2.split()
    y = 0 
    for clss in xsch:
      if clss == ysch[y]:
        return True
      y = y + 1
    return False

  for student in data_input:
        if compare_schedules(infected_student[3], student[3]):
          print(student)
          infected_lst.append(student)
  return infected_lst
  
   

  

    



# contact_tracing(data, random.choice(data))