import random

def has_duplicates(list):
	new_dict = {}
	for i in range(len(list)):
		if new_dict.has_key(list[i]):
			return True
		new_dict[list[i]] = 1
	return False;


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

str1 = ' '.join(str(e) for e in listWithOutDuplicate)
str2 = ' '.join(str(e) for e in listWithDuplicate)

str3 = "Does folowing list " + str1
str3 = str3 + " has duplicates: " + str(has_duplicates(listWithOutDuplicate))
print str3


str4 = "Does folowing list " + str2
str4 = str4 + " has duplicates: " + str(has_duplicates(listWithDuplicate))
print str4

numberOfPeople = 23
numberOfSamples = 100

str5 =  "Probabilty of two people having same bday is "+str(birthdayParadox(numberOfPeople, numberOfSamples))
str5 = str5 + " number of people = "+str(numberOfPeople)+" and number Of Runs = "+str(numberOfSamples)

print str5