import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

import requests

# Define the API URL
api_url = 'http://localhost:8000/api/'

# Create the main window
root = tk.Tk()
root.title("Student Dashboard")
root.minsize(root.winfo_screenwidth() // 2, 400) # set minimum width to half the screen width

# Create the tabs
tab_control = ttk.Notebook(root)


view_complaints_tab = ttk.Frame(tab_control)


tab_control.add(view_complaints_tab, text='View Complaints')


add_complaint_tab = ttk.Frame(tab_control)
tab_control.add(add_complaint_tab, text='Add Complaint')

# Add Complaint Form
complaint_student_id_label = ttk.Label(add_complaint_tab, text='Student ID')
complaint_student_id_entry = ttk.Entry(add_complaint_tab)

complaint_type_label = ttk.Label(add_complaint_tab, text='Complaint Type')
complaint_type_entry = ttk.Entry(add_complaint_tab)

complaint_date_label = ttk.Label(add_complaint_tab, text='Date')
complaint_date_entry = ttk.Entry(add_complaint_tab)

complaint_desc_label = ttk.Label(add_complaint_tab, text='Description')
complaint_desc_entry = ttk.Entry(add_complaint_tab)

complaint_status_label = ttk.Label(add_complaint_tab, text='Status')
complaint_status_entry = ttk.Entry(add_complaint_tab)

def viewc():
    import listc
    listc.open_window()

def add_complaint():
    complaint_data = {
        'studentid': complaint_student_id_entry.get(),
        'complainttype': complaint_type_entry.get(),
        'date': complaint_date_entry.get(),
        'description': complaint_desc_entry.get(),
        'status': complaint_status_entry.get(),
        'severity': 'Low' # Default severity set to low
    }

    viewc()
    
    # Make POST request to REST API
    response = requests.post('http://localhost:8000/api/complaint/', data=complaint_data)
    
    # Show success message
    messagebox.showinfo('Success', 'Complaint added successfully')
    
    # Clear the form
    complaint_student_id_entry.delete(0, tk.END)
    complaint_type_entry.delete(0, tk.END)
    complaint_date_entry.delete(0, tk.END)
    complaint_desc_entry.delete(0, tk.END)
    complaint_status_entry.delete(0, tk.END)

add_complaint_button = ttk.Button(add_complaint_tab, text='Add Complaint', command=add_complaint)

complaint_student_id_label.grid(row=0, column=0, padx=5, pady=5)
complaint_student_id_entry.grid(row=0, column=1, padx=5, pady=5)

complaint_type_label.grid(row=1, column=0, padx=5, pady=5)
complaint_type_entry.grid(row=1, column=1, padx=5, pady=5)

complaint_date_label.grid(row=2, column=0, padx=5, pady=5)
complaint_date_entry.grid(row=2, column=1, padx=5, pady=5)

complaint_desc_label.grid(row=3, column=0, padx=5, pady=5)
complaint_desc_entry.grid(row=3, column=1, padx=5, pady=5)

complaint_status_label.grid(row=4, column=0, padx=5, pady=5)
complaint_status_entry.grid(row=4, column=1, padx=5, pady=5)



add_complaint_button.grid(row=5, columnspan=2, padx=5, pady=5)




def api_call(endpoint, method='GET', data=None):
    base_url = 'http://localhost:8000/api/'  # replace with your server's base URL
    url = base_url + endpoint
    headers = {'Content-Type': 'application/json'}
    response = requests.request(method=method, url=url, headers=headers, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Error {response.status_code}: {response.reason}')
        return None



# View Complaints Tab
view_complaints_tree = ttk.Treeview(view_complaints_tab, columns=('StudentID', 'ComplaintType', 'Date', 'Description', 'Status', 'Severity'))
view_complaints_tree.heading('#0', text='ID')
view_complaints_tree.heading('StudentID', text='Student ID')
view_complaints_tree.heading('ComplaintType', text='Complaint Type')
view_complaints_tree.heading('Date', text='Date')
view_complaints_tree.heading('Description', text='Description')
view_complaints_tree.heading('Status', text='Status')
view_complaints_tree.heading('Severity', text='Severity')

view_complaints_tree.column('#0', width=50)
view_complaints_tree.column('StudentID', width=100)
view_complaints_tree.column('ComplaintType', width=150)
view_complaints_tree.column('Date', width=100)
view_complaints_tree.column('Description', width=200)
view_complaints_tree.column('Status', width=100)
view_complaints_tree.column('Severity', width=100)

view_complaints_tree.pack(expand=True, fill='both')

# Populate View Complaints tab with existing complaints
complaints_data = api_call('complaint')

for complaint in complaints_data:
    view_complaints_tree.insert('', 'end', text=complaint['studentid'], values=(complaint['studentid'], complaint['complainttype'], complaint['date'], complaint['description'], complaint['status'], 'severity'))

# Logout Tab
logout_tab = ttk.Frame(tab_control)
tab_control.add(logout_tab, text='Logout')

# Logout Tab
logout_label = ttk.Label(logout_tab, text='Are you sure you want to logout?', font=('Arial', 14))
logout_label.pack(pady=20)

logout_button_frame = ttk.Frame(logout_tab)
logout_button_frame.pack(pady=20)

def logout():
    import main
    main.open_window()

yes_button = ttk.Button(logout_button_frame, text='Yes', command=logout)
yes_button.pack(side='left', padx=10)

no_button = ttk.Button(logout_button_frame, text='No', command=logout)
no_button.pack(side='left', padx=10)

# Populate View Complaints tab with existing complaints
complaints_data = api_call('complaint')

for complaint in complaints_data:
    view_complaints_tree.insert('', 'end', text=complaint['studentid'], values=(complaint['studentid'], complaint['complainttype'], complaint['date'], complaint['description'], complaint['status'], 'severity'))

# Pack Tab Control
tab_control.pack(expand=1, fill='both')

# Set Add Faculty Tab as default
tab_control.select(view_complaints_tab)

# Run GUI
root.mainloop()
