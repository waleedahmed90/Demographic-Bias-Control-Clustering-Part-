#/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/Counts_Demographics

import gzip
import json
import glob
import itertools
import time
import numpy as np
import os
import ntpath
import shutil



def percentages(templist):
	perc = [((i*100)/sum(templist)) for i in templist]
	return perc 


def stats(demo_gender, demo_race, demo_age):
	stats_gender = {}
	stats_race = {}
	stats_age = {}

	for h in demo_gender:
		stats_gender[h] = percentages(demo_gender[h]) 
		stats_race[h] = percentages(demo_race[h])
		stats_age[h] = percentages(demo_age[h])



	return stats_gender, stats_race, stats_age





if __name__== "__main__":
	start_time = time.time()

	path_gender = "./Demographics_Count/Gender_Count_User_Demographics.gz"
	path_race = "./Demographics_Count/Race_Count_User_Demographics.gz"
	path_age = "./Demographics_Count/Age_Count_User_Demographics.gz"
	



	#Loading dictionaries of Promoter Counts Gender
	with gzip.open(path_gender,'rt') as T1:
		demo_gender_temp = T1.read()
	T1.close()

	demo_gender = json.loads(demo_gender_temp)
	
	#Loading dictionaries of Promoter Counts Race
	with gzip.open(path_race,'rt') as T2:
		demo_race_temp = T2.read()
	T2.close()

	demo_race = json.loads(demo_race_temp)
	
	#Loading dictionaries of Promoter Counts Age
	with gzip.open(path_age,'rt') as T3:
		demo_age_temp = T3.read()
	T3.close()

	demo_age = json.loads(demo_age_temp)

	#create a new directory to store the results//////////if its existing already then its alright

	try:
		os.mkdir('./Demographics_Percentages')
	except:
		shutil.rmtree('./Demographics_Percentages', ignore_errors=True)
		os.mkdir('./Demographics_Percentages')



	Gender_perc, Race_perc, Age_perc = stats(demo_gender, demo_race, demo_age)

	with gzip.open('./Demographics_Percentages/Gender_Percentage_User_Demographics.gz', 'wb') as f1:
		#fout.write(json.dumps(data).encode('utf-8'))
		f1.write(json.dumps(Gender_perc).encode('utf-8'))
	f1.close()
	print("<./Demographics_Percentages/Gender_Percentage_User_Demographics.gz>:::::Written")
	
	with gzip.open('./Demographics_Percentages/Race_Percentage_User_Demographics.gz', 'wb') as f2:
		#fout.write(json.dumps(data).encode('utf-8'))
		f2.write(json.dumps(Race_perc).encode('utf-8'))
	f2.close()
	print("<./Demographics_Percentages/Race_Percentage_User_Demographics.gz>:::::Written")
	
	with gzip.open('./Demographics_Percentages/Age_Percentage_User_Demographics.gz', 'wb') as f3:
		#fout.write(json.dumps(data).encode('utf-8'))
		f3.write(json.dumps(Age_perc).encode('utf-8'))
	f3.close()
	print("<./Demographics_Percentages/Age_Percentage_User_Demographics.gz>:::::Written")



	print("Elapsed Time")
	print("--- %s seconds ---" % (time.time() - start_time))

	