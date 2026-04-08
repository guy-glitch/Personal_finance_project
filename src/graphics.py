#graphs and graphics

import matplotlib.pyplot as plt, tkinter

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
class Menu:
    #create function init, get options'
    def __init__(self,options):
        #create window with boxes for every option
        self.options=options

    #create function use
    def use(self):
        #show window
        root=tkinter.Tk()
        root.title('Personal Finance')
        root.configure(background='black')
        root.minsize(500,500)
        root.maxsize(1000,1000)
        root.geometry('700x700+1300+500')
        #return option clicked
        def push(name):
            self.out=self.buttons[name].cget('name')
            root.destroy()
        '''def push(name):
            root.out=name
            root.destroy()'''
        #check for box click
        buttons=[]
        for i,v in enumerate(self.options):
            buttons.append(tkinter.Button(root,text=v,command=lambda: push(i)))
            #buttons.append(tkinter.Button(root,text=v,command=lambda name=v: push(name)))
        for v,i in enumerate(buttons):
            i.pack()
            i.place(x=100,y=700/len(self.options)*(v+0.42))
        root.mainloop()
        return self.out
        

#create function inputs, get question and wrong
def inputs(question,wrong=False):
    #create window, show question and text box
    root=tkinter.Tk()
    root.title('Personal Finance')
    root.configure(background='black')
    root.minsize(500,500)
    root.maxsize(1000,1000)
    root.geometry('700x700+1300+500')
    out=tkinter.StringVar()
    enter=tkinter.Entry(root,width=50,textvariable=out)
    enter.pack()
    enter.place(x=200,y=350)
    q=tkinter.Label(root,text=question)
    q.pack()
    q.place(x=250,y=300)
    #return text box entry
    def end():
        root.destroy()
    #if wrong is true, also show invalid input, try again
    if wrong:
        error=tkinter.Label(root,text='Invalid input. Try again.')
        error.pack()
        error.place(x=270,y=250)
    button=tkinter.Button(root,text='Enter',command=end)
    button.pack()
    button.place(x=300,y=370)
    root.mainloop()
    return out.get()

#create function show, get stuff
def show(stuff):
    #create window and display stuff
    root=tkinter.Tk()
    root.title('Personal Finance')
    root.configure(background='black')
    root.minsize(500,500)
    root.maxsize(1000,1000)
    root.geometry('700x700+1300+500')
    tkinter.Message(root,text=stuff,width=700)
    def end():
        root.destroy()
    button=tkinter.Button(root,text='Continue',command=end)
    button.pack()
    button.place(x=300,y=500)
    root.mainloop()

#need to test everything except inputs