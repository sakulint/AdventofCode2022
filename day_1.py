"""
Advent of code 2022. Day 1
"""

def main():

    file = open("input_file", mode="r")
    file_lines = [line[:-1] for line in file]

    summa = 0
    lista_summista = []

    for file_line in file_lines:

        if file_line == "":
            lista_summista.append(summa)
            summa = 0
        else:
            summa += int(file_line)

    file.close()

    lista_summista.sort(reverse=True)
    print(sum(lista_summista[:3]))

if __name__ == "__main__":
    main()