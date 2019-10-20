# -*- coding: utf-8 -*-
"""
This program is towards the CAP 4630/5605 AI project-3.

Author: Amitabh Bhattacharya
Version: 3/20/2019
Email: n01412146@ospreys.unf.edu

"""

import Tkinter as tk
from Tkinter import *
from ScrolledText import ScrolledText
import os
import subprocess
import random
import tkMessageBox

root = tk.Tk()
root.geometry("900x675")

root.title("Project 3: CAP 4630/5605 - Introduction to AI (Spring 2019)")

#####################################################################

attributes_list = []
attributes_dict = {}
attributes_loaded = False

def read_attributes():
    """ This method reads the attribute list from a file. The file with appropriate
    attributes input in CNF form should be present before executing this method.
    This method will be executed by the "Step 1: UPLOAD ATTRIBUTES" button in the
    GUI.
    
    Parameters: Nil
    Returns: Nil
    """
    global attributes_list
    global attributes_dict
    global attributes_loaded
    
    if not attributes_loaded:
        with open('A_Input.txt', 'r') as attribute_file:
            for line in attribute_file:
                tmp = line.split(':', 1)
                attributes_list.append(tmp[0].strip())
                attributes_dict.update({tmp[0].strip(): list(x.strip() \
                                        for x in tmp[1].split(','))})
    
            attributes_loaded = True
            button_l.configure(text='SUCCESS!!! ATTRIBUTES LOADED')
            attribute_file.close()
    
            """
            for key, value in attributes_dict.items():
                print key + ": " + ' '.join(value) + ','
            for item in attributes_list:
                print str(attributes_list.index(item) + 1) + ", " + item
            """
        
    
#####################################################################
        
hc_list = []
hc_loaded = False

def read_hc():
    """ This method reads the hard constraints list from a file. The file with 
    appropriate constraints input in CNF form should be present before 
    executing this method. This method will be executed by the 
    "Step 2: UPLOAD CONSTRAINTS" button in the GUI.
    
    Parameters: Nil
    Returns: Nil
    """
    global hc_list
    global attributes_list
    global attributes_dict
    global attributes_loaded
    global hc_loaded
    
    if not attributes_loaded:
        print 'Please update first the attributes'
        return
    
    if not hc_loaded:
        with open('HC_Input.txt', 'r') as hc_file:
            for line in hc_file:
                single_hc = []
                tmp_p1 = line.split('OR')
                for tmp in tmp_p1:                
                    tmp_p2 = tmp.strip()                
                    if tmp_p2.startswith('NOT'):
                        tmp_p3 = tmp_p2[4:]
                        for key, values in attributes_dict.items():
                            if tmp_p3 in values:
                                if values.index(tmp_p3)==0:
                                    single_hc.append(-1*(attributes_list.index(key) + 1))
                                else:
                                    single_hc.append(attributes_list.index(key) + 1)                                
                    else:
                        tmp_p3 = tmp_p2                    
                        for key, values in attributes_dict.items():                        
                            if tmp_p3 in values:                            
                                if values.index(tmp_p3)==0:                               
                                    single_hc.append(attributes_list.index(key) + 1)
                                else:
                                    single_hc.append(-1*(attributes_list.index(key) + 1))
            
                single_hc.append(0)           
                hc_list.append(single_hc)
            hc_loaded = True
            button_m.configure(text='SUCCESS!!! HARD CONSTRAINTS LOADED')
            hc_file.close()    
    """
    for item in hc_list:
        print str(item)
    """
    
#####################################################################
        
preference_list = []
preference_loaded = False

