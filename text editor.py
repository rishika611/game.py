from tkinter import*
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title("text editor of CODINGAL!")
window.geometry('600x600')
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)
def open_file():
    filepath=askopenfilename(
        filetypes=[("Text Files","*.txt"),("All Files","*.*")]
    )
    if not filepath:
        return
    text=txt_edit.get(1.0,END)
    txt_edit.delete(1.0,END)
    with open(filepath,"r") as input_file:
        text=input_file.read()
        txt_edit.insert(END,text)
        input_file.close()
    window.title(f"codingals text editor-{filepath}")

window.mainloop()
