import tkinter as tk
from tkinter import END, messagebox
from tkinter import ttk
import re
import math


def cos(x): 
    return math.cos(math.radians(x))

def sin(x): 
    return math.sin(math.radians(x))

def tan(x): 
    return math.tan(math.radians(x))

def log(x):
    return math.log(x,10)

def ln(x):
    return math.log(x,math.e)

def click_equal(lbl_show_result, lb_hist, current):
    """
    run when user click = button
    
    Args:
        current(str): contexts of lbl_show_result
    """
    pi = math.pi
    e = math.e
    if current[-1] in ['+','-','*','/','(']:
        current = current[:-1]
    if current [-1] == '.' and not current[-2].isdigit():
        current = current[:-1] +'0.0'
    try:
        current = current.replace('%','/100')
        current = current.replace('²','**2')
        lbl_show_result['text'] = f"{eval(current)}"
    except Exception:
        lbl_show_result['text'] = 'Error'
    finally:
        # calc_history.append((current + ' = ' + lbl_show_result['text']))
        lb_hist.insert(lb_hist.size()+1,(current + ' = ' + lbl_show_result['text']))

def click_percent(lbl_show_result, current, text):
    """
    run when user click % button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): %
    """
    test = re.split('\+|\-|\*|\/', current)
    if (('%' in test[-1]) or (test[-1] == '')):
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_trigonometry(lbl_show_result, current, text):
    """
    run when user click sin or cos or tan button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): sin( or cos( or tan(
    """
    test = re.split('\+|\-|\*|\/', current)
    if len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    elif len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    elif len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_log(lbl_show_result, current, text):
    """
    run when user click log button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): log(
    """
    test = re.split('\+|\-|\*|\/', current)
    if len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_ln(lbl_show_result, current, text):
    """
    run when user click ln button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): ln(
    """
    test = re.split('\+|\-|\*|\/', current)
    if len(test[-1]) != 0 and (test[-1][-1].isdigit() or test[-1][-1] in ['pi','e']):
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_pi(lbl_show_result, current, text):
    """
    run when user click π button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): pi
    """
    if current[-1] in ['+','-','*','/','(',]:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_e(lbl_show_result, current, text):
    """
    run when user click e button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): e
    """
    if current[-1] in ['+','-','*','/','(',]:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_pow(lbl_show_result, current, text):
    """
    run when user click power 2 button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): ²
    """
    if not current[-1] in ['+','-','*','/','%','(']:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_point(lbl_show_result, current, text):
    """
    run when user click . button
    
    Args:
        current(str): contexts of lbl_show_result
        text(str): .
    """
    if not re.split('\+|\-|\*|\/|\%', current)[-1].isdigit():
        pass
    else:
        lbl_show_result['text'] = lbl_show_result['text'] + text

def click_del(lbl_show_result, current):
    """
    run when user click Del button
    
    Args:
        current(str): contexts of lbl_show_result
    """
    if len(lbl_show_result['text']) > 1:
        test = re.split('\+|\-|\*|\/', current)
        check_list = ['sin(','cos(','tan(','log(']
        if any(ele in test[-1][-4:] for ele in check_list):
            lbl_show_result['text'] = lbl_show_result['text'][:-4]
        elif 'ln(' in test[-1][-3:]:
            lbl_show_result['text'] = lbl_show_result['text'][:-3]
        else:
            lbl_show_result['text'] = lbl_show_result['text'][:-1]
    else:
        lbl_show_result['text'] = lbl_show_result['text'][:-1] + '0'

def mouse_left_click(lbl_show_result, lb_hist, *args):
    """
    run when user use Left click of mouse
    
    Args:
        args : 'nothing'. just used for binding
    """
    try:
        j = lb_hist.curselection()[0]
        lbl_show_result['text'] = lb_hist.get(j).split(' = ')[0]
    except:
        pass

def click_up(lbl_show_result, lb_hist):
    """
    run when user click ↑ button
    
    Args:
        lb_hsit (listbox): lb_hist is the listbox that have calculation history
    """
    try:
        j = lb_hist.curselection()[0]
    except:
        j= lb_hist.size()

    if j != 0:
        lb_hist.selection_clear(j)
        j -= 1
        lb_hist.selection_set(j)
        lb_hist.see(j)
        lbl_show_result['text'] = lb_hist.get(j).split(' = ')[0]