def read_preferences():
    """ This method reads the preference list from a file. The file with 
    appropriate preferences input should be present before executing this method. 
    This method will be executed by the "Step 3: UPLOAD PREFERENCES" button in 
    the GUI.
    
    Parameters: Nil
    Returns: Nil
    """
    
    global preference_list
    global attributes_list
    global attributes_dict
    global preference_loaded
    global attributes_loaded
       
    if not attributes_loaded:
        print 'Please update first the attributes'
        return
    if not preference_loaded:
        with open('P_Input.txt', 'r') as pref_file:
            for line in pref_file:  
                single_preference = []                      
                tmp_p1 = line.split(',')
                # Process tmp_p1[0] and add it in single_preference list
                tmp_p2 = tmp_p1[0].split('AND')
            
                for item in tmp_p2: 
                    tmp_list = []
                    for tmp_p3 in item.split('OR'):
                        if tmp_p3.strip().startswith('NOT'):
                            tmp_p4 = tmp_p3.strip()[4:]
                            for key, values in attributes_dict.items():
                                if tmp_p4 in values:
                                    if values.index(tmp_p4)==0:
                                        tmp_list.append(-1*(attributes_list.index(key) + 1))
                                    else:
                                        tmp_list.append(attributes_list.index(key) + 1)                                
                        else:
                            tmp_p4 = tmp_p3.strip()
                            for key, values in attributes_dict.items():
                                if tmp_p4 in values:
                                    if values.index(tmp_p4)==0:
                                        tmp_list.append(attributes_list.index(key) + 1)
                                    else:
                                        tmp_list.append(-1*(attributes_list.index(key) + 1))
            
                    single_preference.append(tmp_list)
                single_preference.append(int(tmp_p1[1].strip()))
                preference_list.append(single_preference)
            
            preference_loaded = True
            button_r.configure(text='SUCCESS!!! PREFERENCES LOADED')
            pref_file.close()    
    """
    for item in preference_list:
        print str(item)
    """

#####################################################################


button_l = tk.Button(root, text='Step 1: UPLOAD ATTRIBUTES', \
                     command=read_attributes, bg='pink', fg='black')
# button_l.pack()
button_l.place(x=0, y=0, height=50, width=300)

button_m = tk.Button(root, text='Step 2: UPLOAD CONSTRAINTS', \
                     command=read_hc, bg='pink', fg='black')
button_m.place(x=300, y=0, height=50, width=300)

button_r = tk.Button(root, text='Step 3: UPLOAD PREFERENCES', \
                     command=read_preferences, bg='pink', fg='black')
button_r.place(x=600, y=0, height=50, width=300)


#####################################################################

def insert_attributes():
    """ This method reads the attribute list provided in the attributes test box. 
    The input text should be in CNF form. Exception would be raised if inproper
    input is provided. This method will be executed by the "Insert attributes" 
    button in the GUI.
    
    Parameters: Nil
    Returns: Nil
    """
    global attributes_list
    global attributes_dict
    global attributes_loaded
    
    att_input = att_text.get('1.0','end-1c')    
    
    try:
        att_input_split = att_input.split('\n')
    
        """
        for line in att_input_split:
            print line
        """
        
        for line in att_input_split:
            tmp = line.split(':', 1)
            attributes_list.append(tmp[0].strip())
            attributes_dict.update({tmp[0].strip(): list(x.strip() for x in tmp[1].split(','))})
    
        """
        for key, value in attributes_dict.items():
            print key + " - " + ' '.join(value)
        for item in attributes_list:
            print str(attributes_list.index(item) + 1) + ", " + item  
        """
    except:
        att_text.delete('1.0', END)
        att_text.insert('1.0', "Please enter input in CNF form only." + \
                        " Example: a: a1, a2") 
    
def clr_attributes():
    att_text.delete('1.0', END)    

att_msg = Message(root, text='Enter more attributes here:', \
                  fg='red', width=250)
att_msg.place(x=0, y=75)

att_text = ScrolledText(root, height=6, width=33)
att_text.pack()
att_text.place(x=2, y=100)

att_button_ins = Button(root, height=1, width=18, text="Insert attributes", \
                        command = insert_attributes, bg='grey')
att_button_ins.place(x=5, y=210)

att_button_clr = Button(root, height=1, width=18, text="Clear", \
                        command = clr_attributes, bg='grey')
att_button_clr.place(x=150, y=210)

#####################################################################
   
def insert_hc():
    global hc_list
    global attributes_list
    global attributes_dict
    global attributes_loaded
    global hc_loaded
    
    if not attributes_loaded:
        print 'Please update first the attributes'
        return
    
    hc_input = hc_text.get("1.0","end-1c")
    
    try:    
        hc_input_split = hc_input.split('\n')    
        """
        for line in hc_input_split:
            print line
        """
    
        for line in hc_input_split:
            single_hc = []
            tmp_p1 = line.split('OR')
            for tmp in tmp_p1:                
                tmp_p2 = tmp.strip()                
                if tmp_p2.startswith('NOT'):
                    tmp_p3 = tmp_p2[4:]
                    for key, values in attributes_dict.items():
                        if tmp_p3 in values:
                            if values.index(tmp_p3)==0:
                                single_hc.append(-1*(attributes_list.index(key) + 1))
                            else:
                                single_hc.append(attributes_list.index(key) + 1)                                
                else:
                    tmp_p3 = tmp_p2                    
                    for key, values in attributes_dict.items():                        
                        if tmp_p3 in values:                            
                            if values.index(tmp_p3)==0:                               
                                single_hc.append(attributes_list.index(key) + 1)
                            else:
                                single_hc.append(-1*(attributes_list.index(key) + 1))
            
            single_hc.append(0)           
            hc_list.append(single_hc)    
        """
        for item in hc_list:
            print str(item)
        """    
    except:
        hc_text.delete('1.0', END)
        hc_text.insert('1.0', "Please enter input in CNF form only." + \
                       " Example: NOT c2 OR b1") 

