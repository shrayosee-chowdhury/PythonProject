import tkinter as tk
from random import randint


root = tk.Tk()
root.title("Lets Play Quiz")
root.geometry("500x400")
root.configure(bg="midnightblue")  


root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Heading Label
headingLabel = tk.Label(root, text="Start Quiz", font=('calibre', 20), relief="solid", borderwidth=3, padx=10, pady=5, bg="white")
headingLabel.grid(row=0, column=0, pady=20, columnspan=2)

# Question Label
questionLabel = tk.Label(root, text="", font=('calibre', 16), bg="lightblue")
questionLabel.grid(row=1, column=0, pady=10, columnspan=3)

# Answer Entry
ansEntry = tk.Entry(root, font=('arial', 20), justify="center")
ansEntry.grid(row=2, column=0, columnspan=2, pady=10)

# Result Label
resultLabel = tk.Label(root, text="", font=('calibre', 16), bg="lightblue")
resultLabel.grid(row=4, column=0, pady=10, columnspan=3)


# Timer Label
timerLabel = tk.Label(root, text="Time Left: 10s", font=('calibre', 16), bg="white", fg="red")
timerLabel.grid(row=3, column=0, pady=10, columnspan=2)



time_left = 10
timer_id = None  



def update_timer():
    global time_left, timer_id
    if time_left > 0:
        time_left -= 1
        submitButton.config(text=f"Submit ({time_left}s)")
        timer_id = root.after(1000, update_timer)  
    else:
        resultLabel.config(text="Times Up", fg="red")
        ansEntry.config(state="disabled")  
        submitButton.config(text="Times Up", state="disabled")  



def generate_question():
    global n1, n2, answer, time_left, timer_id

    
    if timer_id:
        root.after_cancel(timer_id)
    
    n1 = randint(1, 10)
    n2 = randint(1, 10)
    answer = n1 + n2
    
 
    questionLabel.config(text=f"Question: {n1} + {n2}")
    resultLabel.config(text="")
    ansEntry.config(state="normal")  
    ansEntry.delete(0, tk.END)  
    time_left = 10  
    submitButton.config(text=f"Submit ({time_left}s)", state="normal")  

    
    update_timer()



def check_answer():
    global time_left
    user_answer = ansEntry.get()
    
    try:
        if int(user_answer) == answer:
            resultLabel.config(text="Correct!", fg="green")
            submitButton.config(text="Correct!", state="disabled")  
            root.after_cancel(timer_id)  
        else:
            resultLabel.config(text="Incorrect. Try again.", fg="red")
    except ValueError:
        resultLabel.config(text="Please enter a valid number.", fg="red")


def restart_quiz():
    generate_question()  



submitButton = tk.Button(root, text=f'Submit ({time_left}s)', font=('arial', 16), command=check_answer, bg="white")
submitButton.grid(row=3, column=0, pady=10, sticky="nsew")
restartButton = tk.Button(root, text='Restart', font=('arial', 16), command=restart_quiz, bg="white")
restartButton.grid(row=3, column=1, pady=10, sticky="nsew")

generate_question()
root.mainloop()
