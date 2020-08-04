Part(1): Supervised by Dr. Abhijnan Chakraborty (MPI-SWS, Saarbrücken, Germany)

Optimum Number of Clusters were determined by running the code in the following repository:

https://github.com/waleedahmed90/Optimum-Clusters-Elbow-method

The optimum number of clusters come out to be the following:
Gender = 4
Race = 5
Age = 5

Running "python driver.py" will result in the following execution order


#################################<Execution Order>######################


1) demo_data_Read.py
INPUT FOLDER################: [Hashtag_Demographics(3months)]
OUTPUT FOLDER###############: [Demographics_Count]

2) demo_percentages.py
INPUT FOLDER################: [Demographics_Count]
OUTPUT FOLDER###############: [Demographics_Percentages]

3) demo_Tweet_counter.py
INPUT FOLDER################: [Demographics_Count]
OUTPUT FOLDER###############: [Hashtags_Tweets_Counts]

4) demo_kmean_clus.py
INPUT FOLDER################: [Demographics_Percentages], [Hashtags_Tweets_Counts]
OUTPUT FOLDER###############: [Clusters_Demographics]

5) trend_usage_Data_read.py
INPUT FOLDER################: [hashtag_Usage_Info(3months)], [Demographics_Percentages]
OUTPUT FOLDER###############: [Usage_Trend_15Min]

6) trend_usage_kmeans_15mins_clus.py
INPUT FOLDER################: [Usage_Trend_15Min], [Hashtags_Tweets_Counts]
OUTPUT FOLDER###############: [Clusters_TrendUsage_Demographics]



####################:::INPUT DATASETS::#######################
1) [Hashtag_Demographics(3months)]#####################(92 Files)
2) [hashtag_Usage_Info(3months)]#######################(92 Files)

These two datasets are a property of Max Planck Institute for Software Systems (Saarbrücken) and are available on request
Write at waleed.wsd@gmail.com





#######################::OUTPUTS::############################
The successful execution will result in the following folders

1) [Demographics_Count]#############################(3 File(s))
2) [Demographics_Percentages]#######################(3 File(s))
3) [Hashtags_Tweets_Counts]#########################(1 File(s))
4) [Clusters_Demographics]##########################(3 File(s))
5) [Usage_Trend_15Min]##############################(3 File(s))
6) [Clusters_TrendUsage_Demographics]###############(3 File(s))



######################################################################################

<<<<Author: Waleed Ahmed, Date: (July 27, 2020), (Saarbrücken, Deutschland)>>>>
