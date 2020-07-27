import gzip
import json
import glob
import os
import shutil
import time

start_time = time.time()

#This code only counts the hashtags and number of tweets they have and sorts them in descending order

with gzip.open('./Demographics_Count/Gender_Count_User_Demographics.gz','rt') as T1:
		demo_gender_temp = T1.read()
T1.close()


demo_gender = json.loads(demo_gender_temp)

#print(demo_gender)
overall_counts = {}
for h in demo_gender.keys():
	overall_counts[h] = sum(demo_gender[h])


sort_demo = sorted(overall_counts.items(), key=lambda x: x[1], reverse=True)

sorted_dictionary = {}
for i in sort_demo:
	sorted_dictionary[i[0]] = i[1]


#create a new directory to store the results//////////if its existing already then its alright
try:
	os.mkdir('./Hashtags_Tweets_Counts')
except:
	shutil.rmtree('./Hashtags_Tweets_Counts', ignore_errors=True)
	os.mkdir('./Hashtags_Tweets_Counts')



with gzip.open('./Hashtags_Tweets_Counts/Sorted_Dictionary.gz', 'wb') as f3:
	#fout.write(json.dumps(data).encode('utf-8'))
	f3.write(json.dumps(sorted_dictionary).encode('utf-8'))
f3.close()
print("<./Hashtags_Tweets_Counts/Sorted_Dictionary.gz>:::::Written")

print("Elapsed Time")
print("--- %s seconds ---" % (time.time() - start_time))


