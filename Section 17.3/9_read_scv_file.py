def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as file:
    #     headings = data.readline().replace('\n', '').split(',')
    #     total_info = []
    #     for temp_line in data.readlines():
    #         temp = {}
    #         for info in zip(headings, temp_line.replace('\n', '').split(',')):
    #             temp[info[0]] = info[1]
    #
    #         total_info.append(temp)
    #
    #     return total_info
        keys = file.readline().replace('\n', '').strip()
        return [dict(zip(keys, line.strip().split(','))) for line in file]

read_csv()