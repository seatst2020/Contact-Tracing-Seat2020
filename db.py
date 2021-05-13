import sqlite3, name_generator, random

conn = sqlite3.connect("database.db")
c = conn.cursor()

def initialize_db():
  print('Setting up database...')

  SQL_STATEMENT = """CREATE TABLE IF NOT EXISTS students(
  "Key" INTEGER PRIMARY KEY AUTOINCREMENT,
  "Name" TEXT,
  "Year" TEXT,
  "Schedule" TEXT
  );"""

  c.execute(SQL_STATEMENT)

  for x in range(50):
    insert_into_database()

  pass

def sql_statement(statement):
  c.execute(statement)
  return c.fetchall()

def list_to_string(l):
  str1 = ""
  for x in l:
    str1 = str1 + x + " "
  return str1

def string_to_list(str1):
  return str1.split()  

def insert_into_database():
  classes = ["English", "Social Studies", "Science", "Study Hall", "Math", "Pathway", "Gym", "Health", "Spanish"]

  years = ["Freshman", "Sophmores", "Juniors", "Seniors"]


  random.shuffle(classes)

  # Insert some users into our database
  try:
    name = "'" + name_generator.generate('first') + " " + name_generator.generate('last') + "'"
    year = "'" + random.choice(years) + "'" 
    schedule = "'" + list_to_string(classes) + "'"


    print('Adding', name, "to the database...")
  
    SQL_STATEMENT = "INSERT INTO students (Name, Year, Schedule) VALUES ({},{},{});".format(name, year, schedule)

    print('New Entry Added')

  #PROGRAMMING ERROR WITH SQL Statement
    c.execute(SQL_STATEMENT)

   
  except TypeError:
    print('Unrecognized string character')

  

  

  

  pass