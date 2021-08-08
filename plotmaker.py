import os
print('\n')
print("Checking If packages are installed or not")
try:
    import matplotlib.pyplot as plt
    import pandas as pd
    from pyautogui import prompt,confirm
except ImportError:
    packages_ask = input('''Packages Not Found.
    Would you like to install them? (y/n)''')

    if packages_ask == 'y':
        # PACKAGES INSTALLATION PROCESS BEGIN
        print("Installing packages .......")
        os.system('figlet "MATPLOTLIB" ')
        os.system('pip install  matplotlib')
        print("matplotlib installed")
        os.system('figlet "PANDAS" ')
        os.system('pip install pandas')
        print("pandas installed")
        os.system('figlet "PYAUTOGUI" ')
        os.system('pip install pyautogui')
        print("pyautogui installed")
        print("Packages installed :)")
        # PACKAGES INSTALLAYTION PROCESS END
        # RE-CHECKING IF PACKAGES ARE INSTALLED OR NOT
        print("Checking If packages are installed or not")
        try:
            import matplotlib.pyplot as plt
            import pandas as pd
            from pyautogui import prompt,confirm
        # IF ERROR IS RAISED, THEN RE-CHECK PACKAGES
        except ImportError:
            print("Sorry some error  occured while installing Packages \n Try installing manually")
            print("Exiting")
            exit()
# IF ANSWER IS NO THEN EXIT
    else:
        print("IF YOU WANT TO RUN THE PROGRAM \n YOU SHOULD HAVE PACKAGES INSTALLED PLEASE RELAUNCH THIS PROGRAM TO INSTALL PACKAGES OR INSTALL IT MANUALLY")
        exit()
# clear screen 
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    # clear screen
clear_screen()
# start
print("Welcome To ")
print("\n")
print("\n")
print('''     _         _          ____  _       _     __  __       _             
   / \  _   _| |_ ___   |  _ \| | ___ | |_  |  \/  | __ _| | _____ _ __ 
  / _ \| | | | __/ _ \  | |_) | |/ _ \| __| | |\/| |/ _` | |/ / _ \ '__|
 / ___ \ |_| | || (_) | |  __/| | (_) | |_  | |  | | (_| |   <  __/ |   
/_/   \_\__,_|\__\___/  |_|   |_|\___/ \__| |_|  |_|\__,_|_|\_\___|_|   
                                                                        
    _              _   ____               _ _      _             
   / \   _ __   __| | |  _ \ _ __ ___  __| (_) ___| |_ ___  _ __ 
  / _ \ | '_ \ / _` | | |_) | '__/ _ \/ _` | |/ __| __/ _ \| '__|
 / ___ \| | | | (_| | |  __/| | |  __/ (_| | | (__| || (_) | |   
/_/   \_\_| |_|\__,_| |_|   |_|  \___|\__,_|_|\___|\__\___/|_|   
                 Developed By: Binayak Jha 
(note: still in development you can also contribute in this project by adding new features and giving your feedback)
''')

print('starting .....')
print('\n')

data_input = prompt(text = 'Please keep your csv file path here (note: give full path or ' , title = 'File path')
df = pd.read_csv(data_input)
X = prompt(text = 'please enter the data table heading which you want to show in x axis ', title= 'X axis')
y = prompt(text = 'please enter the data table heading which you want to show in y axis ' ,title = 'Y axis')
x_label = prompt(text = 'please enter the data table heading which you want to show in x axis ', title = 'X axis heading')
y_label = prompt(text = 'please enter the data table heading which you want to show in y axis ', title = 'Y axis heading')
heading = prompt(text = 'please enter the data table heading which you want to show in graph ' ,title = 'Heading')
plt.title(heading)
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


save_fig = prompt(text = '''Do you want to save the graph? (y/n)''')
if save_fig == 'y' or save_fig == 'Y' or save_fig == 'yes' or save_fig == 'Yes':
    plt.savefig(prompt(text = 'Please enter the file name  eg (abc.png or abc.jpg)' , title = 'File name'))
    confirm(text = 'Picture saved  in the same folder where I am !! ' , title = 'Show graph')
