from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API


class NLPApp:

    def __init__(self):
        # login
        self.db = Database()
        self.apio = API()
        self.root = Tk()
        self.root.title("NLP APP")
        self.root.iconbitmap("Resource/favicon.ico")
        self.root.geometry("300x450")
        self.root.configure(bg='#493387')
        self.login()
        self.root.mainloop()

    def login(self):
        self.clear()
        self.root.geometry("300x450")
        main = Label(self.root, text='NLP App', fg='white', bg="#5834C0")
        main.pack(pady=20, ipadx=15, ipady=10, fill=X)
        main.configure(font="arial 20 italic bold")

        # email
        email_label = Label(self.root, text="Enter Email:", bg='#493387', fg='#DA40D3', font="Helvetica 15 bold")
        email_label.pack(pady=5)

        self.email_entry = Entry(self.root, width=40)
        self.email_entry.pack(pady=8, padx=10, ipady=3)
        self.email_entry.focus()

        # password
        password_label = Label(self.root, text="Enter Password:", bg='#493387', fg='#DA40D3', font="Helvetica 15 bold")
        password_label.pack(padx=10, pady=5)

        self.password_entry = Entry(self.root, width=40, show='*')
        self.password_entry.pack(pady=8, padx=10, ipady=3)
        self.password_entry.focus()

        # Login Button
        login_button = Button(self.root, text="Login", command=self.login_user, borderwidth=10, font="Helvetica 13 bold")
        login_button.pack(ipadx=8, ipady=5, pady=15)

        label3 = Label(self.root, text="Not a Member? ", font="arial 13", bg="#493387", fg='#DA40D3')
        label3.pack()

        redirect_button = Button(self.root, text="Register Now", borderwidth=7, font="Helvetica 13 bold",
                                 command=self.register)
        redirect_button.pack(ipadx=8, pady=10)

    def register(self):
        self.clear()

        # name
        self.root.geometry("300x550")
        main = Label(self.root, text='NLP App', fg='white', bg="#5834C0")
        main.pack(pady=20, ipadx=15, ipady=10, fill=X)
        main.configure(font="arial 20 italic bold")

        # name
        name_label = Label(self.root, text="Enter Name:", bg='#493387', fg='#DA40D3', font="Helvetica 15 bold")
        name_label.pack(pady=5)

        self.name_entry = Entry(self.root, width=40)
        self.name_entry.pack(pady=8, padx=10, ipady=3)
        self.name_entry.focus()

        # email
        email_label = Label(self.root, text="Enter Email:", bg='#493387', fg='#DA40D3', font="Helvetica 15 bold")
        email_label.pack(pady=5)

        self.email_entry = Entry(self.root, width=40)
        self.email_entry.pack(pady=8, padx=10, ipady=3)
        self.email_entry.focus()

        # password
        password_label = Label(self.root, text="Enter Password:", bg='#493387', fg='#DA40D3', font="Helvetica 15 bold")
        password_label.pack(padx=10, pady=5)

        self.password_entry = Entry(self.root, width=40, show='*')
        self.password_entry.pack(pady=8, padx=10, ipady=3)
        self.password_entry.focus()

        # Register Button
        register_button = Button(self.root, text="Register", borderwidth=10, font="Helvetica 13 bold", command=self.user_data)
        register_button.pack(ipadx=8, ipady=5, pady=15)

        label3 = Label(self.root, text="Already a Member? ", font="arial 13", bg="#493387", fg='#DA40D3')
        label3.pack()

        redirect_button = Button(self.root, text="Login Now", borderwidth=7, font="Helvetica 13 bold",
                                 command=self.login)
        redirect_button.pack(ipadx=8, pady=10)

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def user_data(self):
        # fetch data from gui
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        response = self.db.add_data(name, email, password)

        if response:
            messagebox.showinfo("Success", "Registration successful")
        else:
            messagebox.showerror("Error", "Email already exits")

    def login_user(self):

        email = self.email_entry.get()
        password = self.password_entry.get()

        response = self.db.search(email, password)

        if response:
            messagebox.showinfo("Success", "Login Successful")
            self.home_gui()
        else:
            messagebox.showerror("Error", "Incorrect email/password")

    def home_gui(self):
        self.clear()

        main = Label(self.root, text='NLP App', fg='white', bg="#5834C0")
        main.pack(pady=20, ipadx=15, ipady=10, fill=X)
        main.configure(font="arial 20 italic bold")

        stm_button = Button(self.root, text="Sentiment Analysis", borderwidth=10,
                            font="Helvetica 13 bold", command=self.sentiment_gui)
        stm_button.pack(ipadx=8, ipady=5, pady=15)

        ner_button = Button(self.root, text="Name Entity Recognition", borderwidth=10, font="Helvetica 13 bold",
                            command=self.ner_gui)
        ner_button.pack(ipadx=8, ipady=5, pady=15)

        emo_button = Button(self.root, text="Emotion Prediction", borderwidth=10, font="Helvetica 13 bold",
                            command=self.emotion_gui)
        emo_button.pack(ipadx=8, ipady=5, pady=15)

        logout_button = Button(self.root, text="Login Now", borderwidth=7, font="Helvetica 13 bold", command=self.login)
        logout_button.pack(ipadx=8, pady=10)

    def sentiment_gui(self):
        self.clear()

        self.root.geometry("350x600")
        main = Label(self.root, text='NLP App', fg='white', bg="#5834C0")
        main.pack(pady=20, ipadx=15, ipady=10, fill=X)
        main.configure(font="arial 20 italic bold")

        sentiment_heading = Label(self.root, text='Sentiment Analysis', fg='white', bg="#5834C0")
        sentiment_heading.pack(pady=20, ipadx=15, ipady=10, fill=X)
        sentiment_heading.configure(font="arial 15 bold")

        self.label = Label(self.root, text="Enter Text:", bg='#493387', fg='#DA40D3', font="Helvetica 15 bold")
        self.label.pack(pady=5)

        self.sentiment_entry = Entry(self.root, width=40)
        self.sentiment_entry.pack(pady=8, padx=10, ipady=3)
        self.sentiment_entry.focus()

        sentiment_button = Button(self.root, text="Analysis sentiment", borderwidth=7, font="Helvetica 13 bold",
                                  command=self.do_sentiment)
        sentiment_button.pack(ipadx=8, pady=10)

        self.sentiment_result = Label(self.root, text="", bg='#493387', fg='#DA40D3', font="Helvetica 15 bold")
        self.sentiment_result.pack(pady=5)

        go_back_button = Button(self.root, text="Go Back", borderwidth=7, font="Helvetica 13 bold",
                                command=self.home_gui)
        go_back_button.pack(ipadx=8, pady=10)

    def ner_gui(self):
        self.clear()

        self.root.geometry("430x580")
        main = Label(self.root, text='NLP App', fg='white', bg="#5834C0")
        main.pack(pady=20, ipadx=15, ipady=10, fill=X)
        main.configure(font="arial 20 italic bold")

        ner_heading = Label(self.root, text='Name Entity Recognition', fg='white', bg="#5834C0")
        ner_heading.pack(pady=20, ipadx=15, ipady=10, fill=X)
        ner_heading.configure(font="arial 15 bold")

        self.label = Label(self.root, text="Enter Text:", bg='#493387', fg='#DA40D3', font="Helvetica 15 bold")
        self.label.pack(pady=5)

        self.ner_entry = Entry(self.root, width=40)
        self.ner_entry.pack(pady=8, padx=10, ipady=3)
        self.ner_entry.focus()

        ner_button = Button(self.root, text="Analysis NER", borderwidth=7, font="Helvetica 13 bold", command=self.do_ner)
        ner_button.pack(ipadx=8, pady=10)

        self.ner_result = Label(self.root, text="", bg='#493387', fg='#DA40D3', font="Helvetica 15 bold")
        self.ner_result.pack(pady=5)

        go_back_button = Button(self.root, text="Go Back", borderwidth=7, font="Helvetica 13 bold",
                                command=self.home_gui)
        go_back_button.pack(ipadx=8, pady=10)

    def emotion_gui(self):
        self.clear()

        self.root.geometry("350x610")
        main = Label(self.root, text='NLP App', fg='white', bg="#5834C0")
        main.pack(pady=20, ipadx=15, ipady=10, fill=X)
        main.configure(font="arial 20 italic bold")

        emotion_heading = Label(self.root, text='Emotion', fg='white', bg="#5834C0")
        emotion_heading.pack(pady=20, ipadx=15, ipady=10, fill=X)
        emotion_heading.configure(font="arial 15 bold")

        self.label = Label(self.root, text="Enter Text:", bg='#493387', fg='#DA40D3', font="Helvetica 15 bold")
        self.label.pack(pady=5)

        self.emotion_entry = Entry(self.root, width=40)
        self.emotion_entry.pack(pady=8, padx=10, ipady=3)
        self.emotion_entry.focus()

        emotion_button = Button(self.root, text="Analysis Emotion", borderwidth=7, font="Helvetica 13 bold", command=self.do_emotion)
        emotion_button.pack(ipadx=8, pady=10)

        self.emotion_result = Label(self.root, text="", bg='#493387', fg='#DA40D3', font="Helvetica 15 bold")
        self.emotion_result.pack(pady=5)

        go_back_button = Button(self.root, text="Go Back", borderwidth=7, font="Helvetica 13 bold",
                                command=self.home_gui)
        go_back_button.pack(ipadx=8, pady=10)

    def do_sentiment(self):
        text = self.sentiment_entry.get()
        result = self.apio.sentiment_analysis(text)

        txt = ""
        for i in result['sentiment']:
            txt += i + "--> " + str(result['sentiment'][i]) + '\n'
        print(txt)
        self.sentiment_result['text'] = txt

    def do_ner(self):
        text = self.ner_entry.get()
        result = self.apio.ner_analysis(text)

        txt = ""
        for entity in result['entities']:
            name = entity['name']
            category = entity['category']
            confidence = entity['confidence_score']
            txt += f"{name} --> {category} (confidence: {confidence:.3f})\n"

        self.ner_result['text'] = txt
        print(txt)

    def do_emotion(self):
        text = self.emotion_entry.get()
        result = self.apio.emotion_analysis(text)

        txt = ""
        for emo in result['emotion']:
            txt += emo + "--> " + f"{result['emotion'][emo]:.2f}\n"

        print(txt)
        self.emotion_result['text'] = txt


nlp = NLPApp()