import matplotlib.pyplot as plt
import json

def makeBarGraph():

    print("Creating Bar graph...")
    file_to_open = 'dataset/article_2.json'

    dictionary = json.load(open(file_to_open, 'r'))
    yAxis = [key for key, value in dictionary.items()]
    xAxis = [value for key, value in dictionary.items()]
    # plt.grid(True)

    ## BAR GRAPH ##

    # params = {'figure.figsize'  : (50, 40),
    #       'axes.labelsize'  : 30,
    #       'axes.titlesize'  : 30,
    #       'xtick.labelsize' : 20,
    #       'ytick.labelsize' : 20}
    # plt.rcParams.update(params)

    plt.rc('font', size=8) 

    fig = plt.figure()
    plt.barh(yAxis,xAxis)
    plt.bar(xAxis,yAxis, color='maroon')
    plt.xlabel('Publications')
    plt.ylabel('Year')

    plt.show()

def main():
    makeBarGraph()
    


if __name__ == '__main__':
    main()