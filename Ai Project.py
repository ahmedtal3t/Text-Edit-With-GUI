from  tkinter import filedialog

import nltk
from nltk import PorterStemmer
stemmer=PorterStemmer()

from nltk.tokenize import LineTokenizer, SpaceTokenizer, TweetTokenizer
from nltk import word_tokenize


from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Home")
root.geometry("925x500+300+200")
root.configure(bg="light blue")

img=PhotoImage(file="C:/Users/master/OneDrive/Desktop/login.png")
Label(root,image=img,bg="light blue").place(x=50,y=50)



class m:
    
    def open_File(self):
        self.filepath = filedialog.askopenfilename(initialdir="/gui/text/", title="Select a Text File")
        file = open(self.filepath, "r")
        print(file.read())
        file.close()


    def view_text(self):
        input_file = open(self.filepath, "r")
        x = input_file.read()
        z = open("C:/Users/master/OneDrive/Desktop/View Text.txt","w")
        print(z.write(x))


    def count_text(self):
        input_file = open(self.filepath, "r")
        word_count = {}
        for line in input_file:
            words = line.split()
            for word in words:
                word = word.lower()
                if not word in word_count:
                    word_count[word] = 1
                else:
                   word_count[word] += 1
        r = open(self.filepath, "r")
        x = r.read()
        total = "The total words in text is:", len(x.split())        
        z = open("C:/Users/master/OneDrive/Desktop/Word Count.txt","w")
        print(z.write(str(word_count)),z.write("\n"))
        print(z.write(str(total)))
    
    
        
    def cleaning_spaces(self):
       input_file = open(self.filepath, "r")
       x = input_file.read()
       cleaned_string = " ".join(x.split())
       y = cleaned_string
       z = open("C:/Users/master/OneDrive/Desktop/cleaning spaces.txt","w")
       print(z.write(y))



    def lower_case(self):
        input_file = open(self.filepath, "r")
        x = input_file.read()
        y = x.lower()
        z = open("C:/Users/master/OneDrive/Desktop/lower.txt","w")
        print(z.write(y))



    def upper_case(self):
       input_file = open(self.filepath, "r")
       x = input_file.read()
       y = x.upper()
       z = open("C:/Users/master/OneDrive/Desktop/upper.txt","w")
       print(z.write(y))
        
        
        
    def stemming(self):
        input_file = open(self.filepath, "r")
        words = input_file.read()
        s = words.split()
        z = open("C:/Users/master/OneDrive/Desktop/stemming.txt","w")
        for word in s:
            print(z.write(stemmer.stem(word)), z.write(" "))
        
            
           
            
    def tokenize(self):
       input_file = open(self.filepath, "r")
       x = input_file.read()
       
       z = open("C:/Users/master/OneDrive/Desktop/tokenization.txt","w")
       
       lTokenizer = LineTokenizer()
       print(z.write("Line tokenize output:"))
       print(z.write(str((lTokenizer.tokenize(x)))))
       
       sTokenizer = SpaceTokenizer()
       print(z.write("\nSpace tokenizer output:"))
       print(z.write(str(sTokenizer.tokenize(x))))
       
       tTokenize = TweetTokenizer()
       print(z.write("\nTweet tokenizer output:"))
       print(z.write(str(tTokenize.tokenize(x))))
       
       
    def remove_punctuation(self):
       input_file = open(self.filepath, "r")
       x = input_file.read()
       z = open("C:/Users/master/OneDrive/Desktop/Remove punctuation.txt","w")
       tokenizer = nltk.RegexpTokenizer(r"\w+")
       y = tokenizer.tokenize(x)
       for word in y:
           print(z.write(word))
           print(z.write(" "))

x = m()    



btn0 = Button(root,command=x.open_File, text="Open File", width=17,pady=7, height=1, font=5, bg="teal", fg="black",border=0).place(x=580,y=80)
btn1 = Button(root,command=x.view_text, text="View Text", width=17,pady=7, height=1, font=5, bg="teal", fg="black",border=0).place(x=480,y=150)
btn2 = Button(root,command=x.count_text, text="Count Text", width=17,pady=7, height=1, font=5, bg="teal", fg="black",border=0).place(x=480,y=220)
btn3 = Button(root,command=x.cleaning_spaces, text="Cleaning Spaces", width=17,pady=7, height=1, font=5, bg="teal", fg="black",border=0).place(x=480,y=290)
btn4 = Button(root,command=x.lower_case, text="Lower Case", width=17,pady=7, height=1, font=5, bg="teal", fg="black",border=0).place(x=480,y=360)
btn5 = Button(root,command=x.upper_case, text="Upper Case", width=17,pady=7, height=1, font=5, bg="teal", fg="black",border=0).place(x=700,y=150)
btn6 = Button(root,command=x.stemming, text="Stemming", width=17,pady=7, height=1, font=5, bg="teal", fg="black",border=0).place(x=700,y=220)
btn7 = Button(root,command=x.tokenize, text="Tokenize", width=17,pady=7, height=1, font=5, bg="teal", fg="black",border=0).place(x=700,y=290)
btn8 = Button(root,command=x.remove_punctuation, text="Remove Punctuation", width=17,pady=7, height=1, font=5, bg="teal", fg="black",border=0).place(x=700,y=360)




root.mainloop()