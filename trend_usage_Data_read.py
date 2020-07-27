#/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/hashtag_Usage_Info(3months)

import gzip
import json
import glob
import itertools
from pandas import DataFrame
import matplotlib.pyplot as plt
import ntpath
import time
import os
import shutil

def Calc_Top_Trends_Func(surge_dict, top_t):

	t = sorted(surge_dict.items(), key = lambda x: x[1], reverse = True)
	
	dict_top_surges = {}
	counter_flag=0
	
	for i in t:
		dict_top_surges[i[0]]=''
		counter_flag = counter_flag + 1

		if counter_flag==top_t:
			return dict_top_surges

	return dict_top_surges


def calculateSurgeAndTopTrends(prev, curr, usage_thresH, top_t):

	surge_all = {}
	for T in curr.keys():
		if T in prev.keys():
			t_0 = prev[T]
			t_1 = curr[T]

			if t_1>usage_thresH:
				if t_0==0:
					surge_all[T] = t_1
				else:
					surge_all[T] = t_1/t_0

	temp_return = Calc_Top_Trends_Func(surge_all, top_t)
	return temp_return


def extractUsage_current_stamp(dict_trends):
	current_stamp = {}

	for t in dict_trends.keys():
		current_stamp[t] = len(dict_trends[t])

	return current_stamp


if __name__== "__main__":
	start_time = time.time()
	###########################################################
	#Path to directory containing files
	path_hashtagsDemo = "/Users/WaleedAhmed/Documents/THESIS_DS_CODE/June++/dataReadCode_2/hashtag_Usage_Info(3months)/*.gz"
	#Path String
	list_of_files = sorted(glob.glob(path_hashtagsDemo))
	print("Total Files: ", len(list_of_files))

	#F = list_of_files[1]
	details_top_trends_complete = {}

	file_counter_temp = 1

	#threshold of usage in 15 minutes with number of promoters
	usage_threshold = 5
	#how many top trends to pick in the 15 minutes interval 
	top_trends  = 10
	
	

	stamps_top_trends_dictionary = {}

	file_counter = 1
	
	for F in list_of_files:

		with gzip.open(F, 'rt') as f:
			usageInfo = f.read()
		f.close()
		print("File Number: ", file_counter)
		print("Name: ", ntpath.basename(F))
		file_counter = file_counter + 1
	

		usage_info_list = usageInfo.split("\n")
		total_stamps = len(usage_info_list)-1
		
		

		prev_temp = usage_info_list[0].split("\t")
		temp_time_st = prev_temp[0]
		temp_topics_Usage = json.loads(prev_temp[1])
		
		
		previous_stamp = {}
		#receives a dictionary
		previous_stamp = extractUsage_current_stamp(temp_topics_Usage)
		current_stamp = {}
		
		#per_file
		for s in range(1, total_stamps):
			temp = usage_info_list[s].split("\t")
			time_st = temp[0]
			topics_Usage = json.loads(temp[1])
			
			#dictionary with stamp as key and usage as a value dictionary
			current_stamp = extractUsage_current_stamp(topics_Usage)
			#returns a dictionary of top 10 trends until this time stamp {key:''}
			return_value_top_10 = calculateSurgeAndTopTrends(previous_stamp, current_stamp, usage_threshold, top_trends)
			#if type(return_value_top_10) is not None:
			details_top_trends_complete.update(return_value_top_10)
			#updating the previous stamp
			previous_stamp = current_stamp
		
	#print(details_top_trends_complete)
	print(len(details_top_trends_complete))


	gend_link = './Demographics_Percentages/Gender_Percentage_User_Demographics.gz'

	race_link = './Demographics_Percentages/Race_Percentage_User_Demographics.gz'

	age_link = './Demographics_Percentages/Age_Percentage_User_Demographics.gz'

	with gzip.open(gend_link, 'rt') as g:
		gend_temp = g.read()
	g.close()

	gend_perc_dict = json.loads(gend_temp)
	
	with gzip.open(race_link, 'rt') as r:
		race_temp = r.read()
	r.close()

	race_perc_dict = json.loads(race_temp)
	
	with gzip.open(age_link, 'rt') as a:
		age_temp = a.read()
	a.close()

	age_perc_dict = json.loads(age_temp)


	GEND_top_Per_TimeStamp = {}
	RACE_top_Per_TimeStamp = {}
	AGE_top_Per_TimeStamp = {}


	for trend in details_top_trends_complete.keys():
		if trend in gend_perc_dict:
			GEND_top_Per_TimeStamp[trend] = gend_perc_dict[trend]
			RACE_top_Per_TimeStamp[trend] = race_perc_dict[trend]
			AGE_top_Per_TimeStamp[trend] = age_perc_dict[trend]

	try:
		os.mkdir('./Usage_Trend_15Min')
	except:
		shutil.rmtree('./Usage_Trend_15Min', ignore_errors=True)
		os.mkdir('./Usage_Trend_15Min')
	
	path_15_min_gen = './Usage_Trend_15Min/Gender_Trending.gz'
	path_15_min_race = './Usage_Trend_15Min/Race_Trending.gz'
	path_15_min_age = './Usage_Trend_15Min/Age_Trending.gz'

	with gzip.open(path_15_min_gen, 'wb') as f1:
		f1.write(json.dumps(GEND_top_Per_TimeStamp).encode('utf-8'))
	f1.close()
	print("<./Usage_Trend_15Min/Gender_Trending.gz>:::::Written")
	
	with gzip.open(path_15_min_race, 'wb') as f2:
		f2.write(json.dumps(RACE_top_Per_TimeStamp).encode('utf-8'))
	f2.close()
	print("<./Usage_Trend_15Min/Race_Trending.gz>:::::Written")
	
	with gzip.open(path_15_min_age, 'wb') as f3:
		f3.write(json.dumps(AGE_top_Per_TimeStamp).encode('utf-8'))
	f3.close()
	print("<./Usage_Trend_15Min/Age_Trending.gz>:::::Written")


	print("Elapsed Time")
	print("--- %s seconds ---" % (time.time() - start_time))

