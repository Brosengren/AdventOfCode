def byr_ck(passport):
	for item in passport:
		if item[0] == "byr":
			year = int(item[1])
			if(year in range(1920, 2003)):
				return 1
	return 0
	
def iyr_ck(passport):
	for item in passport:
		if item[0] == "iyr":
			year = int(item[1])
			if(year in range(2010, 2021)):
				return 1
	return 0
				
def eyr_ck(passport):
	for item in passport:
		if item[0] == "eyr":
			year = int(item[1])
			if(year in range(2020, 2031)):
				return 1
	return 0
				
def hgt_ck(passport):
	for item in passport:
		if item[0] == "hgt":
			try:
				sys = re.findall("\D+", item[1])[0]
				height = int(re.findall("\d+", item[1])[0])
			except: 
				return 0
			if(sys == "cm" and height in range(150, 194)):
				return 1
			if(sys == "in" and height in range(59, 77)):
				return 1
	return 0
	
def hcl_ck(passport):
	for item in passport:
		if item[0] == "hcl":
			if(item[1][0] != '#'):
				return 0
			hair = item[1].split('#')[1]
			if(len(hair) != 6):
				return 0
			for char in hair:
				c = ord(char)
				if(not((c in range(48, 58)) or (c in range(97, 103)))):
					return 0
			return 1
	return 0

eclrs = [
	'amb',
	'blu',
	'brn',
	'gry',
	'grn',
	'hzl',
	'oth',
	]

def ecl_ck(passport):
	for item in passport:
		if item[0] == "ecl":
			clr = item[1]
			if(clr in eclrs):
				return 1
	return 0

def pid_ck(passport):
	for item in passport:
		if item[0] == "pid":
			pid = item[1]
			if(len(pid) == 9):
				for char in pid:
					if(not((int(char) in range(0, 10)))):
						return 0
				return 1
	return 0

import re

splitinput = []
passports = []
data = []

with open("Day4IN.txt") as f:
	splitinput = f.read().split("\n\n")
for line in splitinput:
	line = re.split("\n|\s",line)
	for item in line:
		data.append(item.split(':'))
	passports.append(data)
	data = []
	
reqFlds = [
	"byr",
	"iyr",
	"eyr",
	"hgt",
	"hcl",
	"ecl",
	"pid"
]

passport = []
count = 0

for passport in passports:
	flds = []
	for item in passport:
		flds.append(item[0])
	if(set(reqFlds).issubset(flds)):
		if(							\
			byr_ck(passport) and	\
			iyr_ck(passport) and	\
			eyr_ck(passport) and	\
			hgt_ck(passport) and	\
			hcl_ck(passport) and	\
			ecl_ck(passport) and	\
			pid_ck(passport)		\
			):
			count += 1
		
print(count)