def clr_hc():
    hc_text.delete('1.0', END)   
    
hc_msg = Message(root, text='Enter more hard constraints here (in CNF form only):', \
                 fg='red', width=300)
hc_msg.place(x=300, y=75)

hc_text = ScrolledText(root, height=6, width=33)
hc_text.pack()
hc_text.place(x=302, y=100)

hc_button_ins = Button(root, height=1, width=18, text="Insert constraints", \
                       command = insert_hc, bg='grey')
hc_button_ins.place(x=305, y=210)

hc_button_clr = Button(root, height=1, width=18, text="Clear", \
                       command = clr_hc, bg='grey')
hc_button_clr.place(x=455, y=210)

#####################################################################
    
def insert_preferences():
    global preference_list
    global attributes_list
    global attributes_dict
    global preference_loaded
    global attributes_loaded
       
    if not attributes_loaded:
        print 'Please update first the attributes'
        return
    
    pref_input = pref_text.get("1.0","end-1c")
    
    try:
        pref_input_split = pref_input.split('\n')    
        """
        for line in pref_input_split:
            print line
        """
    
        for line in pref_input_split:  
            single_preference = []                      
            tmp_p1 = line.split(',')               
            tmp_p2 = tmp_p1[0].split('AND')
            
            for item in tmp_p2: 
                tmp_list = []
                for tmp_p3 in item.split('OR'):
                    if tmp_p3.strip().startswith('NOT'):
                        tmp_p4 = tmp_p3.strip()[4:]
                        for key, values in attributes_dict.items():
                            if tmp_p4 in values:
                                if values.index(tmp_p4)==0:
                                    tmp_list.append(-1*(attributes_list.index(key) + 1))
                                else:
                                    tmp_list.append(attributes_list.index(key) + 1)                                
                    else:
                        tmp_p4 = tmp_p3.strip()
                        for key, values in attributes_dict.items():
                            if tmp_p4 in values:
                                if values.index(tmp_p4)==0:
                                    tmp_list.append(attributes_list.index(key) + 1)
                                else:
                                    tmp_list.append(-1*(attributes_list.index(key) + 1))
            
                single_preference.append(tmp_list)
            single_preference.append(int(tmp_p1[1].strip()))
            preference_list.append(single_preference)        
        """
        for item in preference_list:
            print str(item)
        """
    except:
        pref_text.delete('1.0', END)
        pref_text.insert('1.0', "Please enter input in standard preference syntax." + \
                         " Example: a2 AND b1, 7") 
    
tmp_str = """1
2
3"""

def clr_preferences():
    pref_text.delete('1.0', END)
    # pref_text.insert('1.0', tmp_str)    
    
pref_msg = Message(root, text='Enter more preferences here:', fg='red', \
                 width=250)
pref_msg.place(x=600, y=75)

pref_text = ScrolledText(root, height=6, width=33)
pref_text.pack()
pref_text.place(x=602, y=100)

pref_button_ins = Button(root, height=1, width=18, text="Insert preferences", \
                         command = insert_preferences, bg='grey')
pref_button_ins.place(x=605, y=210)

pref_button_clr = Button(root, height=1, width=18, text="Clear", \
                         command = clr_preferences, bg='grey')
pref_button_clr.place(x=755, y=210)

#####################################################################

feasible_objects = []
attribute_mapping = {}

