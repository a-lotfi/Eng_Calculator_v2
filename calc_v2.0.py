from string import digits
import tkinter as tk
from turtle import right
from calc_modules import *
import os

# constants:
# constants of frames
DISPLAY_FRAME_BG = '#FFFFFF'
BUTTON_FRAME_BG = '#FFFFFF'

# constants of show result label 
LBL_SHOW_RESULT_BG = '#FFFFFF'
LBL_SHOW_RESULT_FG = 'black'
LBL_SHOW_RESULT_FONT = ('Arial', 16, 'bold')
LBL_SHOW_RESULT_HEIGHT = 2

# constants of listbar for calc_history
LB_HIST_BG = '#FFFFFF'
LB_HIST_FG = 'black'
LB_HIST_FONT = ('Arial', 10)
LB_HIST_HEIGHT = 5

# constants of digit and operator buttons
BTN_DIGIT_WIDTH = 8
BTN_DIGIT_HEIGHT = 1
BTN_DIGIT_FG = 'gray20'
BTN_DIGIT_BG = '#FFFFFF'
BTN_DIGIT_ACTIVE_BG = '#8A9DA4'
BTN_DIGIT_ACTIVE_FG = 'black'
BTN_FONT = ('Arial', 11, 'bold')

# constants of clear, Delete buttton
BTN_AC_DEL_FG = '#FFFFFF'
BTN_AC_DEL_BG = '#fa890f'
BTN_AC_DEL_ACTIVE_BG = '#B35700'
BTN_AC_DEL_ACTIVE_FG = '#FFFFFF'

# constants of management buttons such as Save and Exit button
BTN_MANAGE_WIDTH = 8
BTN_MANAGE_HEIGHT = 1
BTN_MANAGE_FG = '#FFFFFF'
BTN_MANAGE_BG = '#202020'
BTN_MANAGE_ACTIVE_BG = '#202020'
BTN_MANAGE_ACTIVE_FG = '#FFFFFF'

# constants of Special buttons such as sin(, log(, . . . 
BTN_SPECIAL_FG = '#FFFFFF'
BTN_SPECIAL_BG = '#31135E'
BTN_SPECIAL_ACTIVE_BG = '#000028'
BTN_SPECIAL_ACTIVE_FG = '#FFFFFF'

# constants of = button
BTN_EQUAL_FG = '#FFFFFF'
BTN_EQUAL_BG = '#fa890f'
BTN_EQUAL_ACTIVE_BG = '#B35700'
BTN_EQUAL_ACTIVE_FG = '#FFFFFF'

