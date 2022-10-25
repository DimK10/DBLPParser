import matplotlib.pyplot as plt
import json

def makeBarGraph():

    print("Creating Bar graph...")
    file_to_open = 'dataset/article_2.json'

    dictionary = json.load(open(file_to_open, 'r'))
    yAxis = [key for key, value in dictionary.items()]
    xAxis = [value for key, value in dictionary.items()]

    ## BAR GRAPH ##

    plt.rc('font', size=8) 

    fig = plt.figure()
    fig.canvas.manager.set_window_title('Number of Publications Per Year from DBLP')
    plt.barh(yAxis,xAxis)
    plt.bar(xAxis,yAxis, color='maroon')
    plt.xlabel('Publications')
    plt.ylabel('Year')

    plt.show()

def main():
    makeBarGraph()
    


if __name__ == '__main__':
    main()