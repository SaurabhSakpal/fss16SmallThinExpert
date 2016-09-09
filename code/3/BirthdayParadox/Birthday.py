import random

def has_duplicates(list):
	new_dict = {}
	for i in range(len(list)):
		if new_dict.has_key(list[i]):
			return False
		new_dict[list[i]] = 1
	return True;


def birthdayParadox(numberOfPeople, numberOfSamples) :
	repeatedBirthdayCount = 0;
	for i in range(numberOfSamples) :
		randomBirthdays = []
		for j in range(numberOfPeople) :
			birthday = random.randint(1,366)
			randomBirthdays.append(birthday)
		if has_duplicates (randomBirthdays) :
			repeatedBirthdayCount = repeatedBirthdayCount + 1
	return float(repeatedBirthdayCount) / numberOfSamples








listWithOutDuplicate = [2, 3, 4, 5, 6]
listWithDuplicate = [2, 3, 4, 5, 6, 4]

print 'Does folowing list : % has duplicates % ',listWithOutDuplicate, has_duplicates(listWithDuplicate)
print has_duplicates(listWithOutDuplicate)

numberOfPeople = 23
numberOfSamples = 100

print birthdayParadox(numberOfPeople, numberOfSamples)