def processing_data(): 
    """
    This method does the complete processing of the input data. 
    Step 1: It calculates the feasible objects
    Step 2: It calculates the preferences of the objects based on penalty logic.
    
    Parameters: Nil
    Returns: Nil
    """
    
    global attributes_list
    global feasible_objects
    global preference_list
    global attributes_list
    global attributes_dict    
    global attribute_mapping
    
    print "Data processing will start once OK is clicked in message box." + \
    " It will take around 5 minutes..."
    
    tkMessageBox.showinfo("Data processing message", "Data processing will" + \
                        " start once OK is clicked. It will take around 5 minutes...")
        
    process_data.configure(text='Data processing is in progress...')
    
    for idx, val in enumerate(attributes_list):
        t_list = attributes_dict.get(val)
        attribute_mapping.update({int(idx+1) : t_list[0]})
        attribute_mapping.update({int(-(idx+1)) : t_list[1]})    
    
    hc_clasp_file = 'hc_clasp_file.txt'
    try:
        os.remove(hc_clasp_file)
        os.remove("hc_clasp_output.txt")
    except OSError:
        pass
    
    with open(hc_clasp_file, 'w+') as hcf:
        hcf.write("p cnf " + str(len(attributes_list)) + ' ' + str(len(hc_list)) + '\n')
        for item1 in hc_list:
            tmp_str = ''
            for item2 in item1:
                tmp_str = tmp_str + str(item2) + ' '
            hcf.write(tmp_str + '\n')
        
    hcf.close()
    
    hc_command = "clasp.exe hc_clasp_file.txt -n 0"
    process = subprocess.Popen(hc_command.split(), stdout=subprocess.PIPE)
    hc_processing_output = process.communicate()[0]
    tmp_po_str = hc_processing_output.split('v ')
    cnt = 0
    
    if len(tmp_po_str) > 0:
        for idx, line in enumerate(tmp_po_str):
            if idx==0:
                pass
            else:
                cnt += 1
                tmp_list = [int(x.strip()) for x in line.split(' 0')[0].split()]
                tmp_list.append(int(0))
                tmp_list.insert(0, 'O_' + str(cnt))
                feasible_objects.append(tmp_list)          
        
    for obj in feasible_objects:
        for pref in preference_list:
            try:                
                os.remove("pref_clasp_file.txt")
            except OSError:
                pass
            
            with open("pref_clasp_file.txt", 'w+') as pcf:
                pcf.write('p cnf ' + str(len(attributes_list)) + ' ' + \
                          str(len(pref) - 1 + len(obj) - 2) + '\n')
                for i1 in pref[:-1]:
                    s1 = ''
                    for i2 in i1:
                        s1 = s1 + str(i2) + ' '
                    s1 = s1 + '0' + '\n'
                    pcf.write(s1)                
                for i3 in obj[1:-1]:                    
                    pcf.write(str(i3) + ' 0\n')
                    
            pcf.close()
            pref_command = "clasp.exe pref_clasp_file.txt -n 0"
            process = subprocess.Popen(pref_command.split(), stdout=subprocess.PIPE)
            pref_processing_output = process.communicate()[0]
            
            if pref_processing_output.find('UNSATISFIABLE') >= 0:
                obj[-1] = int(obj[-1]) + int(pref[-1])
            else:
                # obj[-1] = int(obj[-1]) + 0
                pass                
            
    # print feasible_objects   
        
    process_data.configure(text='Success!!! Data processing is done')  
    tkMessageBox.showinfo("Data processing message", "Data processing is" + \
                        " sucessfully done!!! Click Ok to continue")
                      
    print "Success!!! Data processing is done."

#####################################################################

def execute_q1():    
    global feasible_objects
    
    q1_text.delete('1.0', END)
    q1_text.insert('1.0', "There are " + str(len(feasible_objects)) + \
                   " feasible objects.")  

def clr_q1():
    q1_text.delete('1.0', END)  
    
process_data = Button(root, height=2, width=100, text="PROCESS DATA (Must before query execution)", \
                      command = processing_data, bg='pink')
process_data.place(x=5, y=260, height=50, width=430)

q1_text = ScrolledText(root, height=4, width=52)
q1_text.pack()
q1_text.place(x=2, y=320)

q1_button_ins = Button(root, height=1, width=29, text="Q1: Feasible objects?", \
                       command = execute_q1, bg='grey')
q1_button_ins.place(x=5, y=405)

q1_button_clr = Button(root, height=1, width=29, text="Clear", \
                        command = clr_q1, bg='grey')
q1_button_clr.place(x=220, y=405)

#####################################################################

