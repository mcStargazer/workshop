# Ref: pymotw.com/2/csv/

import csv


def read_csv(filename):

    try:
        f = open(filename, 'rb')
        reader = csv.reader(f)
        rows = []
        for row in reader:
            rows.append(row)

    finally:
        f.close()

    return rows


def write_csv(filename, rows):

    try:
        f = open(filename, 'wb')
        writer = csv.writer(f)
        for row in rows:
            writer.writerow(row)

    finally:
        f.close()


if __name__ == "__main__":

    data = [["col1", "col2", "col3"],
            ['1', '2', '3'],
            ['10', '11', '12']]

    write_csv("test.csv", data)
    contents = read_csv("test.csv")
    print("CSV Contents:\n{}".format(contents))