# ------------------------------------------------------------------------------------

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Eng Calculator 2.0')
        self.window.iconbitmap(r'..\myicon.ico')
        self.window.resizable(False, False)

        # create frame for display widget:
        self.display_frame = self.create_display_frame()

        # create widget in display frmae:
        self.lbl_show_result = self.create_display_lbl()
        self.lb_hist, self.sbr_hist = self.create_display_hist()

        self.digits = {
            7: (6, 1), 8: (6, 2), 9: (6, 3),
            4: (7, 1), 5: (7, 2), 6: (7, 3),
            1: (8, 1), 2: (8, 2), 3: (8, 3),
            0: (9, 2),
        }
        self.simple_operators = {
            '*': (7, 4), '/': (7, 5),
            '+': (8, 4), '-': (8, 5),
            '.': (9, 3), '%': (9, 4)
        }
        self.eng_operators = ['sin(', 'cos(', 'tan(', 'e', 'pi', 'log(', 'ln(', '(', ')', '²',]
        #create frame for button widget:
        self.button_frame = self.create_button_frame()

        # create widget in button frame:
        self.create_digit_button()
        self.create_simple_operators_button()
        self.btn_clear, self.btn_delete = self.create_AC_del_button()
        self.btn_equal = self.create_equal_button()
        self.btn_eng = self.create_eng_button()
        self.btn_manage_objs = self.create_manage_button()
        self.btn_eng_objs = self.create_eng_operators_button()

        self.binding()


    def create_display_frame(self):
        frame = tk.Frame(
            master=self.window,
            bg=DISPLAY_FRAME_BG,
        )
        frame.pack(expand=True, fill=tk.BOTH)
        return frame

    

    def create_display_hist(self):
        # create listbox for show calculation history
        lb_hist = tk.Listbox(
            master=self.display_frame,
            height=LB_HIST_HEIGHT,
            bg=LB_HIST_BG,
            fg=LB_HIST_FG,
            font=LB_HIST_FONT,
            relief=tk.GROOVE,
            borderwidth=0,
        )

        # create scrollbar for listbox
        sbr_hist = tk.Scrollbar(
            master=self.display_frame,
        )

        # link listbox with scrollbar
        lb_hist.config(yscrollcommand=sbr_hist)
        sbr_hist.config(command = lb_hist.yview)

        # pack listbox and scrollbar
        sbr_hist.pack(side=tk.RIGHT, fill=tk.Y, anchor='e')
        lb_hist.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH, anchor='e')

        return lb_hist, sbr_hist
        

    def create_display_lbl(self):
        lbl_show_result = tk.Label(
            master=self.display_frame,
            text='0',
            bg=LBL_SHOW_RESULT_BG,
            fg=LBL_SHOW_RESULT_FG,
            font=LBL_SHOW_RESULT_FONT,
            height=LBL_SHOW_RESULT_HEIGHT,
        )
        lbl_show_result.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
        return lbl_show_result
    

    def create_button_frame(self):
        frame = tk.Frame(
            master=self.window,
            bg = BUTTON_FRAME_BG,
        )
        frame.pack(expand=True, fill=tk.BOTH)
        return frame


    def create_digit_button(self):
        for digit, grid_value in self.digits.items():
            btn_digit = tk.Button(
                master=self.button_frame,
                text=str(digit),
                relief=tk.GROOVE ,
                width=BTN_DIGIT_WIDTH,
                height=BTN_DIGIT_HEIGHT,
                fg=BTN_DIGIT_FG,
                bg=BTN_DIGIT_BG,
                activebackground=BTN_DIGIT_ACTIVE_BG,
                activeforeground=BTN_DIGIT_ACTIVE_FG,
                font=BTN_FONT,
                borderwidth=0,
                command= lambda x=str(digit): self.click_button(x),
                )
            btn_digit.grid(row=grid_value[0], column=grid_value[1])
            
            # Hovering over digit buttons
            btn_digit.bind("<Enter>", lambda e, x=btn_digit: self.on_enter(x))
            btn_digit.bind("<Leave>", lambda e, x=btn_digit: self.on_leave(x))

    def create_simple_operators_button(self):
        for operator, grid_value in self.simple_operators.items():
            btn_operator = tk.Button(
                master=self.button_frame,
                text=operator,
                relief=tk.GROOVE,
                width=BTN_DIGIT_WIDTH,
                height=BTN_DIGIT_HEIGHT,
                fg=BTN_DIGIT_FG,
                bg=BTN_DIGIT_BG,
                activebackground=BTN_DIGIT_ACTIVE_BG,
                activeforeground=BTN_DIGIT_ACTIVE_FG,
                font=BTN_FONT,
                borderwidth=0,
                command= lambda x=operator: self.click_button(x),

            )
            btn_operator.grid(row=grid_value[0], column=grid_value[1])
            
            # Hovering over simple operator buttons
            btn_operator.bind("<Enter>", lambda e, x=btn_operator: self.on_enter(x))
            btn_operator.bind("<Leave>", lambda e, x=btn_operator: self.on_leave(x))
            

    def create_AC_del_button(self):
        btn_clear = tk.Button(
            master=self.button_frame,
            text = 'AC',
            relief=tk.GROOVE,
            width=BTN_DIGIT_WIDTH,
            height=BTN_DIGIT_HEIGHT,
            fg=BTN_AC_DEL_FG,
            bg=BTN_AC_DEL_BG,
            activebackground=BTN_AC_DEL_ACTIVE_BG,
            activeforeground=BTN_AC_DEL_ACTIVE_FG,
            font=BTN_FONT,
            borderwidth=0,
            command= lambda : click_AC_C(
                self.lbl_show_result, 
                self.lb_hist, 
                self.btn_clear, 
                ),

        )
        btn_clear.grid(row=6, column=4)

        btn_delete = tk.Button(
            master=self.button_frame,
            text = 'Del',
            relief=tk.GROOVE,
            width=BTN_DIGIT_WIDTH,
            height=BTN_DIGIT_HEIGHT,
            fg=BTN_AC_DEL_FG,
            bg=BTN_AC_DEL_BG,
            activebackground=BTN_AC_DEL_ACTIVE_BG,
            activeforeground=BTN_AC_DEL_ACTIVE_FG,
            font=BTN_FONT,
            borderwidth=0,
            command= lambda : self.click_button('Del'),

        )
        btn_delete.grid(row=6, column=5)

        # Hovering over clear and delete buttons
        for i in [btn_clear, btn_delete]:
            i.bind("<Enter>", lambda e, x=i: self.on_enter(x))
            i.bind("<Leave>", lambda e, x=i: self.on_leave(x))

        return btn_clear, btn_delete

    def create_equal_button(self):
        btn_equal = tk.Button(
            master=self.button_frame,
            text = '=',
            relief=tk.GROOVE,
            width=BTN_DIGIT_WIDTH,
            height=BTN_DIGIT_HEIGHT,
            fg=BTN_EQUAL_FG,
            bg=BTN_EQUAL_BG,
            activebackground=BTN_EQUAL_ACTIVE_BG,
            activeforeground=BTN_EQUAL_ACTIVE_FG,
            font=BTN_FONT,
            borderwidth=0,
            command= lambda : self.click_button('='),

        )
        btn_equal.grid(row=9, column=5)

        # Hovering over equal button
        btn_equal.bind("<Enter>", lambda e, x=btn_equal: self.on_enter(x))
        btn_equal.bind("<Leave>", lambda e, x=btn_equal: self.on_leave(x))

        return btn_equal
    
    def create_eng_button(self):
        btn_eng = tk.Button(
            master=self.button_frame,
            text = 'Eng',
            relief=tk.GROOVE,
            width=BTN_DIGIT_WIDTH,
            height=BTN_DIGIT_HEIGHT,
            fg=BTN_DIGIT_FG,
            bg=BTN_DIGIT_BG,
            activebackground=BTN_DIGIT_ACTIVE_BG,
            activeforeground=BTN_DIGIT_ACTIVE_FG,
            font=BTN_FONT,
            borderwidth=0,
            command= lambda : on_eng(
                self.btn_eng_objs, 
                self.btn_manage_objs, 
                self.btn_eng, 
                self.window),
        )
        btn_eng.grid(row=9, column=1)

        # Hovering over Eng button
        btn_eng.bind("<Enter>", lambda e, x=btn_eng: self.on_enter(x))
        btn_eng.bind("<Leave>", lambda e, x=btn_eng: self.on_leave(x))
        
        return btn_eng

    def create_manage_button(self):
        btn_up = tk.Button(
            master=self.button_frame,
            text = '↑',
            relief=tk.GROOVE,
            width=BTN_MANAGE_WIDTH,
            height=BTN_MANAGE_HEIGHT,
            fg=BTN_MANAGE_FG,
            bg=BTN_MANAGE_BG,
            activebackground=BTN_MANAGE_ACTIVE_BG,
            activeforeground=BTN_MANAGE_ACTIVE_FG,
            font=BTN_FONT,
            borderwidth=1,
            border=1,
            command= lambda : self.click_button('↑'),

        )

        btn_down = tk.Button(
            master=self.button_frame,
            text = '↓',
            relief=tk.GROOVE,
            width=BTN_MANAGE_WIDTH,
            height=BTN_MANAGE_HEIGHT,
            fg=BTN_MANAGE_FG,
            bg=BTN_MANAGE_BG,
            activebackground=BTN_MANAGE_ACTIVE_BG,
            activeforeground=BTN_MANAGE_ACTIVE_FG,
            font=BTN_FONT,
            borderwidth=1,
            border=1,
            command= lambda : self.click_button('↓'),

        )

        btn_exit = tk.Button(
            master=self.button_frame,
            text = 'Exit',
            relief=tk.GROOVE,
            width=BTN_MANAGE_WIDTH,
            height=BTN_MANAGE_HEIGHT,
            fg=BTN_MANAGE_FG,
            bg=BTN_MANAGE_BG,
            activebackground=BTN_MANAGE_ACTIVE_BG,
            activeforeground=BTN_MANAGE_ACTIVE_FG,
            font=BTN_FONT,
            borderwidth=1,
            border=1,
            command= lambda : click_exit(self.window),
        )
        btn_save = tk.Button(
            master=self.button_frame,
            text = 'Save',
            relief=tk.GROOVE,
            width=BTN_MANAGE_WIDTH,
            height=BTN_MANAGE_HEIGHT,
            fg=BTN_MANAGE_FG,
            bg=BTN_MANAGE_BG,
            activebackground=BTN_MANAGE_ACTIVE_BG,
            activeforeground=BTN_MANAGE_ACTIVE_FG,
            font=BTN_FONT,
            borderwidth=1,
            border=1,
            command= lambda : click_save(self.lb_hist),

        )

        btn_up.grid(row=2, column=2, columnspan=3, sticky='news')
        btn_down.grid(row=3, column=2, columnspan=3, sticky='news')
        btn_exit.grid(row=2, column=5, rowspan=2, sticky='news')
        btn_save.grid(row=2, column=1, rowspan=2, sticky='news')

        # Hovering over management buttons
        for btn_manage in [btn_up, btn_down, btn_exit, btn_save]:
            btn_manage.bind("<Enter>", lambda e, x=btn_manage: self.on_enter(x))
            btn_manage.bind("<Leave>", lambda e, x=btn_manage: self.on_leave(x))

        return btn_up, btn_down, btn_exit, btn_save

    def create_eng_operators_button(self):
        btn_eng_objs=[]
        for operator in self.eng_operators:
            btn_eng_operator = tk.Button(
                master=self.button_frame,
                text=operator,
                relief=tk.GROOVE,
                width=BTN_DIGIT_WIDTH,
                height=BTN_DIGIT_HEIGHT,
                fg=BTN_SPECIAL_FG,
                bg=BTN_SPECIAL_BG,
                activebackground=BTN_SPECIAL_ACTIVE_BG,
                activeforeground=BTN_SPECIAL_ACTIVE_FG,
                font=BTN_FONT,
                borderwidth=0,
                command= lambda x=operator: self.click_button(x),
            )
            btn_eng_objs.append(btn_eng_operator)
            
            # Hovering over special buttons
            btn_eng_operator.bind("<Enter>", lambda e, x=btn_eng_operator: self.on_enter(x))
            btn_eng_operator.bind("<Leave>", lambda e, x=btn_eng_operator: self.on_leave(x))
        return btn_eng_objs

    def click_button(self, text):
        """
        run when user click some button like numbers and etc.
        
        Args:
            text(str): the string that user entered by click button
        """
        current = self.lbl_show_result['text']
        if current in ['0', 'Error']:
            if text in ['+','-','*','/','%','.','²']:
                self.lbl_show_result['text'] = '0' + text
            elif text in ['Del', '=']:
                self.lbl_show_result['text'] = '0'
            elif text == '↓':
                click_down(self.lbl_show_result, self.lb_hist)
            elif text == '↑':
                click_up(self.lbl_show_result, self.lb_hist)
            else:
                self.lbl_show_result['text'] = text
        elif text == '=':
            click_equal(self.lbl_show_result, self.lb_hist, current)
        elif (text in ['+','-','*','/'] and current[-1] in ['+','-','*','/']):
            self.lbl_show_result['text'] = current[:-1] + text
        elif text == '%':
            click_percent(self.lbl_show_result, current, text)
        elif text in ['sin(','cos(','tan(']:
            click_trigonometry(self.lbl_show_result, current, text)
        elif text == 'log(':
            click_log(self.lbl_show_result, current, text)
        elif text == 'ln(':
            click_ln(self.lbl_show_result, current, text)
        elif text == 'pi':
            click_pi(self.lbl_show_result, current, text)
        elif text == 'e':
            click_e(self.lbl_show_result, current, text)
        elif text == '(':
            if not current[-1] in ['+','-','*','/','(']:
                self.lbl_show_result['text'] = self.lbl_show_result['text'] + '*' + text
            else:
                self.lbl_show_result['text'] = self.lbl_show_result['text'] + text 
        elif text == '²':
            click_pow(self.lbl_show_result, current, text)
        elif (text.isdigit() and current[-1] == ['%','sin(']):
            pass
        elif text == '.':
            click_point(self.lbl_show_result, current, text)
        elif text == 'Del':
            click_del(self.lbl_show_result, current)
        elif text =='↑':
            click_up(self.lbl_show_result, self.lb_hist)
        elif text =='↓':
            click_down(self.lbl_show_result, self.lb_hist)
        else:
            self.lbl_show_result['text'] = self.lbl_show_result['text'] + text

        # for edit name of AC button to C
        if self.lbl_show_result['text'] == '0':
            self.btn_clear['text'] = 'AC'
        else:
            self.btn_clear['text'] = 'C'


    def on_enter(self, btn, *args):
        """used for help to hovering buttons"""
        if btn.cget('bg') == BTN_DIGIT_BG:
            btn['background'] = '#d6e9f0'
        elif btn.cget('bg') == BTN_AC_DEL_BG:
            btn['background'] = '#ffa329'
        elif btn.cget('bg') == BTN_MANAGE_BG:
            btn['background'] = '#575757'
        elif btn.cget('bg') == BTN_SPECIAL_BG:
            btn['background'] = '#8349da'



    def on_leave(self, btn, *args):
        """used for help to hovering buttons"""
        if btn.cget('bg') == '#d6e9f0':
            btn['background'] = BTN_DIGIT_BG
        elif btn.cget('bg') == '#ffa329':
            btn['background'] = BTN_AC_DEL_BG
        elif btn.cget('bg') == '#575757':
            btn['background'] = BTN_MANAGE_BG
        elif btn.cget('bg') == '#8349da':
            btn['background'] = BTN_SPECIAL_BG


    def binding(self):
        for digit in self.digits.keys():
            self.window.bind(str(digit), lambda e, x=str(digit): self.click_button(x))
        for operator in self.simple_operators.keys():
            self.window.bind(operator, lambda e, x=operator: self.click_button(x))
        for operator in self.eng_operators[:-1]:
            self.window.bind(f"<Alt-{operator[0]}>", lambda e, x=operator: self.click_button(x))
        
        self.window.bind("(", lambda e, x='(': self.click_button(x))
        self.window.bind(")", lambda e, x=')': self.click_button(x))
        self.window.bind("@", lambda e, x='²': self.click_button(x))
        self.window.bind("<Control-l>", lambda e, x='log(': self.click_button(x))
        self.window.bind("<Up>", lambda e, x='↑': self.click_button(x))
        self.window.bind("<Down>", lambda e, x='↓': self.click_button(x))
        self.window.bind("<Control-s>", lambda e: click_save(self.lb_hist))
        self.window.bind("<Escape>", lambda e: click_exit(self.window))
        self.window.bind("c", lambda e: click_AC_C(self.lbl_show_result, self.lb_hist, self.btn_clear))
        self.window.bind("<Delete>", lambda e, x='Del': self.click_button(x))
        self.window.bind("<Return>", lambda e, x='=': self.click_button(x))
        self.window.bind("e", lambda e: on_eng(self.btn_eng_objs, self.btn_manage_objs, self.btn_eng, self.window))


    def run(self):
        self.window.mainloop()

if __name__ == '__main__':
    calc = Calculator()
    calc.run()