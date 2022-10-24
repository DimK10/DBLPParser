import csv
import json
from collections import Counter

def changeData():
    dblp_path = 'dataset/dblp.xml'
    load_path = './dataset/article.csv'
    save_path = './dataset/article_2.json'
   

    print("Cahnging data to json format for graph...")


    # Opening JSON file
    f = open(load_path, encoding="utf8")
    
    # returns JSON object as 
    # a dictionary
    data = list(csv.reader(f))

    flat_data = [item for sublist in data for item in sublist]

    # remove empty strings
    final_data = [i for i in flat_data if i]

    dict_of_counts = Counter(final_data);

    # remove year word
    del dict_of_counts['year']

    sort_by_key = dict(sorted(dict_of_counts.items(),key=lambda item:item[0]))
   
    # Closing file
    f.close()

    f2 = open(save_path, 'w')
    json.dump(sort_by_key, f2)
    f2.close

def main():
    changeData();



if __name__ == '__main__':
    main()