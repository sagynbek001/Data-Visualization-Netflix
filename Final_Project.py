'''
Team Members:
    ChaeMin Kim : ck3119
    Kateryna Yesieva : ky1143
    Sagynbek Talgatuly : st4121
    
Course: CADT-UH 1013Q
Description: Final project for the course
Date: 07/08/2021
'''

#Final_Project: Data analysis of the Netflix movies

#importing necessary modules
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def start_analysis(data):
    #starting to analyze the data using basic pandas methods
    print("--> The initial fields of the table:\n")
    print(data.head(), end = "\n\n")
    print("--> The sizes of the data is:", str(data.shape), end = "\n\n")
    print("--> Main info about the data:\n")
    print(data.info(), end = "\n\n")
    print("--> Data description:\n")
    print(data.describe(), end = "\n\n")

def find_the_counts(data):
    #finding the occurences of the given genres
    d1 = len(data[data['Genre'] == 'Documentary'])
    d2 = len(data[data['Genre'] == 'Drama'])
    d3 = len(data[data['Genre'] == 'Comedy'])
    d4 = len(data[data['Genre'] == 'Romantic comedy'])
    d5 = len(data[data['Genre'] == 'Thriller'])
    #d6 is the number that corresponds to the rest of the movies
    d6 = len(data) - (d1+d2+d3+d4+d5)
    counts = [d1,d2,d3,d4,d5,d6]
    return counts

def main():
    
    #reading the csv file into variable called data
    data = pd.read_csv("NetflixOriginals.csv", encoding='Windows-1252')
                       
    start_analysis(data)
    
    scores_g_than_eight = data[data['IMDB Score']>=8]
    
    #section1
    #plotting a bar chart of the most liked movies grouped by genre
    plt.figure(figsize = (15,15))
    g = sns.barplot(x = 'Title', y = 'IMDB Score', hue ='Genre', data = scores_g_than_eight)
    g.set_xticklabels(g.get_xticklabels(), rotation=90)
    plt.show()
    plt.savefig("Section1.png")
    print("The figure for section1 was saved!")
    plt.clf()

    #section2
    #plotting a bar chart of the most liked movies grouped by language
    plt.figure(figsize = (20,15))
    g = sns.barplot(x = 'IMDB Score', y = 'Title', hue ='Language', data = scores_g_than_eight)
    plt.show()
    plt.savefig("Section2.png")
    print("The figure for section2 was saved!")
    plt.clf()

    #section3
    #plotting a bar chart of the movies grouped by the language
    data["Language"].value_counts().plot(kind="bar", color="red", figsize=(15,10))
    plt.show()
    plt.savefig("Section3.png")
    print("The figure for section3 was saved!")
    plt.clf()
    
    #section4
    #plotting a pie chart of all the genres
    data['Genre'].value_counts().plot(kind = 'pie')
    plt.show()
    plt.savefig("Section4_All.png")
    print("The figure for section4 was saved!")
    plt.clf()
    #plotting only the most significant ones
    genres = ['Documentary', 'Drama', 'Comedy',
        'Romantic comedy', 'Thriller', 'Others']
    counts = find_the_counts(data)
    fig = plt.figure(figsize =(10, 7))
    plt.pie(counts, labels = genres, autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
    plt.savefig("Section4_Others.png")
    print("The figure for section4 was saved!")
    plt.clf()
    
main()


