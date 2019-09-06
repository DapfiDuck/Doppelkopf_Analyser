# reads csv and returns it as 2D List

def get_sheet(url):
    csv = [];

    #get csv as raw text
    file = open(url, "r")
    text = file.read();
    file.close()

    lines = text.split("\n")

    # convert lines to cell arrays
    for line in lines:
        row = line.split(",")

        for cell in row:
            cell = cell.strip()

        csv.append(row)

    return csv

def write_sheet(url, sheet=[[]]):

    text = ""

    for row in sheet:

        row_str = ""

        for cell in row:
            row_str += str(cell)+","
        text += f"{row_str[0:-1]}\n"

    file = open(url, "w")
    file.write(text)
    file.close()

def append_sheet(url, sheet=[[]]):

    text = ""

    for row in sheet:

        row_str = ""

        for cell in row:
            row_str += str(cell)+","
        text += f"{row_str[0:-1]}\n"

    file = open(url, "a")
    file.write("\n")
    file.write(text)
    file.close()
