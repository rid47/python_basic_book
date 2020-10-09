import argparse
import os
import csv

parser = argparse.ArgumentParser()

parser.add_argument('-i', required=True)
parser.add_argument('-o', required=True)
parser.add_argument('-r', required=True)

args = parser.parse_args()

print(f"args: {args}")

print(f"Input: {args.i}; Output: {args.o}; rows: {args.r}")

row_per_csv = int(args.r)

if os.path.isfile(args.i):
    print("file exists")
    file = args.i
    with open(file, "r") as f:

        # count no of rows
        rows = 0
        for line in f:
            rows += 1

        print(f"No of rows: {rows}")
        f.seek(0, 0)  # reset cursor to start position

        file_reader = csv.reader(f)
        if rows < row_per_csv:
            print("Not enough rows to split")
        else:
            no_of_chunks = rows // row_per_csv
            print(f"Split into {no_of_chunks} chunks")
            content_list = []
            title = next(file_reader)
            print(f"Title : {title}")
            for row in file_reader:
                content_list.append(row)

            print(f"Content list: {content_list}")

            output_chunk = []
            start_index = 0
            while start_index <= len(content_list):
                end_index = start_index+row_per_csv
                enough_row_to_loop = start_index + 2* row_per_csv
                if enough_row_to_loop <= len(content_list):
                    output_chunk.append(content_list[start_index:end_index])
                    start_index += row_per_csv
                else:
                    output_chunk.append(content_list[start_index:len(content_list)])
                    break

            print(f"Your chunk to write : {output_chunk}")

            i = 1
            for chunk in output_chunk:
                chunk.insert(0, title)
                print(chunk)
                with open(args.o+str(i), "w") as my_file:
                    writer = csv.writer(my_file)
                    writer.writerows(chunk)
                    i += 1

else:
    print("file does not exists!")
