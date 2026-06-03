import os

infile = "inputFile.txt"
outfile = "outputFile.txt"

# Create a sample input file if it does not exist
if not os.path.exists(infile):
	with open(infile, "w") as f:
		f.write("Ford,Mustang,2020,Red\n")
		f.write("Toyota,Camry,2019,Blue\n")
		f.write("Honda,Civic,2021,Black\n")

# Clean up previous output file if exists to prevent accumulation across runs
if os.path.exists(outfile):
	os.remove(outfile)

# print each line, as read in
with open(infile) as f1:
	for line in f1:
		print (line)

print ("\n*******************")

# print each line, stripping last newline character
with open(infile) as f1:
	for line in f1:
		print (line[:-1])

print ("\n*******************")
		
# print makes only (first word of each line)
with open(infile) as f1:
	for line in f1:
		row = line.split(",")
		print(row[0])

print ("\n*******************")
		
# print each line as a formatted list
with open(infile) as f1:
	for line in f1:
		row = line.split(",")
		print(row[0] + "\n-----------------")
		for i in range(1, len(row)):
			print(row[i])

print ("\n*******************")
			
# add each line to a list
cars = list()
with open(infile) as f1:
	for line in f1:
		row = line.split(",")
		cars.append(row)
	print(cars[0][0])
	
# write Makes only to outputFile
with open(outfile, 'a') as f2:
	for car in cars:
		f2.write(car[0] + "\n")

# write list of row-lists to outputFile
with open(outfile, 'a') as f2:
	for car in cars:
		f2.write(str(car) + "\n")
		