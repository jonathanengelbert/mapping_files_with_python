import csv


example_file = open("test.csv")
example_reader = csv.reader(example_file)
#example_data = list(example_reader)

#=========================================================================
#Reading through rows (READER OBJECT)
# for row in example_reader:
#     print("Row #" + str(example_reader.line_num)+ " -> "+str(row))

#NOTE: The Reader object can be looped over only once. To reread the CSV file, you must call csv.reader to create a Reader object.
#=========================================================================
#Writing data(WRITER OBJECT)

output = open('output.csv', 'w', newline='')
output_writer = csv.writer(output)
output_writer.writerow(["spam", 'eggs', 'bacon', 'ham'])
output_writer.writerow(['Test', 'Another Test', 'Final Test'])
output.close()
#=========================================================================