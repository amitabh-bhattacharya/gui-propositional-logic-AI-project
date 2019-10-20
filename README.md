## AI gui project using python tkinter

### Project description

This project is an easy-to-use GUI (using the Python Tkinter module) for collecting names of attributes and their values, hard constraints, and preferences. The output of the project is providing of reasoning. 

 •	Attributes (A) in this project are binary.
 •	Hard constraints (H) are represented as propositional formulas in the Conjunctional Normal Form (CNF).
 •	The system supports preferences (T) in the preference language of penalty logic. Formulas involved in the preference theories are of    CNF as well.
  
#### The system supports the following reasoning tasks -

•	Existence of feasible objects: deciding whether there are feasible objects w.r.t H, that is, whether there are models of H that are truth assignments making H true.
•	Exemplification: generating, if possible, two random feasible objects, and showing the preference between the two (strict preference  or equivalence) w.r.t T.
•	Optimization: finding an optimal object w.r.t T.
•	Omni-optimization: finding all optimal objects w.r.t T.


#### Packages used -

Tkinter, ScrolledText, subprocess, tkMessageBox

#### Project execution -

The project should be unpacked in place where there is a permission for the current user to create new files. During the course of the program execution project3 will create new files. Those files will be deleted when the purpose is achieved excepth the last file. The files that would be created on the fly are hc_clasp_file.txt, hc_clasp_output.txt, 
pref_clasp_file.txt

Input_Description.txt file provides a detailed explanation of all the input files required as input to the project.

To execute the project open cmd editor for Windows and enter the below command

>python project.py

#### Execution steps -

Once the GUI is open, by executing the above command, we should do mainly 7 different operations to start quering the engine. The sequesnce of operations are explained below:

Step 1.) Click -> 'Step 1: UPLOAD ATTRIBUTES' button to load the attributes in the file A_Input.txt. After succesfull upload, the button text changes to 'SUCCESS!!! ATTRIBUTES LOADED'

Step 2.) Click -> 'Step 2: UPLOAD CONSTRAINTS' button to load the hard constraints in the file HC_Input.txt. After succesfull upload, the button text changes to 'SUCCESS!!! CONSTRAINTS LOADED'

Step 3.) Click -> 'Step 3: UPLOAD PREFERENCES' button to load the preferences in the file P_Input.txt. After succesfull upload, the button text changes to 'SUCCESS!!! PREFERENCES LOADED'

Step 4.) Enter some more attributes (if any) in attributes text box. Click -> 'Insert attributes' button to upload them to the program. Note: Improperly formatted input would not be accepted by the system and an error message would be displayed in the text box. Use 'Clear' button to clear the garbage data or clear the typing errors. We can start entering fresh data after a text clear operation.

Step 5.) Enter some more hard constraints (if any) in constraints text box. Click -> 'Insert constraints' button to upload them to the program. Note: Improperly formatted input would not be accepted by the system and an error message would be displayed in the text box. Use 'Clear' button to clear the garbage data or clear the typing errors.

Step 6.) Enter more preferences (if any) in preferences text box. Click -> 'Insert preferences' button to upload them to the program. 

Make a note that this project uses clasp software (provided in the repository) to calculate feasible objects and preference value.

Step 7.) A MUST OPERATION BEFORE QUERING THE PROJECT. Click -> "PROCESS DATA (Must before query execution)". This performs all computations of feasible objects from the w.r.t. the input data. It also calculates the preference values of all the feasible objects. It is a time consuming job (around 5 minutes time in average computer).


#### Queries/Results -

There is separate area for each query requested in the project. Clicking on the appropriate button will answer the query in the respective display text box. Make a note that each query can be executed multiple times for different results.
