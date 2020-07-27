import time
start_time = time.time()
import os





demo_data_Read = os.system("python demo_data_Read.py")
print("\n<<< demo_data_Read.py >>> ran with exit code %d \n" %demo_data_Read)

demo_percentages = os.system("python demo_percentages.py")
print("\n<<< demo_percentages.py >>> ran with exit code %d \n" %demo_percentages)

demo_Tweet_counter = os.system("python demo_Tweet_counter.py")
print("\n<<< demo_data_Read.py >>> ran with exit code %d \n" %demo_Tweet_counter)

demo_kmean_clus = os.system("python demo_kmean_clus.py")
print("\n<<< demo_data_Read.py >>> ran with exit code %d \n" %demo_kmean_clus)

###########15 minute timestamp trend calclations#############
trend_usage_Data_read = os.system("python trend_usage_Data_read.py")
print("\n<<< trend_usage_Data_read.py >>> ran with exit code %d \n" %trend_usage_Data_read)

trend_usage_kmeans_15mins_clus = os.system("python trend_usage_kmeans_15mins_clus.py")
print("\n<<< trend_usage_kmeans_15mins_clus.py >>> ran with exit code %d \n" %trend_usage_kmeans_15mins_clus)

print("\nEntire Module Ran Successfully: ")
print("#################################\n")

print("\nTotal Elapsed Time")
print("--- %s seconds ---\n" % (time.time() - start_time))
