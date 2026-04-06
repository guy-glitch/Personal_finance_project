#graphs and graphics

import matplotlib.pyplot as plt

#create class pie,
class Pie:
#   create function init,  get caption and values dictionary]
    def __init__(self,caption,values):
        #save pie chart with caption caption and names keys in values, portions values in values
        self.caption=caption
        self.values=values

    #create function update, get values dictionary
    def update(self,values):
        #Update saved chart to include values
        self.values|=values
    
    #create function show
    def show(self):
        #show saved graph
        fig,ax=plt.subplots(1,2)
        ax[0].pie(self.values.values(),labels=self.values.keys(),autopct='%1.1f%%')
        ax[0].set_title(self.caption)
        plt.show()


#create class Line
class Line:
#   create function init, get plus, minus dictionaries
    def __init__(self,plus,minus,y,capt):
        #plot and save line graph with plus line, minus line, and them combined line
        self.plus=plus
        self.minus-minus
        self.y=y
        self.capt=capt

    #create function update, get plus, minus dictionaries
    def update(self,plus,minus):
        #update saved graph
        self.plus|=plus
        self.minus|=minus
    
    #create functon show
    def show(self):
        #show saved graph
        plt.plot(list(self.plus.values()),color='g')
        plt.plot(list(self.minus.values()),color='r')
        plt.ylabel(self.y)
        plt.title(self.capt)
        all={}
        for i in self.plus:
            all[i]=self.plus[i]+self.minus[i]
        plt.plot(list(all.values()),color='b')
        plt.show()


#create class bars
class Bars:
#   craete function init, get values
    def __init__(self,values,y,capt):
        #create bar chart with name values keys and values values values
        self.values=values
        self.y=y
        self.capt=capt

    #create function update, get values
    def update(self,values):
        #update saved chart
        self.values|=values

    #create function show
    def show(self):
        #show saved chart
        plt.bar(self.values.keys(),self.values.values())
        plt.ylabel(self.y)
        plt.title(self.capt)
        plt.show()


#create class menu
    #create function init, get options
        #create window with boxes for every option

    #create function use
        #show window
        #check for box click
        #return option clicked


#create function inputs, get question and wrong
    #create window, show question and text box
    #if wrong is true, also show invalid input, try again
    #return text box entry

#create function show, get stuff
    #create window and display stuff

