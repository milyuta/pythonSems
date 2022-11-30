import csv
import string
from os.path import exists


def append_user(info):
    path = 'C:\\Users\\milutin.a\\Desktop\\python\\8hw\\DATABASE.csv'
    valid = exists(path)
    if not valid:
        creating()
    writing_scv(info)

def creating ():
    file = 'C:\\Users\\milutin.a\\Desktop\\python\\8hw\\DATABASE.csv'
    with open (file, 'w', encoding = 'utf-8') as csvfile:
          csvfile.write(f'id, last name, name, second name, phone number \n')

def writing_scv(info):
    file = 'C:\\Users\\milutin.a\\Desktop\\python\\8hw\\DATABASE.csv'
    with open (file, 'a', encoding = 'utf-8') as csvfile:
        csvfile.write(f'{info[0]},{info[1]},{info[2]},{info[3]},{info[4]}\n')

def reading_csv(id):
    file ='C:\\Users\\milutin.a\\Desktop\\python\\8hw\\DATABASE.csv'
    with open(file, 'r', encoding='utf-8') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for row in csv_reader:
            for n in row:
                if row[0]=='1':
                #if row[0]==str(id):
                    f_string=row
                
        print(f_string[1], f_string[2],f_string[3], f_string[4])
  