def click_down(lbl_show_result, lb_hist):
    """
    run when user click ↓ button
    
    Args:
        lb_hsit (listbox): lb_hist is the listbox that have calculation history
    """
    try:
        j = lb_hist.curselection()[0]
        if lb_hist.size() != 0:
        
            if  j != lb_hist.size()-1:
                lb_hist.selection_clear(j)
                j += 1
                lb_hist.selection_set(j)
                lb_hist.see(j)
                lbl_show_result['text'] = lb_hist.get(j).split(' = ')[0]
            else:
                lb_hist.selection_clear(j)
                lbl_show_result['text'] = '0'
    except:
        pass

def store_file(fname, lb_hist, root):
    """
    run when user click on Save button in save history window
    
    Args:
        fname(str): name of textfile for storing
        root: window 
    """
    text_list = lb_hist.get(0, tk.END)
    with open(f'{fname}.txt', 'w') as f:
        f.writelines('\n'.join(text_list))
        f.close()
    root.destroy()

def click_save(lb_hist, *args):
    """
    run when user click save button in main window
    
    Args:
        args : 'nothing'. just used for binding
    """
    def handle_focus_in(_):
        """
        delete and replace example text by name of text file
        """
        ent_fname.delete(0, tk.END)
        ent_fname.config(fg='black')

    win2 = tk.Tk()
    # win2.iconbitmap(r"../myicon.ico")
    win2.title('Save History')
    win2.geometry('220x100')

    label = tk.Label(win2, text='Choose your textfile name:')
    label.grid(row=0, column=0, pady=(5,0))

    ent_fname = tk.Entry(win2, bg='white', width=30, fg='grey')
    ent_fname.grid(row=1, column=0, pady=5, padx=15)

    btn_name_save = ttk.Button(
        master=win2,
        text='Save',
        command= lambda: store_file(ent_fname.get(), lb_hist, win2)
    )
    btn_name_save.grid(row=2, column=0, pady=10)

    ent_fname.insert(0, "Example: textfile")
    ent_fname.bind("<FocusIn>", handle_focus_in)

    win2.mainloop()

def click_exit(master, *args):
    """
    run when user click Exit button
    
    Args:
        args : 'nothing'. just used for binding
    """
    ask_quit = messagebox.askquestion("Quit",
                           "Do you want to quit?")
    if ask_quit == 'yes':
        master.destroy()

def click_AC_C(lbl_show_result, lb_hist, btn_clear, *args):
    """
    run when user click AC/C button
    
    Args:
        args : 'nothing'. just used for binding
    """
    lbl_show_result['text'] = '0'
    if btn_clear['text'] == 'AC':
        lb_hist.delete(0,END)
    else:
        btn_clear['text'] = 'AC'

def off_eng(btn_eng_objs, btn_manage_objs, btn_eng, master, *args):
    """
    off Eng button 
    """
    for btn_eng_obj in btn_eng_objs:
        btn_eng_obj.grid_forget()
    for manage_btn_obj in btn_manage_objs:
        manage_btn_obj.grid_forget()

    btn_manage_objs[0].grid(row=2, column=2, columnspan=3, sticky='news')
    btn_manage_objs[1].grid(row=3, column=2, columnspan=3, sticky='news')
    btn_manage_objs[2].grid(row=2, column=5, rowspan=2, sticky='news')
    btn_manage_objs[3].grid(row=2, column=1, rowspan=2, sticky='news')

    btn_eng.configure(command= lambda: on_eng(btn_eng_objs, btn_manage_objs, btn_eng, master, *args))
    master.bind("e", lambda e: on_eng(btn_eng_objs, btn_manage_objs, btn_eng, master))


def on_eng(btn_eng_objs, btn_manage_objs, btn_eng, master, *args):
    """
    on Eng button
    """
    for i, btn_eng_obj in enumerate(btn_eng_objs):

        if i >=5:
            btn_eng_obj.grid(row=(i//10)+5, column=(i%5)+1, sticky='news')
        else:
            btn_eng_obj.grid(row=(i%5)+5, column=0, sticky='news')
    
    btn_manage_objs[0].grid(row=2, column=2, columnspan=2, sticky='news')
    btn_manage_objs[1].grid(row=3, column=2, columnspan=2, sticky='news')
    btn_manage_objs[2].grid(row=2, column=4, rowspan=2, columnspan=2, sticky='news')
    btn_manage_objs[3].grid(row=2, column=0, rowspan=2, columnspan=2, sticky='news')
 
    btn_eng.configure(command= lambda : off_eng(btn_eng_objs, btn_manage_objs, btn_eng, master, *args))
    master.bind("e", lambda e: off_eng(btn_eng_objs, btn_manage_objs, btn_eng, master))
