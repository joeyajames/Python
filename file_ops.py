infile = "inputFile.txt"
outfile = "outputFile.txt"

# read file and print each line
with open(infile) as f:
    for line in f:
        print(line, end='')

# read file and print each line without the newline character
with open(infile) as f:
    for line in f:
        print(line.rstrip())

# read file and print only the first word of each line
with open(infile) as f:
    for line in f:
        print(line.split(',')[0])

# read file and print each line as a formatted list
with open(infile) as f:
    for line in f:
        row = line.split(',')
        print(f"{row[0]}\n{'-' * 17}")
        for item in row[1:]:
            print(item.strip())

# read file and create a list of rows
with open(infile) as f:
    cars = [line.strip().split(',') for line in f]

# write Makes only to outputFile
with open(outfile, 'w') as f:
    f.write('\n'.join(car[0] for car in cars))

# write list of rows to outputFile
with open(outfile, 'a') as f:
    f.write('\n'.join(str(car) for car in cars))
