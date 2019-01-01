# \033[1;32;40m green
# \033[1;35;40m purple
# \033[1;34;40m Bright Blue
# \033[0;37;40m Normal text
# \033[2;37;40m Normal text underline
import filecmp
import sys

# folder1="/Volumes/Mikaela\'s Hardrive/TV SHOWS"
# folder2 = "/Volumes/Grayson/Tv shows/"
# dc = filecmp.dircmp(folder1, folder2)
# dc.report_full_closure()

class Compare(object):
	"""The compare class that is the brains behind this whole program"""
	def __init__(self, folder1, folder2):
		self.dc = ""
		self.folder1 = folder1
		self.folder2 = folder2
		
	"""
		Sets the class "dc" to the given dc value
		@param dc The value to become self.dc value
		"""	
	def set_dc(self, dc):
		self.dc = dc

	# TODO: [write] function definition (99)
	def get_init_details(self, dc):
		# folder1=sys.argv[1]
		# folder2 = sys.argv[2]
		if self.dc == "":
			Compare.set_dc(self,dc)

		# self.table_print(self.dc)

		# left = '\n'.join(dc.left_only)
		# right = '\n'.join(dc.right_only)
		# com = '\n'.join(dc.common_dirs)
		# sub = '\n'.join(dc.subdirs)

		# print statments
		print("Legends of colours:\n"+"\033[1;35;40m"+"Left Only"+
			"\033[1;34;40m"+" Right Only"+
			"\033[1;32;40m"+" Common Directories/files\033[0;37;40m\n")

		self.init_prompt()

		# self.recursive_dir(dc,self.folder1,self.folder2)

	"""
	Prints the left directory only. Where only file/folders that appear in the
	left compared directory appear.
	"""
	def left_directory_only(self):
		left = '\n'.join(self.dc.left_only)
		# Left Only
		print("\033[1;35;40m" +"left_only: \033[0;37;40m\n" + left + "\n")

	"""
	Prints the right directory only. where only file/folders that appear in the
	right compared directory appear.
	"""
	def right_directory_only(self):
		right = '\n'.join(self.dc.right_only)
		# right Only
		print("\033[1;34;40m"+"Right Only: \033[0;37;40m\n" + right + "\n")

	"""
	Prints the comparison between directory 1 and 2 together.
	"""
	def compared_only(self):
		com = '\n'.join(self.dc.common_dirs)
		# common directories print
		print("\033[1;32;40m"+"Common Directories/files\033[0;37;40m\n" + com + "\n")


	# //TODO: [write] function definition (99)
	# @staticmethod
	def recus_details(self,dc,folder1,folder2):
		# left = '\n'.join(dc.left_only)
		# right = '\n'.join(dc.right_only)
		# com = '\n'.join(dc.common)

		# leftOnly = "\033[1;35;40m" +format("left_only: ","^25s")+"\033[0;37;40m"
		# rightOnly = "\033[1;34;40m"+format("Right Only: ","^25s")+"\033[0;37;40m"
		# Common = "\033[1;32;40m"+format("Common Directories/files","^25s")+"\033[0;37;40m"
		# yellow_pole = "\033[1;33;40m"+"|"+"\033[0;37;40m"

		# # Left Only
		# print(yellow_pole+leftOnly+yellow_pole)
		# print(left)
		# # right Only
		# print(yellow_pole+rightOnly+yellow_pole)
		# print(right)
		# # common directories print
		# print(yellow_pole+Common+yellow_pole)
		# print(com)
		self.table_print(dc)


	"""
	Recursive of sorts, finds subfolders and go through them and 
	prints out subfolders info.
	@see recus_details
	"""
	# @staticmethod
	def recursive_dir(self,dc,folder1,folder2):
		if len(dc.common_dirs)>0:
			for folder in dc.common_dirs:
				
				# print folder name in yellow
				pole = "|"+ format(folder,"^25s")+"|"
				print("\033[1;33;40m"+"+"+format("--","-^25s")+"+"+"\033[0;37;40m")
				print("\033[1;33;40m"+pole+"\033[0;37;40m")
				print("\033[1;33;40m"+"+"+format("--","-^25s")+"+"+"\033[0;37;40m")
				
				left = folder1+"/"+folder
				right = folder2+"/"+folder 
				newdc = filecmp.dircmp(left, right)
				# Compare.recus_details(newdc,left,right)
				self.recus_details(newdc,left,right)
				
				# # deals with the subfolders in the current folder. i.e Season 1
				# if len(newdc.common_dirs)>0:
				# 	for subfolder in newdc.common_dirs:
				# 		# print("\nsubfolder: "+subfolder)
				# 		# print("======================\n")
				# 		print("\n\033[1;33;40m"+subfolder+"\033[0;37;40m")
				# 		subleft = left+"/"+subfolder
				# 		subright = right+"/"+subfolder 
				# 		subdc = filecmp.dircmp(subleft, subright)
				# 		# Compare.recus_details(subdc,subleft,subright)
				# 		self.recus_details(subdc,subleft,subright)
				# 	print("#######################\n")
				# # Compare.give_best_score(len(dc.common),newdc)
				# self.give_best_score(len(dc.common),newdc)
				# print("======================\n")

				# self.subfolder_rec(newdc, left, right, dc)

	"""
	Takes in the dc and newdc, which is for the subfolders of the dc, and 
	prints out the subfolder infomation for that dc folder.
	@param newdc The newdc for the subfolder
	@param dc teh dc for the parent directory
	@param left The left directory subfolder creation
	@param right The right directory subfolder creation
	"""
	def subfolder_rec(self, newdc, left, right, dc):
	# deals with the subfolders in the current folder. i.e Season 1
		if len(newdc.common_dirs)>0:
			for subfolder in newdc.common_dirs:
				# print("\nsubfolder: "+subfolder)
				# print("======================\n")
				print("\n\033[1;33;40m"+subfolder+"\033[0;37;40m")
				subleft = left+"/"+subfolder
				subright = right+"/"+subfolder 
				subdc = filecmp.dircmp(subleft, subright)
				# Compare.recus_details(subdc,subleft,subright)
				self.recus_details(subdc,subleft,subright)
			print("#######################\n")
		# Compare.give_best_score(len(dc.common),newdc)
		self.give_best_score(len(dc.common),newdc)
		print("======================\n")

	"""
	The initial prompt that appears after successful initialisation of program.
	It launches all the sub_programs of this program. If anything but 0-4, or h
	is entered then there is a reprompt.
	"""
	def init_prompt(self):
		# name of python program
		# options
		# - see only things on first directory(quick look)
		# - see only things on second directory(quick look)
		# - see things on both first and second directory(quick look)
		# - go into sub directories
		# input prompt
		print("[0] Left Only")
		print("[1] Right Only")
		print("[2] Comparison Only")
		print("[3] Table Comparison")
		print("[4] Recursive Comparison")
		print("[h] Reprint these help messages")
		print("[exit] Exit this program")
		
		usrInput = input("Type number from 0 - 3: ")
		if usrInput == "0":
			self.left_directory_only()
		elif usrInput == "1":
			self.right_directory_only()
		elif usrInput == "2":
			self.compared_only()
		elif usrInput == "3":
			self.table_print(self.dc)
		elif usrInput == "4":
			self.recursive_dir(self.dc,self.folder1,self.folder2)
		elif usrInput == "h":
			self.init_prompt()
		elif usrInput == "exit":
			exInput = input("Are you sure you want to exit [Y|N]: ")
			if exInput == "Y":
				sys.exit(2)
		else:
			self.print_red("error please input a number between 0 - 3")

		self.init_prompt()

	"""
	In a nice table format gives all comparason types (left_only, right_only, 
	and comparison)
	@param dc the self.dc value
	"""
	@staticmethod
	def table_print(dc):

		# left = '\n'.join(dc.left_only)
		# right = '\n'.join(dc.right_only)
		# com = '\n'.join(dc.common_dirs)

		# coloured words
		leftOnly = "\033[1;35;40m" +"left_only\033[0;37;40m"
		rightOnly = "\033[1;34;40m"+"Right Only\033[0;37;40m"
		commonDirs = "\033[1;32;40m"+"Common Directories/files\033[0;37;40m"
		# leftTitle = format(leftOnly,":^10")
		# ------ borders
		leftPole = "-"*23
		middlePole = "-"*24
		rightPole = "-"*28
		
		print("+"+"-"*23+"+"+"-"*24+"+"+"-"*28+"+")
		print("|       "+leftOnly+"       |       "+rightOnly+"       |  "+commonDirs+"  |")
		print("+"+"-"*23+"+"+"-"*24+"+"+"-"*28+"+")

		# get heights of the three coloums and get the largest number and use for
		# for loop
		sizes = []
		sizes.append(len(dc.left_only))
		sizes.append(len(dc.right_only))
		sizes.append(len(dc.common))

		for x in range(0,max(sizes)):
			# 1st column
			temp = "|"
			if x < sizes[0]:
				dcl = str(dc.left_only[x])
				# lft = 23 - len(dc.left_only[x])
				temp += dcl[0:23].ljust(23, ' ')
				temp = temp.splitlines()
				temp = "?".join(temp)
				# print('{0:.23}'.format(dcl) + " "*lft, end="")
			else:
				temp += " "*23
			temp += "|"

			# 2nd column
			if x < sizes[1]:
				temp_right = dc.right_only[x]
				# rght = 24 - len(dc.right_only[x])
				# if temp.isprintable():
				# 	print("is printable")
				# else:
				# 	print("is not printable")
				temp += temp_right[0:24].ljust(24, ' ')
				temp = temp.splitlines()
				temp = "?".join(temp)
				# if temp.isprintable():
				# 	print("is printable")
				# else:
				# 	print("is not printable")
				# print('{0:.24}'.format(dc.right_only[x]) + " "*rght, end="")
			else:
				temp += " "*24
				# print(" "*24, end="")
			# print("[temp = ]"+temp)
			temp += "|"
			# print("|", end="",flush=True)

			# 3rd column
			if x < sizes[2]:
				temp_comm = dc.common[x]
				# comp = 28 - len(dc.common[x])
				temp += temp_comm[0:28].ljust(28, ' ')
				temp = temp.splitlines()
				temp = "?".join(temp)
				# print('{0:.28}'.format(dc.common[x]) + " "*comp, end="")
			else:
				temp += " "*28
				# print(" "*28, end="",flush=True)
			temp += "|"
			# print("|")
			print(temp)
			temp = ""
		print("+"+"-"*23+"+"+"-"*24+"+"+"-"*28+"+")
			
		Compare.print_red("left_only = "+str(len(dc.left_only)))
		Compare.print_red("right_only: "+str(len(dc.right_only)))
		Compare.print_red("common: "+str(len(dc.common)))
		# get size of all coloums and use the larget number for "for loop"
		# bigest = max(sizes)

	"""
	Give best average to help with calulating what version to delete
	of what location. takes both directories with same folder name and 
	determines which folder has more items and such to help establish what 
	folder version to keep and delete.
	@param commonNumber The number of files/folders that both directories have 
		in common.
	@param subdc The dc value from filecmp
	@see filecmp#dircmp
		{https://docs.python.org/3/library/filecmp.html#filecmp.dircmp}
	"""
	@staticmethod
	def give_best_score(commonNumber,subdc):
		# tv show folder common directs/folders number
		# sub
		leftScore = commonNumber
		rightScore = commonNumber
		# for subfolders in subdc.common_dirs:
		leftScore += len(subdc.left_only)
		rightScore += len(subdc.right_only)
		
		leftScore += len(subdc.common)
		rightScore += len(subdc.common)
		# rightScore = len(subdc.right_only)+len(subdc.common)
		# leftScore = len(subdc.left_only)+len(subdc.common)
		Compare.print_red("left:"+str(leftScore)+" right: "+str(rightScore))
		if leftScore > rightScore:
			print("keep left, delete right")
		elif rightScore > leftScore:
			print("keep right, delete left")
		else:
			print("both equal")

	# ============helper function======================

	"""
	Uses the inbuild "print" method but changes all the text to red
	@param string - The string to print out red
	@see print
	"""
	@staticmethod
	def print_red(string):
		print("\033[1;31;40m"+string+"\033[0;37;40m")

"""
Checks argv value. If when initialising progam there are not 2 directories 
given then print error message and exit program.
"""
def check_argv():
	if len(sys.argv) != 3:
		print("\033[1;31;40m"+"name folder1 folder2\033[0;37;40m")
		sys.exit(2)


# //TODO: create testing functions and stuff
"""
Main funtion
@param argv Arguments from commandline
"""
def main(argv):
	# print(sys.argv[1])
	# folder1="/Volumes/Mikaela\'s Hardrive/TV SHOWS"
	# folder2 = "/Volumes/Grayson/Tv shows/"
	check_argv()
	comp = Compare(sys.argv[1],sys.argv[2])
	folder1 = sys.argv[1]
	folder2 = sys.argv[2]
	dc = filecmp.dircmp(folder1, folder2)
	comp.get_init_details(dc)
  
if __name__== "__main__":
	main(sys.argv)

