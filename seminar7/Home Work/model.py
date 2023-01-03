import csv

# def reading_txt_file():
#     with open('file.txt', encoding='utf-8') as r_file:
#         data = r_file.read()
#     return data

def reading_txt_file():
    with open('file.txt', 'r', encoding='utf-8') as data:
        list_1 = data.read().split('\n')
    list_2 = []
    list_3 = []
    count = 0
    i = 0
    while i < len(list_1):
        while count < 4:
            list_2.append(list_1[i])
            count += 1
            i += 1
        list_3.append(list_2)
        list_2 = []
        count = 0
    list_4 = []
    for i in range(len(list_3) - 1):
        dic = {list_3[0][0]: list_3[i + 1][0],
               list_3[0][1]: list_3[i + 1][1],
               list_3[0][2]: list_3[i + 1][2],
               list_3[0][3]: list_3[i + 1][3]}
        list_4.append(dic)
        dic = {}
    return list_4


def reading_csv_file():
    with open('file.csv', encoding='utf8') as data:
        reader = csv.DictReader(data, delimiter=',')
        return list(reader)

# def record_txt(data):
#     with open('record.txt', 'w', encoding='utf-8') as w_file:
#         for s in data:
#             w_file.write('\n'.join(s) + '\n\n')


def record_txt(data):
    with open('record.txt', 'w', encoding='utf-8') as file:
        for i in range(len(data)):
            if i == 0:
                for key in data[i]:
                    file.write(key + '\n')
                for key, value in data[i].items():
                    file.write(value + '\n')
            else:
                for key, value in data[i].items():
                    file.write(value + '\n')


def record_csv(data):
    with open('record.csv', 'w', encoding='utf8', newline='') as rec:
        writer = csv.DictWriter(rec, fieldnames=list(data[0].keys()), delimiter=';')
        writer.writeheader()
        for i in data:
            writer.writerow(i)




