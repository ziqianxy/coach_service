# coding=utf-8
import csv
import string

from common_utils import gps

CSV_NAME = '_2016-1210-080343'
file_name = '_data_resolved/' + CSV_NAME + '.csv'

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
def print_list(d_list):
    for i in d_list:
        print i


data_list = []
# read data
with open(file_name, 'rb') as data:
    reader = csv.reader(data)
    for line in reader:
        data_list.append(line)
    pre_row = 2
    data_list = data_list[pre_row:]

gps_list = []
# resolve data
for row in data_list[1:-1:50]:
    LON = string.atof(row[km.get("G_LON")])
    LAT = string.atof(row[km.get("G_LAT")])
    gps_list.append([LON, LAT])

print gps.gps2amap(gps_list)
