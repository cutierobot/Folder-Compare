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
	"""docstring for Compare"""
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
	@param parameter description
	@return [retType]	description
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
	@param parameter description
	@return [retType]	description
	"""
	def compared_only(self):
		com = '\n'.join(self.dc.common_dirs)
		# common directories print
		print("\033[1;32;40m"+"Common Directories/files\033[0;37;40m\n" + com + "\n")


	# //TODO: [write] function definition (99)
	@staticmethod
	def recus_details(dc,folder1,folder2):
		left = '\n'.join(dc.left_only)
		right = '\n'.join(dc.right_only)
		com = '\n'.join(dc.common)

		leftOnly = "\033[1;35;40m" +format("left_only: ","^25s")+"\033[0;37;40m"
		rightOnly = "\033[1;34;40m"+format("Right Only: ","^25s")+"\033[0;37;40m"
		Common = "\033[1;32;40m"+format("Common Directories/files","^25s")+"\033[0;37;40m"
		yellow_pole = "\033[1;33;40m"+"|"+"\033[0;37;40m"

		# Left Only
		print(yellow_pole+leftOnly+yellow_pole)
		print(left)
		# right Only
		print(yellow_pole+rightOnly+yellow_pole)
		print(right)
		# common directories print
		print(yellow_pole+Common+yellow_pole)
		print(com)

	"""
	Recursive of sorts, finds subfolders and go through them and 
	prints out subfolders info.
	@see recus_details
	"""
	@staticmethod
	def recursive_dir(dc,folder1,folder2):
		if len(dc.common_dirs)>0:
			for folder in dc.common_dirs:
				# print folder name in yellow
				# print("\033[1;33;40m"+folder+"\033[0;37;40m")
				# pole = "|"+ format(folder,"^25s")+"|"
				pole = "|"+ format(folder,"^25s")+"|"
				# print("\033[1;33;40m"+folder+"\033[0;37;40m")
				print("\033[1;33;40m"+"+"+format("--","-^25s")+"+"+"\033[0;37;40m")
				print("\033[1;33;40m"+pole+"\033[0;37;40m")
				print("\033[1;33;40m"+"+"+format("--","-^25s")+"+"+"\033[0;37;40m")
				
				left = folder1+"/"+folder
				right = folder2+"/"+folder 
				newdc = filecmp.dircmp(left, right)
				Compare.recus_details(newdc,left,right)
				
				if len(newdc.common_dirs)>0:
					for subfolder in newdc.common_dirs:
						# print("\nsubfolder: "+subfolder)
						# print("======================\n")
						print("\n\033[1;33;40m"+subfolder+"\033[0;37;40m")
						subleft = left+"/"+subfolder
						subright = right+"/"+subfolder 
						subdc = filecmp.dircmp(subleft, subright)
						Compare.recus_details(subdc,subleft,subright)
					print("#######################\n")
				Compare.give_best_score(len(dc.common),newdc)
				print("======================\n")

	# //TODO: [write] function definition (99)
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

		leftOnly = "\033[1;35;40m" +"left_only\033[0;37;40m"
		rightOnly = "\033[1;34;40m"+"Right Only\033[0;37;40m"
		commonDirs = "\033[1;32;40m"+"Common Directories/files\033[0;37;40m"
		# leftTitle = format(leftOnly,":^10")
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

		# print("one", end='')
		# print("two", end='')
		# print("three", end='')
		for x in range(0,max(sizes)):
			# print("|"+" "*23 + "|"+" "*24 + "|"+" "*28+"|")
			# print(str(len(dc.left_only[0])) + " - 23 = " + str(lft))
			
			# 1st column
			print("|", end="")
			if x < sizes[0]:
				lft = 23 - len(dc.left_only[x])
				# print('{:.23}'.format() dc.left_only[x] + " "*lft, end='')
				print('{:.23}'.format(dc.left_only[x]) + " "*lft, end='')
			else:
				print(" "*23, end="")
			print("|", end="")

			# 2nd column
			if x < sizes[1]:
				rght = 24 - len(dc.right_only[x])
				# print(dc.right_only[x] + " "*rght, end="")
				print('{:.24}'.format(dc.right_only[x]) + " "*rght, end="")
			else:
				print(" "*24, end="")
			print("|", end="")

			# 3rd column
			if x < sizes[2]:
				comp = 28 - len(dc.common[x])
				# print(dc.common[x] + " "*comp+"|")
				print('{:.28}'.format(dc.common[x]) + " "*comp, end="")
			else:
				print(" "*28, end="")
			print("|")
		print("+"+"-"*23+"+"+"-"*24+"+"+"-"*28+"+")
			
		# get size of all coloums and use the larget number for "for loop"
		# bigest = max(sizes)
		# print_red(str(sizes))


	"""
	Give best average to help with calulating what version to delete
	of what location
	"""
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


	# //TODO: [write] function definition (99)
	# //TODO: [immediet] commenting thing on Harvey
	@staticmethod
	def check_argv():
		if len(sys.argv) != 3:
			print("\033[1;31;40m"+"name folder1 folder2\033[0;37;40m")
			sys.exit(2)

	# ============helper function======================

	"""
	Uses the inbuild "print" method but changes all the text to red
	@param string - The string to print out red
	@see print
	"""
	@staticmethod
	def print_red(string):
		print("\033[1;31;40m"+string+"\033[0;37;40m")

def main(argv):
	# print(sys.argv[1])
	# folder1="/Volumes/Mikaela\'s Hardrive/TV SHOWS"
	# folder2 = "/Volumes/Grayson/Tv shows/"
	comp = Compare(sys.argv[1],sys.argv[2])
	comp.check_argv()
	folder1 = sys.argv[1]
	folder2 = sys.argv[2]
	dc = filecmp.dircmp(folder1, folder2)
	comp.get_init_details(dc)
  
if __name__== "__main__":
	main(sys.argv)

