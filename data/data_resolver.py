import csv
import string

from common_utils.util_log import log

CSV_NAME = '2016-1210-080343'
file_name = './_data/' + CSV_NAME + '.csv'
file_save = './_data_resolved/_' + CSV_NAME + '.csv'

# key-map of the column
km = {
    "_time": 0, "G_STA": 1, "G_LON": 2, "G_LAT": 3, "G_ALT": 4,
    "G_pdop": 5, "G_hdop": 6, "G_vdop": 7, "G_SPD": 8, "G_DIR": 9,
    "G_DATE": 10, "G_TIME": 11, "SL_V": 12, "SL_GPS": 13, "SL_BD": 14,
    "G_MODE": 15, "_0103": 16, "_0104": 17, "_0105": 18, "_0106": 19,
    "_0107": 20, "_010c": 21, "_010d": 22, "_010e": 23, "_010f": 24,
    "_0110": 25, "_0111": 26, "_0115": 27, "_011f": 28, "_0121": 29,
    "_0124": 30, "_012e": 31, "_0130": 32, "_0131": 33, "_0133": 34,
    "_0134": 35, "_013c": 36, "_013e": 37, "_0142": 38, "_0143": 39,
    "_0144": 40, "_0145": 41, "_0147": 42, "_0149": 43, "_014a": 44,
    "_014c": 45, "_014d": 46, "_014e": 47
}


# function to print the list data
def print_data(d_list):
    for i in d_list:
        print i


data_list = []
cmd = []

# read data
with open(file_name, 'rb') as data:
    reader = csv.reader(data)
    for line in reader:
        data_list.append(line)
    cmd = data_list[1]

    # to print cmd
    # idx = 0
    # for item in cmd:
    #     # print idx,'\t',item,'\t', data_list[2][idx]
    #     print '"', item, '":', idx, ','
    #     idx += 1
    # to slice the data head
    pre_row = 2
    data_list = data_list[pre_row:]

print cmd

# forward and backward replace the data twice
for i in range(1, 2):

    # resolve err with forward data
    log.info('== to replace err with forward data ==')

    idx, idy = 0, 0
    for row in data_list:
        idy = 0
        for item in row:
            if idx == 0:
                continue
            if item == 'err':
                print idx, idy, data_list[idx - 1][idy], data_list[idx][idy]
                data_list[idx][idy] = data_list[idx - 1][idy]
            idy += 1
        idx += 1

    log.info('== forward process done! ==')

    # resolve err with backward data
    log.info('== to replace err with backward data ==')

    idx, idy = 0, 0
    for row in data_list:
        idy = 0
        for item in row:
            if idx == len(data_list) - 1:
                continue
            if item == 'err':
                print idx, idy, data_list[idx][idy], data_list[idx + 1][idy]
                data_list[idx][idy] = data_list[idx + 1][idy]
            idy += 1
        idx += 1

    log.info('== backward process done! ==')

# resolve data
for row in data_list:
    row[km.get("G_LON")] = row[km.get("G_LON")][:-2]
    row[km.get("G_LAT")] = row[km.get("G_LAT")][:-2]
    row[km.get("G_ALT")] = row[km.get("G_ALT")][:-1]

    key = "_0104"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp * 100.0 / 255)

    key = "_0105"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp - 40)

    key = "_0106"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str((tmp - 128) * 100.0 / 128)

    key = "_0107"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str((tmp - 128) * 100.0 / 128)

    key = "_010c"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp / 4.0)

    key = "_010d"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp)

    key = "_010e"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str((tmp - 128) / 2.0)

    key = "_010f"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp - 40)

    key = "_0110"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp / 100.0)

    key = "_0111"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp * 100.0 / 255)

    key = "_011f"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp)

    key = "_0121"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp)

    key = "_0124"
    tmp_1 = string.atoi(row[km.get(key)][4:-4], 16)
    tmp_2 = string.atoi(row[km.get(key)][8:], 16)
    row[km.get(key)] = str(tmp_1 / 32768.0) + '-' + str(tmp_2 / 8192.0)

    key = "_012e"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp * 100 / 255)

    key = "_0130"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp)

    key = "_0131"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp)

    key = "_0133"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp)

    key = "_0134"
    tmp_1 = string.atoi(row[km.get(key)][4:-4], 16)
    tmp_2 = string.atoi(row[km.get(key)][8:], 16)
    row[km.get(key)] = str(tmp_1 / 32768.0) + '-' + str(tmp_2 / 256.0 - 128)

    key = "_013c"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp / 10.0 - 40)

    key = "_013e"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp / 10.0 - 40)

    key = "_0142"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp / 1000.0)

    key = "_0143"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp * 100.0 / 255)

    key = "_0144"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp / 32768)

    key = "_0145"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp * 100.0 / 255)

    key = "_0147"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp * 100.0 / 255)

    key = "_0149"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp * 100.0 / 255)

    key = "_014a"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp * 100.0 / 255)

    key = "_014c"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp * 100.0 / 255)

    key = "_014d"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp)

    key = "_014e"
    tmp = string.atoi(row[km.get(key)][4:], 16)
    row[km.get(key)] = str(tmp)

log.info('==== data resolve done! ==== ')

print_data(data_list)

# write data into new file
# mode must be 'b', or it will got some new line
with open(file_save, 'ab') as f:
    writer = csv.writer(f)
    writer.writerow(cmd)
    for line in data_list:
        writer.writerow(line)
