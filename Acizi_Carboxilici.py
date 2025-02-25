import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image  

cnt = 0

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo, PageThree, PageFour, ContactPage, PageFive, PageSix, PageSeven, PageEight,
                 QuizPage1, QuizPage2, QuizPage3, QuizPage4, QuizPage5, QuizPage6, QuizPage7, QuizPage8, QuizPage9, 
                 QuizPage10, QuizPage11, QuizPage12, QuizPage13, QuizPage14, QuizPage15, FinalQuiz):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.update()
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.title("Acizi Carboxilici")
        self.controller.iconphoto(False,tk.PhotoImage(file=r"images\bg-images\_icon.png"))
        def continuare_lectie():
            controller.show_frame("PageOne")
        def quiz():
            controller.show_frame("QuizPage1")
        def contact():
            controller.show_frame("ContactPage")
        def quit():
            self.quit()
        load = Image.open(r"images\bg-images\_start_page_bg.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load1 = Image.open(r"images\buttons\incepe.png")
        btn_img1= ImageTk.PhotoImage(load1)
        btn_label1 = tk.Label(self,image=btn_img1)
        button_incepe= tk.Button(self, image=btn_img1,command = continuare_lectie,borderwidth = 0,highlightthickness = 0)
        button_incepe.image=btn_img1
        button_incepe.place(x=710,y=244)

        load2 = Image.open(r"images\buttons\chestionar.png")
        btn_img2= ImageTk.PhotoImage(load2)
        btn_label2 = tk.Label(self,image=btn_img2)
        button_quiz= tk.Button(self, image=btn_img2,command = quiz,borderwidth = 0,highlightthickness = 0)
        button_quiz.image=btn_img2
        button_quiz.place(x=710,y=393)

        load3 = Image.open(r"images\buttons\contact.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_contact= tk.Button(self, image=btn_img3,command = contact,borderwidth = 0,highlightthickness = 0)
        button_contact.image=btn_img3
        button_contact.place(x=710,y=538)

        load4 = Image.open(r"images\buttons\iesire.png")
        btn_img4= ImageTk.PhotoImage(load4)
        btn_label4 = tk.Label(self,image=btn_img4)
        button_exit= tk.Button(self, image=btn_img4,command= quit,borderwidth = 0,highlightthickness = 0)
        button_exit.image=btn_img4
        button_exit.place(x=886,y=538)

        
class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
      
        def urmator():
            controller.show_frame("PageTwo")
        def home():
            controller.show_frame("StartPage")

        load = Image.open(r"images\bg-images\pagina 1.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        # ---------------------------------------   B U T O A N E _ N A V ---------------------------------------------------

        load2 = Image.open(r"images\buttons\next-button.png")
        btn_img2= ImageTk.PhotoImage(load2)
        btn_label2 = tk.Label(self,image=btn_img2)
        button_urm= tk.Button(self, image=btn_img2,command = urmator ,borderwidth = 0,highlightthickness = 0)
        button_urm.image=btn_img2
        button_urm.place(x=1150,y=320)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0,highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        
class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        def inapoi():
            controller.show_frame("PageOne")
        def urmator():
            controller.show_frame("PageThree")
        def home():
            controller.show_frame("StartPage")

        load = Image.open(r"images\bg-images\pagina 2.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        # ---------------------------------------   B U T O A N E _ N A V ---------------------------------------------------
        load1 = Image.open(r"images\buttons\back-button.png")
        btn_img1= ImageTk.PhotoImage(load1)
        btn_label1 = tk.Label(self,image=btn_img1)
        button_inapoi= tk.Button(self, image=btn_img1,command = inapoi,borderwidth = 0,highlightthickness = 0)
        button_inapoi.image=btn_img1
        button_inapoi.place(x=50,y=320)

        load2 = Image.open(r"images\buttons\next-button.png")
        btn_img2= ImageTk.PhotoImage(load2)
        btn_label2 = tk.Label(self,image=btn_img2)
        button_urm= tk.Button(self, image=btn_img2,command = urmator ,borderwidth = 0,highlightthickness = 0)
        button_urm.image=btn_img2
        button_urm.place(x=1150,y=320)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0,highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

         
class PageThree(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def inapoi():
            controller.show_frame("PageTwo")
        def urmator():
            controller.show_frame("PageFour")
        def home():
            controller.show_frame("StartPage")

        load = Image.open(r"images\bg-images\pagina 3.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)


        # ---------------------------------------   B U T O A N E _ N A V ---------------------------------------------------
        load1 = Image.open(r"images\buttons\back-button.png")
        btn_img1= ImageTk.PhotoImage(load1)
        btn_label1 = tk.Label(self,image=btn_img1)
        button_inapoi= tk.Button(self, image=btn_img1,command = inapoi,borderwidth = 0,highlightthickness = 0)
        button_inapoi.image=btn_img1
        button_inapoi.place(x=50,y=320)

        load2 = Image.open(r"images\buttons\next-button.png")
        btn_img2= ImageTk.PhotoImage(load2)
        btn_label2 = tk.Label(self,image=btn_img2)
        button_urm= tk.Button(self, image=btn_img2,command = urmator ,borderwidth = 0,highlightthickness = 0)
        button_urm.image=btn_img2
        button_urm.place(x=1150,y=320)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0,highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)
 
        
class PageFour(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def inapoi():
            controller.show_frame("PageThree")
        def urmator():
            controller.show_frame("PageFive")
        def home():
            controller.show_frame("StartPage")

        load = Image.open(r"images\bg-images\pagina 4.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        # ---------------------------------------   B U T O A N E _ N A V ---------------------------------------------------
        load1 = Image.open(r"images\buttons\back-button.png")
        btn_img1= ImageTk.PhotoImage(load1)
        btn_label1 = tk.Label(self,image=btn_img1)
        button_inapoi= tk.Button(self, image=btn_img1,command = inapoi,borderwidth = 0,highlightthickness = 0)
        button_inapoi.image=btn_img1
        button_inapoi.place(x=50,y=320)

        load2 = Image.open(r"images\buttons\next-button.png")
        btn_img2= ImageTk.PhotoImage(load2)
        btn_label2 = tk.Label(self,image=btn_img2)
        button_urm= tk.Button(self, image=btn_img2,command = urmator ,borderwidth = 0,highlightthickness = 0)
        button_urm.image=btn_img2
        button_urm.place(x=1150,y=320)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0,highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)
 

class PageFive(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def inapoi():
            controller.show_frame("PageFour")
        def urmator():
            controller.show_frame("PageSix")
        def home():
            controller.show_frame("StartPage")

        load = Image.open(r"images\bg-images\pagina 5.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        # ---------------------------------------   B U T O A N E _ N A V ---------------------------------------------------
        load1 = Image.open(r"images\buttons\back-button.png")
        btn_img1= ImageTk.PhotoImage(load1)
        btn_label1 = tk.Label(self,image=btn_img1)
        button_inapoi= tk.Button(self, image=btn_img1,command = inapoi,borderwidth = 0,highlightthickness = 0)
        button_inapoi.image=btn_img1
        button_inapoi.place(x=50,y=320)

        load2 = Image.open(r"images\buttons\next-button.png")
        btn_img2= ImageTk.PhotoImage(load2)
        btn_label2 = tk.Label(self,image=btn_img2)
        button_urm= tk.Button(self, image=btn_img2,command = urmator ,borderwidth = 0,highlightthickness = 0)
        button_urm.image=btn_img2
        button_urm.place(x=1150,y=320)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0,highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)
 

class PageSix(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def inapoi():
            controller.show_frame("PageFive")
        def urmator():
            controller.show_frame("PageSeven")
        def home():
            controller.show_frame("StartPage")

        load = Image.open(r"images\bg-images\pagina 6.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)


        # ---------------------------------------   B U T O A N E _ N A V ---------------------------------------------------
        load1 = Image.open(r"images\buttons\back-button.png")
        btn_img1= ImageTk.PhotoImage(load1)
        btn_label1 = tk.Label(self,image=btn_img1)
        button_inapoi= tk.Button(self, image=btn_img1,command = inapoi,borderwidth = 0,highlightthickness = 0)
        button_inapoi.image=btn_img1
        button_inapoi.place(x=50,y=320)

        load2 = Image.open(r"images\buttons\next-button.png")
        btn_img2= ImageTk.PhotoImage(load2)
        btn_label2 = tk.Label(self,image=btn_img2)
        button_urm= tk.Button(self, image=btn_img2,command = urmator ,borderwidth = 0,highlightthickness = 0)
        button_urm.image=btn_img2
        button_urm.place(x=1150,y=320)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0,highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)
 

class PageSeven(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def inapoi():
            controller.show_frame("PageSix")
        def urmator():
            controller.show_frame("PageEight")
        def home():
            controller.show_frame("StartPage")

        load = Image.open(r"images\bg-images\pagina 7.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        # ---------------------------------------   B U T O A N E _ N A V ---------------------------------------------------
        load1 = Image.open(r"images\buttons\back-button.png")
        btn_img1= ImageTk.PhotoImage(load1)
        btn_label1 = tk.Label(self,image=btn_img1)
        button_inapoi= tk.Button(self, image=btn_img1,command = inapoi,borderwidth = 0,highlightthickness = 0)
        button_inapoi.image=btn_img1
        button_inapoi.place(x=50,y=320)

        load2 = Image.open(r"images\buttons\next-button.png")
        btn_img2= ImageTk.PhotoImage(load2)
        btn_label2 = tk.Label(self,image=btn_img2)
        button_urm= tk.Button(self, image=btn_img2,command = urmator ,borderwidth = 0,highlightthickness = 0)
        button_urm.image=btn_img2
        button_urm.place(x=1150,y=320)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0,highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)
 

class PageEight(tk.Frame):
    
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def inapoi():
            controller.show_frame("PageSeven")
        def home():
            controller.show_frame("StartPage")

        load = Image.open(r"images\bg-images\pagina 8.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)


        # ---------------------------------------   B U T O A N E _ N A V ---------------------------------------------------
        load1 = Image.open(r"images\buttons\back-button.png")
        btn_img1= ImageTk.PhotoImage(load1)
        btn_label1 = tk.Label(self,image=btn_img1)
        button_inapoi= tk.Button(self, image=btn_img1,command = inapoi,borderwidth = 0,highlightthickness = 0)
        button_inapoi.image=btn_img1
        button_inapoi.place(x=50,y=320)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0,highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)
 

class ContactPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        def home():
            controller.show_frame("StartPage")

        load = Image.open(r"images\bg-images\_contact-page.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)


#----------------------------------------------------------------------------------- Q U I Z ---------------------------------------------------------------


class QuizPage1(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller

        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage2")
        def gresit():
            controller.show_frame("QuizPage2")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

       

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 1 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="Formula generală a acizilor monocarboxilici saturați este:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')

        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\1a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\1b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\1c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\1d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage2(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage3")
        def gresit():
            controller.show_frame("QuizPage3")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 2 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="Oțetul conține:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')

        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\2a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\2b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\2c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\2d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage3(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage4")
        def gresit():
            controller.show_frame("QuizPage4")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 3 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="Acidul cu un singur atom de carbon se numește:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')

        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\3a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\3b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\3c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\3d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage4(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage5")
        def gresit():
            controller.show_frame("QuizPage5")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 4 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="Acetatul de benzil are formula moleculară:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')

        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\4a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\4b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\4c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\4d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage5(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage6")
        def gresit():
            controller.show_frame("QuizPage6")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 5 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="Acidul acetic dizolvat in 200g soluție este consumat complet de 16,25g Zn\nde puritate 80%. Concentrația soluției este:", bg="#eaebed", fg="#21605D", font="Helvetica 25 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')


        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\5a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\5b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\5c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\5d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage6(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage7")
        def gresit():
            controller.show_frame("QuizPage7")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 6 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="În urma reacției CH3-CH2-OH + 2[O] va rezulta:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')


        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\6c.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\6b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\6a.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\6d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage7(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage8")
        def gresit():
            controller.show_frame("QuizPage8")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 7 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="În urma hidrolizei acide a formiatului de propil va rezulta:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')


        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\7a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\7b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\7c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\7d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage8(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage9")
        def gresit():
            controller.show_frame("QuizPage9")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 8 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="S-au obținut 1,64L gaz măsurați la 3 atm și 27°C din reacția acidului formic\ncu Na. Volumul de soluție de acid formic(Cm = 1M) este:", bg="#eaebed", fg="#21605D", font="Helvetica 25 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')


        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\8a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\8b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\8c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\8d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage9(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage10")
        def gresit():
            controller.show_frame("QuizPage10")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 9 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="Formula acidului acetic este:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')


        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\9d.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\9b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\9c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\9a.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage10(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage11")
        def gresit():
            controller.show_frame("QuizPage11")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 10 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="În urma reacției 2CH3-COOH + CaO rezultă:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')


        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\10a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\10b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\10c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\10d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage11(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage12")
        def gresit():
            controller.show_frame("QuizPage12")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 11 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="Schema reacției de esterificare este corectă în:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')


        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\11a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\11b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\11c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\11d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage12(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage13")
        def gresit():
            controller.show_frame("QuizPage13")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 12 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="Acidul cu formula HOOC-COOH se numește:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')


        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\12d.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\12b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\12c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\12a.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage13(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage14")
        def gresit():
            controller.show_frame("QuizPage14")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 13 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="Sarea cu formula CH3-COONa se numește:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')


        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\13a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\13b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\13c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\13d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage14(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            controller.show_frame("QuizPage15")
        def gresit():
            controller.show_frame("QuizPage15")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------

        enunt = tk.Label(self, text="Întrebarea 14 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="Acidul aromatic cu formula C6H5-COOH se numește:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')


        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        
        ans1 = Image.open(r"images\quiz-buttons\14a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)


        ans2 = Image.open(r"images\quiz-buttons\14b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)


        ans3 = Image.open(r"images\quiz-buttons\14c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)


        ans4 = Image.open(r"images\quiz-buttons\14d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)


class QuizPage15(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def corect():
            global cnt
            cnt=cnt+1
            messagebox.showinfo("Felicitări", f"Ai obținut {cnt}/15 puncte!")
            controller.show_frame("FinalQuiz")
        def gresit():
            messagebox.showinfo("Felicitări", f"Ai obținut {cnt}/15 puncte!")
            controller.show_frame("FinalQuiz")

        load = Image.open(r"images\bg-images\_chestionar.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        #--------------------------------------------------------------------- Q U E S T I O N ---------------------------------------------------------------------
        enunt = tk.Label(self, text="Întrebarea 15 din 15", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        enunt.place(relx = 0.5, rely = 0.25, anchor = 'center')

        question = tk.Label(self, text="Acidul formic este:", bg="#eaebed", fg="#21605D", font="Helvetica 30 bold")
        question.place(relx = 0.5, rely = 0.35, anchor = 'center')
        #---------------------------------------------------------------------   C H O I C E S ---------------------------------------------------------------------
        ans1 = Image.open(r"images\quiz-buttons\15a.png")
        btn_ans1 = ImageTk.PhotoImage(ans1)
        btn_labelA = tk.Label(self, image = btn_ans1)
        button_optionA = tk.Button(self, image = btn_ans1, command = corect, borderwidth = 0, highlightthickness = 0)
        button_optionA.image = btn_ans1
        button_optionA.place(x=260, y=360)

        ans2 = Image.open(r"images\quiz-buttons\15b.png")
        btn_ans2 = ImageTk.PhotoImage(ans2)
        btn_labelB = tk.Label(self, image = btn_ans2)
        button_optionB = tk.Button(self, image = btn_ans2, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionB.image = btn_ans2
        button_optionB.place(x=700, y=360)

        ans3 = Image.open(r"images\quiz-buttons\15c.png")
        btn_ans3 = ImageTk.PhotoImage(ans3)
        btn_labelC = tk.Label(self, image = btn_ans3)
        button_optionC = tk.Button(self, image = btn_ans3, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionC.image = btn_ans3
        button_optionC.place(x=260, y=520)

        ans4 = Image.open(r"images\quiz-buttons\15d.png")
        btn_ans4 = ImageTk.PhotoImage(ans4)
        btn_labelD = tk.Label(self, image = btn_ans4)
        button_optionD = tk.Button(self, image = btn_ans4, command = gresit, borderwidth = 0, highlightthickness = 0)
        button_optionD.image = btn_ans4
        button_optionD.place(x=700, y=520)

class FinalQuiz(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        def home():
            global cnt
            cnt=0
            controller.show_frame("StartPage")
        def again():
            global cnt
            cnt = 0
            controller.show_frame("QuizPage1")

        load = Image.open(r"images\bg-images\_rezumat-background.png")
        bg_img = ImageTk.PhotoImage(load)
        bg_label = tk.Label(self,image=bg_img)
        bg_label.image=bg_img
        bg_label.place(x=0,y=0,relwidth=1,relheight=1)

        load3 = Image.open(r"images\buttons\home-button.png")
        btn_img3= ImageTk.PhotoImage(load3)
        btn_label3 = tk.Label(self,image=btn_img3)
        button_home= tk.Button(self, image=btn_img3,command = home ,borderwidth = 0, highlightthickness = 0)
        button_home.image=btn_img3
        button_home.place(x=50,y=50)

        enunt0 = tk.Label(self, text=f"Felicitări, ai terminat chestionarul!", bg="#eaebed", fg="#21605D", font="Helvetica 50 bold")
        enunt0.place(relx = 0.5, rely = 0.5, anchor = 'center')

        tryagain = Image.open(r"images\buttons\incearca-din-nou.png")
        btn_img = ImageTk.PhotoImage(tryagain)
        btn_label = tk.Label(self, image=btn_img)
        button_trya = tk.Button(self, image=btn_img, command = again , borderwidth = 0, highlightthickness = 0)
        button_trya.image = btn_img
        button_trya.place(x=469, y=556)
        
        
if __name__ == "__main__":
    app = SampleApp()
    app.resizable(False,False)
    #app.geometry("1280x720")
    app.title("Acizii carboxilici")
    window_height = 720
    window_width = 1280
    
    screen_width = app.winfo_screenwidth()
    screen_height = app.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (window_width/2))
    y_cordinate = int((screen_height/2) - (window_height/2))

    app.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))


    app.mainloop()