# after seeing the graph close it to continue
confirm(text = 'Close the graph to continue (You will get to see it at last also)' , title = 'Close graph')
print('Here is the graph  .....')
plt.show() 
print("\n")
print("\n")
print("\n")
os.system('figlet "MATHS"')
print("\n")
print("\n")
def maths():
    print(''' Please select a number from list:
    1) Standard Deviation \t 2) Mean
    3) Variance \t 4) Median
    5) Mode \t 6) Range
    7) Quartile1 \t 8) Quartile3
    \t 9) all  
    
    SELECTING A NUMBER .....
    ''')
    me = prompt(text = ''' Please select a number from list:
    1) Standard Deviation     2) Mean
    3) Variance    4) Median
    5) Mode       6) Range
    7) Quartile1    8) Quartile3
    9) all
    ''', title = 'Select a number from list')
    if me == '1':
        # standard deviation
        std = df[y].std()
        confirm(text = 'Standard deviation of the data is ' + str(std) , title = ' Standard Deviation')
    if me == '2':
        # mean
        mean = df[y].mean()
        confirm(text = 'Mean of the data is ' + str(mean) , title = ' Mean')
    if me == '3':
        # variance
        var = df[y].var()
        confirm(text = 'Variance of the data is ' + str(var) , title = ' Variance')
    if me == '4':
        # median
        median = df[y].median()
        confirm(text = 'Median of the data is ' + str(median) , title = ' Median ')
    if me == '5':
        # mode
        mode = df[y].mode()
        confirm(text = 'Mode of the data is ' + str(mode) , title = ' Mode ')
    if me == '6':
        # range
        range = df[y].max() - df[y].min()
        confirm(text = 'Range of the data is ' + str(range) , title = ' Range ')
    if me == '7':
        # quartile1
        q1 = df[y].quantile(0.25)
        confirm(text = 'Quartile1 of the data is ' + str(q1) , title = ' Quartile 1 ')
    if me == '8':
        # quartile3
        q3 = df[y].quantile(0.75)
        confirm(text = 'Quartile3 of the data is ' + str(q3) , title = ' Quartile 2 ')
    if me == '9':
        # all
        std = df[y].std()
        mean = df[y].mean()
        var = df[y].var()
        median = df[y].median()
        mode = df[y].mode()
        range = df[y].max() - df[y].min()
        q1 = df[y].quantile(0.25)
        q3 = df[y].quantile(0.75)
        confirm(text = 'Standard deviation of the data is ' + str(std) + '\n' + 'Mean of the data is ' + str(mean) + '\n' + 'Variance of the data is ' + str(var) + '\n' + 'Median of the data is as follows \n ' + str(median) + '\n' + 'Mode of the data is ' + str(mode) + '\n' + 'Range of the data is ' + str(range) + '\n' + 'Quartile1 of the data is ' + str(q1) + '\n' + 'Quartile3 of the data is ' + str(q3) , title = ' All ')

ask = prompt(text = 'Do you want to see mean and other things? (y/n) ' , title = 'Continue')
if ask == 'y' or ask == 'Y' or ask == 'yes' or ask == 'Yes':
    maths()
elif ask == 'n' or ask == 'N' or ask == 'no' or ask == 'No':
    pass

#PREDICTION
print("\n")
os.system('figlet "PREDICTION"')
print("\n")
predict_ask = prompt(text = 'Do you want to predict? (y/n) ' , title = 'Continue')
def predicts():
    from sklearn.linear_model import LinearRegression
    model = LinearRegression()
    model.fit(df[[X]], df[[y]])
    # ask a value to predict
    predict_value = prompt(text = 'Please enter a value  of '+str(x_label)+' to predict '+str(y_label) , title = 'Predict')
    predict = model.predict([[predict_value]])
    confirm(text = 'Predicted value of '+ str(y_label)+ ' is ' + str(int(predict)) , title = 'Predict')
if predict_ask == 'y' or predict_ask == 'Y' or predict_ask == 'yes' or predict_ask == 'Yes':
    predicts()
elif predict_ask == 'n' or predict_ask == 'N' or predict_ask == 'no' or predict_ask == 'No':
    prompt(text = 'Thank you for using this program')
    print("\n")

print('Graph ....')
plt.show() 
os.system('figlet "END"')
print("\n")
