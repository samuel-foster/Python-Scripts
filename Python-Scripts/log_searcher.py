import os
import subprocess
import tkinter as tk
from tkinter import filedialog
from zipfile import ZipFile

# Define the command to search for a certain word in a file
def search_file(file_path, keyword):
    command = "grep " + keyword + " " + file_path
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# Define a function to handle the button click event
def handle_search():
    directory = directory_entry.get()
    keyword = keyword_entry.get()
    results = ""
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".log") or file.endswith(".log.zip") or file.endswith(".txt"):
                file_path = os.path.join(root, file)
                if file.endswith(".zip"):
                    try:
                        with ZipFile(file_path, 'r') as zip:
                            for logfile in zip.namelist():
                                if logfile.endswith(".log") or logfile.endswith(".txt"):
                                    file_data = zip.read(logfile).decode('utf-8')
                                    log_results = search_file(file_data, keyword)
                                    if log_results:
                                        results += f"\n\n{file}/{logfile}:\n{log_results}"
                    except Exception as e:
                        print(f"Error searching {file}: {e}")
                else:
                    try:
                        log_results = search_file(file_path, keyword)
                        if log_results:
                            results += f"\n\n{file_path}:\n{log_results}"
                    except Exception as e:
                        print(f"Error searching {file_path}: {e}")
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, results)

# Create the GUI
root = tk.Tk()
root.title("File Search")

# Create the input fields and search button
tk.Label(root, text="Directory:").grid(row=0, column=0)
directory_entry = tk.Entry(root)
directory_entry.grid(row=0, column=1)
directory_button = tk.Button(root, text="Choose", command=lambda: directory_entry.insert(tk.END, filedialog.askdirectory()))
directory_button.grid(row=0, column=2)
tk.Label(root, text="Keyword:").grid(row=1, column=0)
keyword_entry = tk.Entry(root)
keyword_entry.grid(row=1, column=1)
search_button = tk.Button(root, text="Search", command=handle_search)
search_button.grid(row=2, column=0, columnspan=3)

# Create the results field
tk.Label(root, text="Results:").grid(row=3, column=0)
result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=4, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()
