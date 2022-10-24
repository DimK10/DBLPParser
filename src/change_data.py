import csv
import json

def main():
    dblp_path = 'dataset/dblp.xml'
    save_path = 'dataset/article.csv'
   

    # Opening JSON file
    f = open(save_path)
    
    # returns JSON object as 
    # a dictionary
    data = csv.reader(f)

    dict_of_counts = {};
    
    # Iterating through the json
    # list
    for i in data:
        dict_of_counts = {item:data.count(item) for item in data}

    json.dump(dict_of_counts, f)
    # Closing file
    f.close()



if __name__ == '__main__':
    main()
