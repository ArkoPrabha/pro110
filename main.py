import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv('data.csv')
data=df['average'].tolist()

def random_set_of_mean(counter):
    data_set=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        data_set.append(value)
    sample_mean=statistics.mean(data_set)
    return(sample_mean)
def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(676)
        mean_list.append(set_of_means)
    mean=statistics.mean(mean_list)
    print('MEAN OF SAMPLING DISTRIBUTION',mean)
    fig=ff.create_distplot([mean_list],['SAMPLE AVERAGE'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1.7],mode='lines',name='MEAN'))
    fig.show()
setup()

def standard_dev():
    mean_list=[]
    for i in range(0,1000):
        set_of_means=random_set_of_mean(676)
        mean_list.append(set_of_means)
    stdev=statistics.stdev(mean_list)
    print('STDEV OF SAMPLING DISTRIBUTTION',stdev)
standard_dev()

