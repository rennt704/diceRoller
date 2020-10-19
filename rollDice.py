#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:40:20 2020

@author: renny
"""

import random
import tkinter as tk
import tkinter.messagebox

root = tk.Tk()

def rollDice(n, o):
    """
    
    Parameters
    ----------
    n : int, size of die
    o : int, number of die

    Returns
    -------
    List containing results of rolls of die

    """
    
    vals = []
    answer = ', '
    for val in range(o):
        vals.append(str(random.randint(1, n)))
    return answer.join(vals)

def getDice(n, o):
    try:
        n = int(n)
        o = int(o)
    except:
        tk.messagebox.showinfo("Error", "Please enter a valid number")
    if int(n) < 1 or int(o) < 0:
        tk.messagebox.showinfo("Error", "Please enter a valid number")
    else:
        tk.messagebox.showinfo("Dice Rolls", rollDice(n, o))

    
## GUI
button = tk.Button(root, text="Roll Dice", bg ='#00ff99', command = lambda: getDice(E1.get(), E2.get()))
button.pack(side = 'bottom')

L1 = tk.Label(root, text="Size of Dice: ")
L1.pack(side = 'left')

E1 = tk.Entry(root, bd =5)
E1.pack(side = 'left')

L2 = tk.Label(root, text="Number of Dice: ")
L2.pack(side = 'left')

E2 = tk.Entry(root, bd =5)
E2.pack(side = 'right')

root.mainloop()