import csv

user_list =  [
    {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
    {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
    {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'}
]

def read_csv(name_list):
    with open('user_list.csv', 'w', encoding='utf-8') as f:
        fields = ['name', 'age', 'job']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()
        for user in name_list:
            writer.writerow(user)

def main():
    read_csv(user_list)
    
if __name__ == "__main__":
    main()