from tkinter import*
import tkinter.messagebox
import student_markDB

class markSheet:

	def __init__(self, master):

		root.title("Student Marksheet")

		#variables
		stdclass = StringVar()
		fname = StringVar()
		lname = StringVar()
		eng = StringVar()
		nep = StringVar()
		maths = StringVar()
		social = StringVar()
		hp = StringVar()
		sci = StringVar()
		comp = StringVar()
		optm = StringVar()


		#Functons
		def iExit():
			iExit = tkinter.messagebox.askyesno("Student Marksheet Generator", "Confirm if you want to exit")
			if(iExit > 0):
				root.destroy()
				return 

		def clearData():
			self.classtext.delete(0,END)
			self.fnametext.delete(0,END)
			self.lnametext.delete(0,END)
			self.engtext.delete(0,END)
			self.neptext.delete(0,END)
			self.mathtext.delete(0,END)
			self.socialtext.delete(0,END)
			self.hptext.delete(0,END)
			self.scitext.delete(0,END)
			self.comptext.delete(0,END)
			self.optmtext.delete(0,END)

		def addData():
			if(len(stdclass.get())!=0):
				student_markDB.addDataRec(stdclass.get(), fname.get(), lname.get(), eng.get(), nep.get(), maths.get(),
					social.get(), hp.get(), sci.get(), comp.get(), optm.get())

				studentlist.delete(0,END)
				studentlist.insert(END, (stdclass.get(), fname.get(), lname.get(), eng.get(), nep.get(), maths.get(),
				social.get(), hp.get(), sci.get(), comp.get(), optm.get()))


		def displayData():
			studentlist.delete(0,END)
			for row in student_markDB.viewData():
				total = int(row[4])+int(row[5])+int(row[6])+int(row[7])+int(row[8])+int(row[9])+int(row[10])+int(row[11])
				percentage = float((total/800)*100)
				if(int(row[4])>=32 and int(row[5])>=32 and int(row[6])>=32 and int(row[7])>=32 and 
				int(row[8])>=32 and int(row[9])>=32 and int(row[10])>= 32 and int(row[11])>=32):
					result = "Pass"
				else:
					result = "Fail"

				studentlist.insert(END, row,total,percentage,result)


		def selectedStudent(event):
			global ss
			searchstd = studentlist.curselection()[0]

			ss = studentlist.get(searchstd)

			self.classtext.delete(0,END)
			self.classtext.insert(END,ss[1])
			self.fnametext.delete(0,END)
			self.fnametext.insert(END,ss[2])
			self.lnametext.delete(0,END)
			self.lnametext.insert(END,ss[3])
			self.engtext.delete(0,END)
			self.engtext.insert(END,ss[4])
			self.neptext.delete(0,END)
			self.neptext.insert(END,ss[5])
			self.mathtext.delete(0,END)
			self.mathtext.insert(END,ss[6])
			self.socialtext.delete(0,END)
			self.socialtext.insert(END,ss[7])
			self.hptext.delete(0,END)
			self.hptext.insert(END,ss[8])
			self.scitext.delete(0,END)
			self.scitext.insert(END,ss[9])
			self.comptext.delete(0,END)
			self.comptext.insert(END,ss[10])
			self.optmtext.delete(0,END)
			self.optmtext.insert(END,ss[11])


		def deleteData():
			if(len(stdclass.get())!=0):
				student_markDB.deleteRec(ss[0])
				clearData()
				displayData()

		def updateDatabase():
			if(len(stdclass.get())!=0):
				student_markDB.updateData(ss[0],stdclass.get(), fname.get(), lname.get(), eng.get(), nep.get(), maths.get(),
					social.get(), hp.get(), sci.get(), comp.get(), optm.get())

		def serarchDatabase():
			studentlist.delete(0,END)
			for row in student_markDB.searchData(stdclass.get(), fname.get(), lname.get(), eng.get(), nep.get(), maths.get(),
					social.get(), hp.get(), sci.get(), comp.get(), optm.get()):
				studentlist.insert(END,row)

		def export_window():
			export_win = Toplevel()


		#Frame Design

		self.titleFrame  = Frame(root, bd = 2, padx = 40, pady = 8, bg = 'maroon', relief = RAISED)
		self.titleFrame.pack(side = TOP, fill = X)
		self.titleLabel = Label(self.titleFrame, font = ('arial', 46, 'bold'), text = "Student Marksheet Generator")
		#self.titleLabel.place(x = 100)
		#self.titleLabel.grid(row = 0, column = 0)
		self.titleLabel.pack()

		self.bottomFrame = Frame(root, bd = 2, width = 1350, height = 100, padx = 20, pady = 20, bg = 'maroon', relief = RAISED)
		self.bottomFrame.pack(side = BOTTOM)

		self.dataFrame = Frame(root, bd = 0, width  = 1350, height = 1000, relief = RIDGE)
		self.dataFrame.pack(side = BOTTOM)

		self.dataFrameLeft = LabelFrame(self.dataFrame, bd = 2, width = 700, height = 1000, padx = 20, relief = RIDGE, font = ('arial', 26, 'bold'),
			text = "Student Marks Inforamtion", bg = 'gray')
		self.dataFrameLeft.pack(side = LEFT)

		self.dataFrameLeftTop = LabelFrame(self.dataFrameLeft, bd = 2, width = 700, height = 200, padx = 20, relief  = RIDGE, font = ('arial', 26, 'bold'),
			text = "Student", bg = 'maroon')
		self.dataFrameLeftTop.pack()

		self.dataFrameLeftBottom = LabelFrame(self.dataFrameLeft, bd = 2, width = 700, height = 500, padx = 20, relief  = RIDGE, font = ('arial', 26, 'bold'),
			text = "Subjects & Marks", bg = 'maroon')
		self.dataFrameLeftBottom.pack()

		self.dataFrameRight = LabelFrame(self.dataFrame, bd = 2, width = 600, height = 1000, padx = 20, relief = RIDGE, font = ('arial', 26, 'bold'),
			text = "Marksheet")
		self.dataFrameRight.pack(side = RIGHT)

		#Labels and Data Entry 

		self.classlabel = Label(self.dataFrameLeftTop, font = ('arial', 16, 'bold'), text = "Class", width = 45, pady = 2)
		self.classlabel.grid(row = 0, column = 0, sticky = W)
		self.classtext = Entry(self.dataFrameLeftTop, font = ('arial', 16, 'bold'), textvariable = stdclass, width = 20)
		self.classtext.grid(row = 0, column = 1) 

		self.fnamelabel = Label(self.dataFrameLeftTop, font = ('arial', 16, 'bold'), text = "First Name", width = 45, pady = 2)
		self.fnamelabel.grid(row = 1, column = 0, sticky = W)
		self.fnametext = Entry(self.dataFrameLeftTop, font = ('arial', 16, 'bold'), textvariable = fname, width = 20)
		self.fnametext.grid(row = 1, column = 1)

		self.lnamelabel = Label(self.dataFrameLeftTop, font = ('arial', 16, 'bold'), text = "Last Name", width = 45, pady = 2)
		self.lnamelabel.grid(row = 2, column = 0, sticky = W)
		self.lnametext = Entry(self.dataFrameLeftTop, font = ('arial', 16, 'bold'), textvariable = lname, width = 20)
		self.lnametext.grid(row = 2, column = 1)

		self.englabel = Label(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), text = "English", width = 45, pady = 2)
		self.englabel.grid(row = 0, column = 0, sticky = W)
		self.engtext = Entry(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), textvariable = eng, width = 20)
		self.engtext.grid(row = 0, column = 1)

		self.neplabel = Label(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), text = "Nepali", width = 45, pady = 2)
		self.neplabel.grid(row = 1, column = 0, sticky = W)
		self.neptext = Entry(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), textvariable = nep, width = 20)
		self.neptext.grid(row = 1, column = 1)

		self.mathlabel = Label(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), text = "Mathematics", width = 45, pady = 2)
		self.mathlabel.grid(row = 2, column = 0, sticky = W)
		self.mathtext = Entry(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), textvariable = maths, width = 20)
		self.mathtext.grid(row = 2, column = 1)

		self.sociallabel = Label(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), text = "Social", width = 45, pady = 2)
		self.sociallabel.grid(row = 3, column = 0, sticky = W)
		self.socialtext = Entry(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), textvariable = social, width = 20)
		self.socialtext.grid(row = 3, column = 1)

		self.hplabel = Label(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), text = "Health and Population", width = 45, pady = 2)
		self.hplabel.grid(row = 4, column = 0, sticky = W)
		self.hptext = Entry(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), textvariable = hp, width = 20)
		self.hptext.grid(row = 4, column = 1)

		self.scilabel = Label(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), text = "Science", width = 45, pady = 2)
		self.scilabel.grid(row = 5, column = 0, sticky = W)
		self.scitext = Entry(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), textvariable = sci, width = 20)
		self.scitext.grid(row = 5, column = 1)

		self.complabel = Label(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), text = "Computer", width = 45, pady = 2)
		self.complabel.grid(row = 6, column = 0, sticky = W)
		self.comptext = Entry(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), textvariable = comp, width = 20)
		self.comptext.grid(row = 6, column = 1)

		self.optmlabel = Label(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), text = "Optional Mathematics", width = 45, pady = 2)
		self.optmlabel.grid(row = 7, column = 0, sticky = W)
		self.optmtext = Entry(self.dataFrameLeftBottom, font = ('arial', 16, 'bold'), textvariable = optm, width = 20)
		self.optmtext.grid(row = 7, column = 1)


		#----------------------------------------------------LISTBOX & SCROLLBAR------------------------------------------------

		scrollbar = Scrollbar(self.dataFrameRight)
		scrollbar.grid(row = 0, column = 1, sticky = 'ns')

		studentlist = Listbox(self.dataFrameRight, width = 45, height = 12, font = ('arial', 12, 'bold'), yscrollcommand = scrollbar.set)
		studentlist.bind('<<ListboxSelect>>',selectedStudent)
		studentlist.grid(row = 0, column = 0, padx = 15)
		scrollbar.config(command = studentlist.yview)


		#Buttons


		self.addnewBtn = Button(self.bottomFrame, text = "Add New", font = ('arial', 14, 'bold'), height = 2, width = 18, bd = 4, command = addData)
		self.addnewBtn.grid(row = 0, column = 0)

		self.displaydataBtn = Button(self.bottomFrame, text = "Display Marks", font = ('arial', 14, 'bold'), height = 2, width = 18, bd = 4, command  = displayData)
		self.displaydataBtn.grid(row = 0, column = 1)

		self.btnClearData = Button(self.bottomFrame, text = 'Clear Data', font = ('arial', 14, 'bold'), height = 2, width = 18, bd = 4, command = clearData)
		self.btnClearData.grid(row = 0, column = 2)

		self.btnDeleteData = Button(self.bottomFrame, text = 'Delete Data', font = ('arial', 14, 'bold'), height = 2, width = 18, bd = 4, command = deleteData)
		self.btnDeleteData.grid(row = 0, column = 3)

		self.btnUpdateData = Button(self.bottomFrame, text = 'Update Data', font = ('arial', 14, 'bold'), height = 2, width = 18, bd = 4, command = updateDatabase)
		self.btnUpdateData.grid(row = 0, column = 4)

		self.btnSearchData = Button(self.bottomFrame, text = 'Search Data', font = ('arial', 14, 'bold'), height = 2, width = 18, bd = 4, command = serarchDatabase)
		self.btnSearchData.grid(row = 0, column = 5)

		self.exportBtn = Button(self.bottomFrame, text = 'Export', font = ('arial', 14, 'bold'), height = 2, width = 18, bd = 4, command = export_window)
		self.exportBtn.grid(row = 0, column = 6)

		self.btnExit = Button(self.bottomFrame, text = 'Exit', font = ('arial', 14, 'bold'), height = 2, width = 18, bd = 4, command = iExit)
		self.btnExit.grid(row = 0, column = 7)


root = Tk()

b = markSheet(root)
root.mainloop()  