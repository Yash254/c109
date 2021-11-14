import random
from types import resolve_bases
import plotly.express as px
import plotly.figure_factory as ff
import statistics

diceResult=[]
count=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceResult.append(dice1+dice2)
mean=sum(diceResult)/len(diceResult)
print(mean)
std=statistics.stdev(diceResult)
print(std)
median=statistics.median(diceResult)
print(median)
mode=statistics.mode(diceResult)
print(mode)
fig=ff.create_distplot([diceResult],["Result"],show_hist=False)
fig.show()

firststdstart,firsststdend=mean-std,mean+std
secondstdstart,secondstdend=mean-(2*std),mean+(2*std)
thirdstdstart,thirdstdend=mean-(3*std),mean+(3*std)
list1std=[result for result in diceResult if result>firststdstart and result<firsststdend]
list2std=[result for result in diceResult if result>secondstdstart and result<secondstdend]
list3std=[result for result in diceResult if result>thirdstdstart and result<thirdstdend]
print("{}% of data lies with in firststd".format(len(list1std)*100.0/len(diceResult)))
print("{}% of data lies with in secondstd".format(len(list2std)*100.0/len(diceResult)))
print("{}% of data lies with in thirdstd".format(len(list3std)*100.0/len(diceResult)))