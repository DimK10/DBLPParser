import csv
import json
from collections import Counter

def main():
    dblp_path = 'dataset/dblp.xml'
    load_path = './dataset/article.csv'
    save_path = './dataset/article_2.csv'
   

    # Opening JSON file
    f = open(load_path, encoding="utf8")
    
    # returns JSON object as 
    # a dictionary
    data = list(csv.reader(f))

    flat_data = [item for sublist in data for item in sublist]

    # remove empty strings
    final_data = [i for i in flat_data if i]

    dict_of_counts = Counter(final_data);
   
    # Closing file
    f.close()

    f2 = open(save_path, 'w')
    json.dump(dict_of_counts, f2)
    f2.close



if __name__ == '__main__':
    main()