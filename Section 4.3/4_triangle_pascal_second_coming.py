def pascal(search_row):
    gen_ls = [[1]]

    for i in range(search_row):
        print(*gen_ls[i])

        team_list = [gen_ls[i][num - 1] + gen_ls[i][num] for num in range(1, len(gen_ls[i]))]
        team_list.append(1)
        team_list.insert(0, 1)

        gen_ls.append(team_list)


n = int(input())
pascal(n)
