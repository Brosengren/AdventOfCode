import re


splitinput = []
passports = []
data = []

with open("Day4IN.txt") as f:
	splitinput = f.read().split("\n\n")
for line in splitinput:
	line = re.split('\n|\s',line)
	for item in line:
		data.append(item.split(':'))
	passports.append(data)
	data = []
	
reqFlds = [
	'byr',
	'iyr',
	'eyr',
	'hgt',
	'hcl',
	'ecl',
	'pid'
]

passport = []
count = 0

for passport in passports:
	flds = []
	for item in passport:
		flds.append(item[0])
	if(set(reqFlds).issubset(flds)):
		count += 1
print(count)