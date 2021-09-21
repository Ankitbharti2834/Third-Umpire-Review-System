#!/usr/bin/env python
# coding: utf-8

# In[2]:


pip install tk


# In[3]:


pip install opencv-python


# In[4]:


pip install pyimage


# In[5]:


pip install pillow


# In[6]:


from tkinter import *
import PIL.Image, PIL.ImageTk
import cv2


# In[7]:


from functools import partial


# In[8]:


pip install threaded


# In[9]:


import tkinter


# In[10]:


import threading 


# In[11]:


import imutils
import time


# In[ ]:


# Width and Height of our main screen....
Set_width= 750       
Set_height= 405

stream= cv2.VideoCapture("Clip.mp4")
# Play function...
def play(speed):
    print(f"You Clicked on Play Speed is {speed}")
    
    # Reverse mode
    frame1= stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    grabbed,frame = stream.read()
    print("Done successful",frame1)
    
    frame= imutils.resize(frame, width= Set_width, height= Set_height)
    frame= PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0,0, image=frame, anchor= tkinter.NW)
    

    # pending function...
def pending(decision):
    # Display decision pending image
    frame=cv2.cvtColor(cv2.imread("Decision Pending.jpg"), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width= Set_width, height= Set_height)
    frame= PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.image= frame
    canvas.create_image(0, 0, image= frame, anchor= tkinter.NW)
    # Wait for 2 second
    time.sleep(2)
    # Display sponsor image
    frame=cv2.cvtColor(cv2.imread("Sponsor.jpg"), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width= Set_width, height= Set_height)
    frame= PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0,0, image=frame, anchor=tkinter.NW)
    # Wait for 2 second
    time.sleep(2)
    
    # Display out/not out image
    if decision=='not_out':
        a="Not Out.png"
        decisionImg= a
    else:
        decisionImg= "Out.png"
        
    frame=cv2.cvtColor(cv2.imread(decisionImg), cv2.COLOR_BGR2RGB)
    frame=imutils.resize(frame, width= Set_width, height= Set_height)
    frame= PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(frame))
    canvas.image=frame
    canvas.create_image(0, 0, image=frame, anchor= tkinter.NW)
    # Wait for 2 second
    time.sleep(2)

# Out function....
def out():
    thread= threading.Thread(target=pending, args=("out",))
    thread.daemon=1
    thread.start()
    print("It's Out")
    
# Not out function...
def not_out():
    thread= threading.Thread(target=pending, args=("not_out",))
    thread.daemon=1
    thread.start()
    print("It's Not Out")
    

# GUI tkinter...
window= tkinter.Tk()
window.title(" Third Umpire Decision Review")
cv_img=cv2.cvtColor(cv2.imread("TUDRS.png "), cv2.COLOR_BGR2RGB)
cv2.imwrite("TUDRS.png",cv_img)
canvas= tkinter.Canvas(window, width= Set_width, height= Set_height)
photo = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(cv_img))
image_on_canvas = canvas.create_image(0, 0, anchor= tkinter.NW, image= photo)
canvas.pack()


# Playback Buttons
button= tkinter.Button(window, text="<< Previous (fast)",width=50,command=partial(play,-25))
button.pack()
button= tkinter.Button(window, text="<  Previous (slow)",width=50, command=partial(play, -2))
button.pack()
button= tkinter.Button(window, text=" Forward (fast) >>", width=50, command=partial(play, 25))
button.pack()
button= tkinter.Button(window, text=" Forward (slow)  >", width=50, command=partial(play, 2))
button.pack()
button=tkinter.Button(window, text=" Out",width=50,command=out)
button.pack()
button= tkinter.Button(window,text=" Not Out", width=50, command= not_out)
button.pack()


window.mainloop()


# In[ ]:




