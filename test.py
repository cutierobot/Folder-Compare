import FC
import unittest	
import filecmp
import sys
# from unittest.mock import patch
from unittest import mock
from io import StringIO

# import containers
# import builtins

class TestClass(unittest.TestCase):
	"""docstring for testClass"""
	# @mock.patch('sys.stdout', new_callable=StringIO)
	# sys.stdout = open('log.txt', 'w')

	def setUp(self):
		self.arg1 = "/test_folder/folder1"
		self.arg2 = "/test_folder/folder2"
		self.comp = FC.Compare(self.arg1, self.arg2)
		self.dc = filecmp.dircmp(self.arg1, self.arg2)

	@mock.patch('sys.stdout', new_callable=StringIO)
	def test_get_init_details(self, usrInput, mock_stdout):
		with mock.patch('builtins.input', side_effect=usrInput):
			# with mock.patch('sys.stdout', new_callable=StringIO) as mock_stdout:
			# greeting()
			self.comp.get_init_details(self.dc)
		return mock_stdout.getvalue()


	def test_exit(self):
		test = "Legends of colours:\nLeft Only Right Only Common Directories/files\n\n[0] Left Only\n[1] Right Only\n[2] Comparison Only\n[3] Table Comparison\n[4] Recursive Comparison\n[h] Reprint these help messages\n[exit] Exit this program\nType number from 0 - 4: exit\nAre you sure you want to exit [Y|N]: Y"
		user_input = ['exit', 'Y']

		with self.assertRaises(SystemExit) as cm:
		    # your_method()
			self.assertEqual(self.test_get_init_details(user_input), test)

		self.assertEqual(cm.exception.code, 0)
		


# tst2 = em2 + em1 + 'Jerry is NOT a palindrome\n'
# self.assertEqual(self.main_op(['to', 'a2a', 'Jerry']), tst2)


if __name__ == '__main__':
    unittest.main()