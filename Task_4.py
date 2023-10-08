import customtkinter as ctk
from PIL import Image
import random


class RockPaperScissor:
    def __init__(self, window):
        self.main = window
        self.main.geometry('760x520')
        self.main.resizable(False, False)
        self.main.title('Rock Paper Scissors')
        self.win = 0
        self.loose = 0
        self.main.rowconfigure((0, 1, 2, 3, 4, 5, 6), weight=1, uniform='a')
        self.main.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), weight=1, uniform='a')
        self.rock_c = ctk.CTkImage(Image.open('player_rock.png'), size=(120, 101))
        self.paper_c = ctk.CTkImage(Image.open('player_paper.png'), size=(120, 122))
        self.scissor_c = ctk.CTkImage(Image.open('player_scissors.png'), size=(120, 106))
        self.rock1 = ctk.CTkImage(Image.open('rock_1.png'), size=(100, 83))
        self.paper1 = ctk.CTkImage(Image.open('paper_1.png'), size=(110, 96))
        self.scissor1 = ctk.CTkImage(Image.open('scissors_1.png'), size=(110, 75))

        self.rock_l1 = ctk.CTkLabel(self.main, image=self.rock1, text='', bg_color='transparent')
        self.paper_l1 = ctk.CTkLabel(self.main, image=self.paper1, text='', )
        self.scissor_l1 = ctk.CTkLabel(self.main, image=self.scissor1, text='')
        self.yourChoice_l = ctk.CTkLabel(self.main, text='Your Choice', text_color='#000000', fg_color='#32d9ff',
                                         corner_radius=10,
                                         width=310)
        self.compChoice_l = ctk.CTkLabel(self.main, text='Computer\'s Choice', fg_color='#ff7e00', corner_radius=10,
                                         width=310)
        self.rps = ctk.CTkButton(self.main, text='Rock Paper Scissors', text_color='#000000', fg_color='#32d9ff',
                                 corner_radius=30, hover='NONE',
                                 font=ctk.CTkFont('default', 25)).place(x=250, y=10)
        self.vs = ctk.CTkImage(Image.open('versus.png'), size=(500, 500))
        self.vs_l = ctk.CTkLabel(self.main, image=ctk.CTkImage(Image.open('vs-te.png'), size=(300, 400)), text='', )
        self.rock_t = ctk.CTkButton(self.main, text='rock', fg_color='#3b3b3b', command=lambda: self.computer("rock"),
                                    corner_radius=30, width=90)
        self.paper_t = ctk.CTkButton(self.main, text='paper', fg_color='#3b3b3b',
                                     command=lambda: self.computer('paper'), corner_radius=30, width=90)
        self.scissor_t = ctk.CTkButton(self.main, text='scissors', fg_color='#3b3b3b',
                                       command=lambda: self.computer('scissor'), corner_radius=30, width=90)
        self.mostStart()

    def mostStart(self):
        self.rulesLabel = ctk.CTkLabel(self.main, corner_radius=20, width=200, text='Rules', fg_color='#3b3b3b')
        self.rulesLabel1 = ctk.CTkLabel(self.main, corner_radius=20, width=200, text='1.Rock beats Scissors',
                                        fg_color='#3b3b3b')
        self.rulesLabel2 = ctk.CTkLabel(self.main, corner_radius=20, width=200, text='2.Scissors beat Paper',
                                        fg_color='#3b3b3b')
        self.rulesLabel3 = ctk.CTkLabel(self.main, corner_radius=20, width=200, text='3.Paper beats Rock',
                                        fg_color='#3b3b3b')
        self.rulesLabel4 = ctk.CTkLabel(self.main, corner_radius=20, width=200, text='4.That\' all', fg_color='#3b3b3b')
        self.feedback = ctk.CTkLabel(self.main, corner_radius=20, width=200, text='feedback', fg_color='#3b3b3b')
        self.feedback.place(x=500, y=120)
        self.feed = ctk.CTkEntry(self.main, placeholder_text='Please Enter Your Feedback here...', height=180,
                                 width=200, corner_radius=20)
        self.feed.place(x=500, y=170)
        self.feed_button = ctk.CTkButton(self.main, text='submit feedback', command=lambda: print(self.feed.get()),
                                         corner_radius=20)
        self.feed_button.place(x=525, y=370)
        self.rulesLabel.place(x=50, y=100 + 20)
        self.rulesLabel1.place(x=50, y=150 + 20)
        self.rulesLabel2.place(x=50, y=200 + 20)
        self.rulesLabel3.place(x=50, y=250 + 20)
        self.rulesLabel4.place(x=50, y=300 + 20)
        self.play = ctk.CTkButton(self.main, text='Start', width=100, corner_radius=20, command=lambda: self.start1())
        self.play.place(x=330, y=420)

    def start1(self):
        self.rulesLabel.destroy()
        self.rulesLabel1.destroy()
        self.rulesLabel2.destroy()
        self.rulesLabel3.destroy()
        self.rulesLabel4.destroy()
        self.feedback.destroy()
        self.feed_button.destroy()
        self.play.destroy()
        self.feed.destroy()
        self.start()

    def start(self):
        self.rock_l = ctk.CTkLabel(self.main, image=self.rock_c, text='')
        self.paper_l = ctk.CTkLabel(self.main, image=self.paper_c, text='', )
        self.scissor_l = ctk.CTkLabel(self.main, image=self.scissor_c, text='')

        self.rock_l1 = ctk.CTkLabel(self.main, image=self.rock1, text='', bg_color='transparent')
        self.paper_l1 = ctk.CTkLabel(self.main, image=self.paper1, text='', )
        self.scissor_l1 = ctk.CTkLabel(self.main, image=self.scissor1, text='')
        self.winLabel = ctk.CTkLabel(self.main, text=f'Wins : {self.win}', fg_color='#3b3b3b', corner_radius=10,
                                     width=100)
        self.looseLabel = ctk.CTkLabel(self.main, text=f'Lose : {self.loose}', fg_color='#3b3b3b', corner_radius=10,
                                       width=100)
        self.choice()

    def choice(self):
        self.yourChoice_l.place(x=45, y=60)
        self.compChoice_l.place(x=400, y=60)
        self.rock_l1.place(x=120, y=100)
        self.paper_l1.place(x=120, y=230)
        self.scissor_l1.place(x=120, y=380)
        self.rock_l.place(x=580, y=100)
        self.paper_l.place(x=580, y=230)
        self.scissor_l.place(x=580, y=380)

        self.rock_t.place(x=20, y=100 + 30)
        self.paper_t.place(x=20, y=230 + 40)
        self.scissor_t.place(x=20, y=380 + 20)
        self.vs_l.place(x=230, y=100)

        self.winLabel.place(x=47, y=10)
        self.looseLabel.place(x=610, y=10)

    def computer(self, comp):
        self.background = ctk.CTkImage(Image.open('VS_Background.jpg'), size=(760, 520))
        self.background_l = ctk.CTkLabel(self.main, image=self.background, text='')
        comp_move = random.choice(["rock", "paper", "scissor"])
        self.rock_l1 = ctk.CTkLabel(self.main, image=self.rock1, text='', bg_color='#fa9600')
        self.paper_l1 = ctk.CTkLabel(self.main, image=self.paper1, text='', bg_color='#fa9600')
        self.scissor_l1 = ctk.CTkLabel(self.main, image=self.scissor1, text='', bg_color='#fa9600')
        self.rock_l = ctk.CTkLabel(self.main, image=self.rock_c, text='', bg_color='#32d9ff')
        self.paper_l = ctk.CTkLabel(self.main, image=self.paper_c, text='', bg_color='#32d9ff')
        self.scissor_l = ctk.CTkLabel(self.main, image=self.scissor_c, text='', bg_color='#32d9ff')
        if comp_move == "rock":
            self.img = self.rock_l
        elif comp_move == "paper":
            self.img = self.paper_l
        else:
            self.img = self.scissor_l
        if comp == "rock":
            self.img_1 = self.rock_l1
        elif comp == "paper":
            self.img_1 = self.paper_l1
        else:
            self.img_1 = self.scissor_l1
        self.background_l.pack()
        self.img.place(x=530, y=230)
        self.img_1.place(x=170, y=230)
        if comp == comp_move:
            self.text = 'It\' a tie!'
        elif (comp == 'rock' and comp_move == 'scissor') or (comp == 'paper' and comp_move == 'rock') or (
                comp == 'scissor' and comp_move == 'paper'):
            self.text = 'You Won!'
            self.win += 1
        elif (comp == 'scissor' and comp_move == 'rock') or (comp == 'rock' and comp_move == 'paper') or (
                comp == 'paper' and comp_move == 'scissor'):
            self.text = 'You Lose!'
            self.loose += 1
        self.label = ctk.CTkLabel(self.main, width=200, text=self.text, corner_radius=30, fg_color='#3b3b3b',
                                  bg_color='#32d9ff')
        self.player_move = ctk.CTkLabel(self.main, width=100, text=f'you chose {comp}', corner_radius=30,
                                        fg_color='#3b3b3b',
                                        bg_color='#ff7e00')
        self.computer_move = ctk.CTkLabel(self.main, width=100, text=f'computer chose {comp_move}', corner_radius=30,
                                          fg_color='#3b3b3b',
                                          bg_color='#32d9ff')
        self.player_move.place(x=300, y=100)
        self.computer_move.place(x=470, y=100)
        self.computer_move.place()
        self.label.place(x=305, y=430)
        self.restart_b = ctk.CTkButton(self.main, text='restart', width=100, bg_color='#ff7e00',
                                       command=lambda: self.restart(), corner_radius=30)
        self.restart_b.place(x=180, y=430)

    def restart(self):
        self.player_move.destroy()
        self.computer_move.destroy()
        self.restart_b.destroy()
        self.label.destroy()
        self.background_l.destroy()
        self.rock_l1.destroy()
        self.paper_l1.destroy()
        self.scissor_l1.destroy()
        self.rock_l.destroy()
        self.paper_l.destroy()
        self.scissor_l.destroy()

        self.start()


main = ctk.CTk()
# ctk.set_default_color_theme("green")
app = RockPaperScissor(main)
main.mainloop()
