import random
import statistics
import pandas as pd

df=pd.read_csv("StudentsPerformance.csv")
data=df["math score"].tolist()

mean=sum(data)/len(data)
median=statistics.median(data)
mode=statistics.mode(data)
std_dev=statistics.stdev(data)
print(mean)
print(median)
print(mode)
print(std_dev)

first_std_dev_start, first_std_dev_end = mean-std_dev, mean+std_dev
sec_std_dev_start, sec_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
thi_std_dev_start, thi_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)
list_of_data_within_1_std_dev=[result for result in data if result > first_std_dev_start and result < first_std_dev_end]
list_of_data_within_2_std_dev=[result for result in data if result > sec_std_dev_start and result < sec_std_dev_end]
list_of_data_within_3_std_dev=[result for result in data if result > thi_std_dev_start and result < thi_std_dev_end]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_dev)*100.0/len(data)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_dev)*100.0/len(data)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_dev)*100.0/len(data)))