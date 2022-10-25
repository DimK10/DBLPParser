# DBLP Dataset Parser for Publications Per Year Bar Graph

This code demonstrates a bar graph by parsing dblp.xml and producing a simple bar graph that shows article publications per year, as an exercise. The author of the parser is [Zhang Hao](https://github.com/IsaacChanghau). I added only the change_data.py, and make_bar_graph.py, in order to show the graph needed for my use case.
<br/>

The process i followed was the following:
 - Use the dblp_parser.py to generate a csv file for the article type and year feature, then use the change_data.py to generate a new file of type json, by counting from the csv file all duplicate year values and making a dictionary out of it that then is written is json format.
 - Load that json file to a bar graph by using the matplotlib library. The json file can also be used for making graphs using other technologies (such as js chart libraries).

original repo readme:

# DBLP Dataset Parser 

![Authour](https://img.shields.io/badge/Author-Zhang%20Hao%20(Isaac%20Changhau)-blue.svg) ![Python](https://img.shields.io/badge/Python-3.6.5-brightgreen.svg)

It is a python parser for [DBLP dataset](https://dblp.uni-trier.de/), the XML format dumped file can be downloaded [here](http://dblp.org/xml/) from [DBLP Homepage](https://dblp.org/).

This parser requires `dtd` file, so make sure you have both `dblp-XXX.xml` (dataset) and `dblp-XXX.dtd` files. Note that you also should guarantee that both `xml` and `dtd` files are in the same directory, and the name of `dtd` file shoud same as the name given in the `<!DOCTYPE>` tag of the `xml` file. Such information can be easily accessed through `head dblp-XXX.xml` command. As shown below
```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE dblp SYSTEM "dblp-2017-08-29.dtd">
<dblp>
<phdthesis mdate="2016-05-04" key="phd/dk/Heine2010">
<author>Carmen Heine</author>
<title>Modell zur Produktion von Online-Hilfen.</title>
...
```

A sample to use the parser:
```python
def main():
    dblp_path = 'dataset/dblp.xml'
    save_path = 'article.json'
    try:
        context_iter(dblp_path)
        log_msg("LOG: Successfully loaded \"{}\".".format(dblp_path))
    except IOError:
        log_msg("ERROR: Failed to load file \"{}\". Please check your XML and DTD files.".format(dblp_path))
        exit()
    parse_article(dblp_path, save_path, save_to_csv=False)  # default save as json format
```

Some extracted results:

**Count the number of all different type of publications**:
![general](/img/general.png)

**Count the number of all different attributes among all publications**:
![all_feature](/img/all_feature.png)

**Count the number of five different features of articles**:
![article_feature](/img/article_feature.png)

**Distribution of published year of articles**:
![article_year](/img/article_year.png)