def execute_q2():   
    global attributes_list
    global attributes_dict
    global feasible_objects
    global attribute_mapping    
        
    q2_text.delete('1.0', END)
    id1 = random.randint(0, len(feasible_objects)-1)
    id2 = random.randint(0, len(feasible_objects)-1)
    
    feasible_obj_str = feasible_objects[id1][0] + ": ["
    
    for it1 in feasible_objects[id1][1:-1]:
        feasible_obj_str = feasible_obj_str + attribute_mapping.get(int(it1)) + ", "
    feasible_obj_str = feasible_obj_str + "] Preference value: " + \
                       str(feasible_objects[id1][-1]) + "\n\n"
                       
    feasible_obj_str = feasible_obj_str + feasible_objects[id2][0] + ": ["
                       
    for it1 in feasible_objects[id2][1:-1]:
        feasible_obj_str = feasible_obj_str + attribute_mapping.get(int(it1)) + ", "
    feasible_obj_str = feasible_obj_str + "] Preference value: " + \
                       str(feasible_objects[id2][-1]) + "\n\n"
    
    if int(feasible_objects[id1][-1]) > int(feasible_objects[id2][-1]):
        feasible_obj_str = feasible_obj_str + feasible_objects[id1][0] + " has " + \
        "lower preference over " + feasible_objects[id2][0] + "\n"
    elif int(feasible_objects[id1][-1]) == int(feasible_objects[id2][-1]):
        feasible_obj_str = feasible_obj_str + feasible_objects[id1][0] + " has " + \
        "same preference as " + feasible_objects[id2][0] + "\n"
    else:
        feasible_obj_str = feasible_obj_str + feasible_objects[id1][0] + " has " + \
        "higher preference over " + feasible_objects[id2][0] + "\n"
    
    q2_text.insert('1.0', feasible_obj_str)  
    
def clr_q2():   
    q2_text.delete('1.0', END) 
    
q2_text = ScrolledText(root, height=8, width=52)
q2_text.pack()
q2_text.place(x=452, y=260)

q2_button_ins = Button(root, height=1, width=29, text="Q2: 2 Random feasible objects?", \
                       command = execute_q2, bg='grey')
q2_button_ins.place(x=460, y=405)

q2_button_clr = Button(root, height=1, width=29, text="Clear", \
                       command = clr_q2, bg='grey')
q2_button_clr.place(x=675, y=405)

#####################################################################

def execute_q3():  
    global feasible_objects
    global attribute_mapping
    
    q3_text.delete('1.0', END)    
    
    min_val = min([item[-1] for item in feasible_objects])
    feasible_obj_str = ''
    
    for id1, obj in enumerate(feasible_objects):
        if obj[-1] == min_val:
            feasible_obj_str = feasible_obj_str + feasible_objects[id1][0] + ": ["
            for it1 in feasible_objects[id1][1:-1]:
                feasible_obj_str = feasible_obj_str + attribute_mapping.get(int(it1)) + ", "
            feasible_obj_str = feasible_obj_str + "] Preference value: " + \
                    str(feasible_objects[id1][-1]) + "\n"
            break
        
    q3_text.insert('1.0', feasible_obj_str)  
    
def clr_q3():
    q3_text.delete('1.0', END)    

q3_text = ScrolledText(root, height=8, width=52)
q3_text.pack()
q3_text.place(x=2, y=460)

q3_button_ins = Button(root, height=1, width=29, text="Q3: An optimal object?", \
                       command = execute_q3, bg='grey')
q3_button_ins.place(x=2, y=605)

q3_button_clr = Button(root, height=1, width=29, text="Clear", \
                       command = clr_q3, bg='grey')
q3_button_clr.place(x=220, y=605)

#####################################################################


def execute_q4():    
    global feasible_objects
    global attribute_mapping
    
    q4_text.delete('1.0', END)    
    
    min_val = min([item[-1] for item in feasible_objects])
    feasible_obj_str = ''
    
    for id1, obj in enumerate(feasible_objects):
        if obj[-1] == min_val:
            feasible_obj_str = feasible_obj_str + feasible_objects[id1][0] + ": ["
            for it1 in feasible_objects[id1][1:-1]:
                feasible_obj_str = feasible_obj_str + attribute_mapping.get(int(it1)) + ", "
            feasible_obj_str = feasible_obj_str + "] Preference value: " + \
                    str(feasible_objects[id1][-1]) + "\n\n"     
                    
    q4_text.insert('1.0', feasible_obj_str)  
    
    
def clr_q4():
    q4_text.delete('1.0', END)    

q4_text = ScrolledText(root, height=8, width=52)
q4_text.pack()
q4_text.place(x=452, y=460)

q4_button_ins = Button(root, height=1, width=29, text="Q4: All optimal objects?", \
                       command = execute_q4, bg='grey')
q4_button_ins.place(x=460, y=605)

q4_button_clr = Button(root, height=1, width=29, text="Clear", \
                       command = clr_q4, bg='grey')
q4_button_clr.place(x=675, y=605)

#####################################################################

root.mainloop()
