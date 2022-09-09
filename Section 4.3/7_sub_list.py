def sun_listing(main_list):
    res_list = [[]]
    temp_list = []

    for i in range(len(main_list)):
        for j in range(len(main_list)):
            temp_list = main_list[j:i + j + 1]

            if len(temp_list) == i + 1:
                res_list.append(temp_list)

    return res_list


main_list = input().split()
print(sun_listing(main_list))