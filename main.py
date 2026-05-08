from tkinter import *
import csv
root = Tk()
root.title("Student Record System")
root.geometry("500x550")
root.config(bg="lightgreen")


# Title
title = Label(root,
    text="Student Record System",
    font=("Arial", 24, "bold"),
    bg="white")
title.pack(pady=15)

Label(root, text="Roll Number", font=("Arial", 12), bg="lightblue").pack()
roll_entry = Entry(root, width=30)
roll_entry.pack(pady=5)

Label(root, text="Student Name", font=("Arial", 12,), bg="lightblue").pack()
name_entry = Entry(root, width=30)
name_entry.pack(pady=5)

Label(root, text="Subject 1 Marks", font=("Arial", 12), bg="lightblue").pack()
sub1_entry = Entry(root, width=30)
sub1_entry.pack(pady=5)

Label(root, text="Subject 2 Marks", font=("Arial", 12), bg="lightblue").pack()
sub2_entry = Entry(root, width=30)
sub2_entry.pack(pady=5)

Label(root, text="Subject 3 Marks", font=("Arial", 12), bg="lightblue").pack()
sub3_entry = Entry(root, width=30)
sub3_entry.pack(pady=5)


# Function to calculate result
def calculate_result(event=None):
    try:
        sub1 = int(sub1_entry.get())
        sub2 = int(sub2_entry.get())
        sub3 = int(sub3_entry.get())
        total = sub1 + sub2 + sub3
        average = total / 3

        total_label.config(text=f"{name_entry.get()} | Total: {total}")
        average_label.config(text=f"Average: {average:.2f}")

    except ValueError:
        total_label.config(text="Enter valid numbers!")
        average_label.config(text="")


def save_record():
    roll = roll_entry.get()
    name = name_entry.get()

    sub1 = int(sub1_entry.get())
    sub2 = int(sub2_entry.get())
    sub3 = int(sub3_entry.get())
    total = sub1 + sub2 + sub3
    average = total / 3

    with open("students.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll, name, sub1, sub2, sub3, total, average])

    total_label.config(text="Record Saved Successfully!")

calculate_btn = Button(root, text="Calculate Result",
    font=("Arial", 12, "bold"), bg="red", fg="white",
    command=calculate_result)
calculate_btn.pack(pady=20)

save_btn = Button(root, text="Save Record",
    font=("Arial", 12, "bold"), bg="green", fg="white",
    command=save_record)
save_btn.pack(pady=5)

# Result Labels
total_label = Label(root, text="", font=("Arial", 12), bg="white")
total_label.pack()

average_label = Label(root, text="", font=("Arial", 12), bg="white")
average_label.pack()

roll_entry.bind("<Return>", lambda event: name_entry.focus())
name_entry.bind("<Return>", lambda event: sub1_entry.focus())
sub1_entry.bind("<Return>", lambda event: sub2_entry.focus())
sub2_entry.bind("<Return>", lambda event: sub3_entry.focus())
sub3_entry.bind("<Return>", calculate_result)
root.mainloop()
