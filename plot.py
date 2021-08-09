import pandas as pd
import matplotlib.pyplot as plt
from pyautogui import prompt, alert, confirm
def plot(df,X,y,x_label,y_label,heading):
# print(find_files("canada_predicted_csv.csv","/")[0])   
    type_graph = prompt(text = '''Please enter the type of graph you want to show:
    1) Plot     
    2) Scatter plot
    3) Histogram
    4) Box plot
    5) Pie chart
    6) Bar chart
    7) Area plot
    (enter a number)   ''',title = 'Graph type')
    if type_graph == '1':
        # want to add a marker in your plot?
        marker = prompt(text = '''Do you want to add a marker in your plot? (y/n)''', title = 'Marker')
        if marker == 'y' or marker == 'Y' or marker == 'yes' or marker == 'Yes':
            marker_input = prompt(text = 'Please enter the marker you want to add ' , title = 'Marker')
            plt.plot(df[X],df[y],marker = marker_input)
        else:
            plt.plot(df[X],df[y])
        plt.xlabel(x_label)
        plt.ylabel(y_label)

    elif type_graph == '2':
        plt.scatter(df[X], df[y])
        plt.xlabel(x_label)
        plt.ylabel(y_label)

    elif type_graph == '3':
        plt.hist(df[y])
        plt.xlabel(x_label)
        plt.ylabel(y_label)

    elif type_graph == '4':
        plt.boxplot(df[y])
        plt.xlabel(x_label)
        plt.ylabel(y_label)

    elif type_graph == '5':
        plt.pie(df[y], labels = df[X])

    elif type_graph == '6':
        # fwhat bar graph horizontally or vertically    
        ask2 = prompt(text = '''Do you want to show bar graph horizontally or vertically?
    1) Horizontal
    2) Vertical
    (enter a number)   ''',title = 'Horizontal or vertical')
        if ask2 == '1':
            plt.barh(df[X], df[y])
            plt.xlabel(x_label)
            plt.ylabel(y_label)
        elif ask2 == '2':
            plt.bar(df[X], df[y])
            plt.xlabel(x_label)
            plt.ylabel(y_label)

    elif type_graph == '7':
        plt.plot(df[X], df[y])
        plt.xlabel(x_label)
        plt.ylabel(y_label)
    # after seeing the graph close it to continue
    save_fig = prompt(text = '''Do you want to save the graph? (y/n)''')
    if save_fig == 'y' or save_fig == 'Y' or save_fig == 'yes' or save_fig == 'Yes':
        plt.savefig(prompt(text = 'Please enter the file name  eg (abc.png or abc.jpg)' , title = 'File name'))
        confirm(text = 'Picture saved  in the same folder where I am !! ' , title = 'Show graph')
    print('Here is the graph  .....')
    plt.show() 