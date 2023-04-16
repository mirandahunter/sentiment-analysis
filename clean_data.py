import re
import string

filename = 'IMDBDataset.csv'
file = open(filename, 'r')
text = file.read()
file.close()

write_file = open('clean_dataset.csv', 'w')

lines = text.split('\n')
lines = lines[1:]
for line in lines:
	if "<br />" in line:
		line = re.sub("<br />", "", line)

		table = str.maketrans('', '', string.punctuation)

		stripped = line.translate(table)
		stripped = re.sub(r'\d', '', stripped)
		stripped = stripped.lower()

		sentiment = stripped[-8:]

		stripped = stripped[:-8]
		
		write_file.write(stripped + "," + sentiment + "\n")