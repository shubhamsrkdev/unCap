import tkinter as tk
from tkinter import filedialog, messagebox
import os
from openpyxl import load_workbook

def main():
    creds={}
    root=tk.Tk()
    root.iconify()
    print("Pick the excel file from which you want to import credentials\n")
    input("press enter to start\n")
    root.deiconify()
    excel=filedialog.askopenfilename(title="open uncap.exe",filetypes=[("excel","*.xl*")])
    root.iconify()
    if(excel==''):
        print("file does not exist")
        messagebox.showerror("No file selected","No File Selected. Program Terminated.")
        return
    print("point to the location of uncap.exe\n")
    input("press enter to start\n")
    root.deiconify()
    uncap=filedialog.askopenfilename(title="open uncap.exe",filetypes=[("uncap","uncap.exe")])
    if uncap=='':
        print("select a file")
        messagebox.showerror("No file selected","No File Selected. Program Terminated.")
        return
    root.iconify()
    [uncap_dir,uncap_exe]=os.path.split(uncap)
    if os.path.exists(os.path.join(uncap_dir,"main.py")):
        wb=load_workbook(excel)
        sheets=wb.get_sheet_names()
        #print(sheets)
        ws=wb[sheets[0]]
        i=0
        for row in ws.rows:
            creds[row[0].value]=row[1].value
            i=i+1
    #print(creds)
    else:
        messagebox.showerror("Dependencies not found","cannot find other files related to uncap. Program Terminated.")
    with open(os.path.join(uncap_dir,"cred.bin"),"wb") as f:
        from pickle import dump
        dump(creds,f)
    messagebox.showinfo("import success", "successfully imported "+str(i)+" credentials")
    root.destroy()
if __name__=="__main__":
    main()
