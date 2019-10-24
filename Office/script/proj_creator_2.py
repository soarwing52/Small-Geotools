import os
import shutil
from PIL import Image, ImageTk

try:
	import Tkinter as tk
	import tkFileDialog as filedialog
	import tkMessageBox as messagebox

except ImportError:
	import tkinter as tk
	from tkinter import filedialog
	from tkinter import messagebox


class creator():
	def __init__(self,root):
		
		self.image = Image.open(r"./Logo2.png")
		self.img_copy = self.image.copy()

		self.background_image = ImageTk.PhotoImage(self.image)

		self.background = tk.Label(root, image=self.background_image)
		self.background.pack(fill='x', expand='yes')
		self.background.bind('<Configure>', self._resize_image)

		frame = tk.Frame(root, bg='#80c1ff', bd=5)
		frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.2, anchor='n')

		Input_Label = tk.Label(frame, text='Neue Kommun Name \n ex.BIL_Billerbeck', bd=5, bg='#80c1ff', width=40, font=40).place(relx=0.05,relwidth=0.45,relheight=1)
		self.entry = tk.Entry(frame, font=40)
		self.entry.place(relx=0.55, relwidth=0.4, relheight=1)

		lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
		lower_frame.place(relx=0.5, rely=0.75, relwidth=0.75, relheight=0.2, anchor='n')

		create_button = tk.Button(lower_frame, text='Projekt offnen \n Waehlen Z:\Projekte\BIL_Billerbeck\BIL_001', font=40, command=self.create_file)
		create_button.place(relx=0.5, relheight=1, relwidth=0.8, anchor='n')
	def _resize_image(self, event):
		new_width = event.width
		new_height = int(new_width * 161/ 1000)

		self.image = self.img_copy.resize((new_width, new_height))

		self.background_image = ImageTk.PhotoImage(self.image)
		self.background.configure(image=self.background_image)

	def create_file(self):
		name = self.entry.get()
		path = str(filedialog.askdirectory())
		if path:
			print(name, path)
			try:
				source = r'Z:\Vorlagen\Pr_Nr_Ordner_Struktur'
				for data_stucture in os.listdir(source):
					shutil.copytree(os.path.join(source, data_stucture), os.path.join(path, data_stucture))

				bearbeitung = path + r'\5_Bearbeitung'
				GIS = bearbeitung + r'\GIS'
				WWK = 'Z:\Vorlagen\WWK'
				shutil.copytree(WWK, GIS)
				# list files in the folder
				WWK_list = os.listdir(GIS)

				for file in WWK_list:
					print(file)
					full = os.path.join(GIS, file)
					new_full = full.replace('Kommune', name)
					os.rename(full, new_full)

				messagebox.showinfo('Info', 'Done!')
			except WindowsError:
				messagebox.showerror('Error', "can't create" )
		else:
			print('nothing happened')


def main():
	root = tk.Tk()
	root.geometry('1000x500+0+0')
	#root.iconbitmap('car.ico')
	creator(root)
	root.mainloop()

if __name__ == '__main__':
	main()
