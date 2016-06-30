import common.constant as c
from common.data_utilities import DataUtils
from django.test import TestCase

TESTING_FILE = c.TEST_ORIGIN_DATA_PATH
class DataUtilitiesTests(TestCase):

	def setUp(self):
		self.selected_attrs = dict({
			'A':'C', 
			'B':'D',
			'C':'C',
			'D':'D',
			'E':'C',
			'F':'D',
			'G':'D',
			'I':'D',
			'J':'D',
			'K':'D',
			'O':'D'
		})		
		self.data = DataUtils(file_path = TESTING_FILE, selected_attrs = self.selected_attrs)
		self.data.data_coarsilize()

	def test_data_preview(self):
		data = DataUtils(file_path = TESTING_FILE)
		preview = data.data_preview()
		self.assertEqual(len(preview.values[0]) > 0, True)

	def test_read_data_by_three_selected_column(self):
		"""
		Test the read data by user specified columns
		"""
		self.assertEqual(len(self.data.get_nodes_name()) == len(self.selected_attrs), True)

	def test_data_domain_keep_original_order(self):
		"""
		Test the order in domain object is in same order with 
		original raw data.
		"""
		df = self.data.get_pandas_df()
		domain = self.data.get_domain()
		cols = domain.keys()
		self.assertEqual(cols == list(df.columns.values), True)

	def test_data_coarsilization(self):
		print self.data.get_pandas_df()[:5]

	def test_data_generalization(self):
		self.data.data_generalize()
		print self.data.get_pandas_df()[:5]