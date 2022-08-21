
def parse():
    data_temp = {}
    for i in range(1,13):
        temperatures = open(f"data/110-tavg-1-{i}-1990-2022.csv", "r")
        for _ in range(0,6):
            temperatures.readline()
        for _ in range(0,29):
            line = temperatures.readline().split(',')
            data_temp[int(line[0])] = float(line[1][:-2])
        temperatures.close()
    data = []
    death_file = open("data/Deaths by Month Table.csv",'r')
    while line[0] != "":
        line = death_file.readline().split(';')
        if line[0].isdigit():
            if line[1] == "Jan":
                data.append((data_temp[int(line[0]) * 100 + 1], int(line[2])))
            elif line[1] == "Feb":
                data.append((data_temp[int(line[0]) * 100 + 2], int(line[2])))
            elif line[1] == "Mar":
                data.append((data_temp[int(line[0]) * 100 + 3], int(line[2])))
            elif line[1] == "Apr":
                data.append((data_temp[int(line[0]) * 100 + 4], int(line[2])))
            elif line[1] == "May":
                data.append((data_temp[int(line[0]) * 100 + 5], int(line[2])))
            elif line[1] == "Jun":
                data.append((data_temp[int(line[0]) * 100 + 6], int(line[2])))
            elif line[1] == "Jul":
                data.append((data_temp[int(line[0]) * 100 + 7], int(line[2])))
            elif line[1] == "Aug":
                data.append((data_temp[int(line[0]) * 100 + 8], int(line[2])))
            elif line[1] == "Sep":
                data.append((data_temp[int(line[0]) * 100 + 9], int(line[2])))
            elif line[1] == "Oct":
                data.append((data_temp[int(line[0]) * 100 + 10], int(line[2])))
            elif line[1] == "Nov":
                data.append((data_temp[int(line[0]) * 100 + 11], int(line[2])))
            elif line[1] == "Dec":
                data.append((data_temp[int(line[0]) * 100 + 12], int(line[2])))
    death_file.close()

    # print_min_max_temp(data)
    # print_data(data)

    return data

def print_min_max_temp(data):
    min_temp = 100
    max_temp = 0
    for value in data.values():
        if value[0] < min_temp:
            min_temp = value[0]
        if value[0] > max_temp:
            max_temp = value[0]
    print(min_temp, max_temp)

def print_data(data):
    for d in data:
        print(d)


if __name__ == "__main__":
    parse()