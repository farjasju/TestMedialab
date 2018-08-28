from os import path, name
import csv
from collections import Counter
from tqdm import tqdm

def analyse_nbtweets(data_file):
	directory = path.dirname(__file__)
	path_to_file = path.join(directory, "data", data_file)

	with open(path_to_file,"r", encoding="utf-8") as f:
		cr = csv.DictReader(f)
		nbTweets = Counter()

		for row in tqdm(cr):
			nbTweets[row['from_user_name']] += 1

		top50 = nbTweets.most_common(50)

	with open("top50.csv", "w") as csvresult:
		spamwriter = csv.DictWriter(csvresult,fieldnames=["Pseudo", "Nb de tweets"])
		spamwriter.writeheader()
		for user,nb in top50:
			spamwriter.writerow({"Pseudo":user, "Nb de tweets":nb})

def analyse_client(data_file):
	directory = path.dirname(__file__)
	path_to_file = path.join(directory, "data", data_file)

	with open(path_to_file,"r", encoding="utf-8") as f:
		cr = csv.DictReader(f)
		nbTweets = Counter()
		nbInsoumis = 0
		nbRepublicains = 0
		nbLREM = 0
		nbAndroidIns = 0
		nbAndroidRep = 0
		nbAndroidEm = 0
		nbiPhoneIns = 0
		nbiPhoneRep = 0
		nbiPhoneEm = 0
		insoumis = ["insoumis", "mélenchon"]
		republicains = [" droite", "mercins", "républicains", "epublicain"]
		lrem = ["enmarche", "marcheur", "en marche", "lrem", "macron"]


		for row in tqdm(cr):
			description = row["from_user_description"].lower()
			if any(x in description for x in insoumis):
				nbInsoumis += 1
				if "Android" in row["source"] :
					nbAndroidIns += 1
				elif "iPhone" in row["source"] :
					nbiPhoneIns += 1
			elif any(x in description for x in republicains):
				nbRepublicains += 1
				if "Android" in row["source"] :
					nbAndroidRep += 1
				elif "iPhone" in row["source"] :
					nbiPhoneRep += 1
			elif any(x in description for x in lrem):
				nbLREM += 1
				if "Android" in row["source"] :
					nbAndroidEm += 1
				elif "iPhone" in row["source"] :
					nbiPhoneEm += 1


	PerFIiPhone = nbiPhoneIns/nbInsoumis
	PerFIAndroid = nbAndroidIns/nbInsoumis
	PerLREMiPhone = nbiPhoneEm/nbLREM
	PerLREMAndroid = nbAndroidEm/nbLREM
	PerLRiPhone = nbiPhoneRep/nbRepublicains
	PerLRAndroid = nbAndroidRep/nbRepublicains

	with open("iphonevsandroid.csv", "w") as csvresult:
		spamwriter = csv.DictWriter(csvresult,fieldnames=["Parti", "Pourcentage d'iPhone user", "Pourcentage d'Android user"])
		spamwriter.writeheader()
		spamwriter.writerow({"Parti":"France Insoumise", "Pourcentage d'iPhone user":PerFIiPhone, "Pourcentage d'Android user":PerFIAndroid})
		spamwriter.writerow({"Parti":"LREM", "Pourcentage d'iPhone user":PerLREMiPhone, "Pourcentage d'Android user":PerLREMAndroid})
		spamwriter.writerow({"Parti":"Les Républicains", "Pourcentage d'iPhone user":PerLRiPhone, "Pourcentage d'Android user":PerLRAndroid})


if __name__ == "__main__":
	analyse_nbtweets("sample.csv")


