import unittest
from files_to_dict import get_items, make_dict
import tempfile

class TestGetItems(unittest.TestCase):
    file_descriptor, file_path = tempfile.mkstemp(suffix='.tmp')

    def test_empty_file_parsing(self):
        with open(self.file_path, 'r') as open_file:
            self.assertEqual(get_items(open_file, str), [])
            self.assertEqual(get_items(open_file, int), [])

    def test_string_parsing(self):
        with open(self.file_path, 'w') as open_file:
            open_file.write('a ab abc')
        with open(self.file_path, 'r') as open_file:
            self.assertEqual(get_items(open_file, str), ['a', 'ab', 'abc'])

    def test_int_parsing(self):
        with open(self.file_path, 'w') as open_file:
            open_file.write('1 12 123')
        with open(self.file_path, 'r') as open_file:
            self.assertEqual(get_items(open_file, int),
                            [1, 12, 123])

    def test_multiline_parsing(self):
        with open(self.file_path, 'w') as open_file:
            open_file.write('1 12 123\n2 23\n3 345 3456\n4')
        with open(self.file_path, 'r') as open_file:
            self.assertEqual(get_items(open_file, int),
                            [1, 12, 123, 2, 23, 3, 345, 3456, 4])

    def test_multiline_parsing_with_empty_string(self):
        with open(self.file_path, 'w') as open_file:
            open_file.write('1 12 123\n \n\n2 23\n3 345 3456\n4')
        with open(self.file_path, 'r') as open_file:
            self.assertEqual(get_items(open_file, int),
                            [1, 12, 123, 2, 23, 3, 345, 3456, 4])

class TestMakeDict(unittest.TestCase):
    empty_list = []
    keys = ['a', 'ab', 'abc']
    values_lt = [1]
    values = [1, 2, 3]
    values_gt = [1, 2, 3, 4]


    def test_empty_key_list(self):
        self.assertEqual(make_dict(self.empty_list, self.empty_list), {})
        self.assertEqual(make_dict(self.empty_list, self.values), {})

    def test_dict(self):
        self.assertEqual(make_dict(self.keys, self.values), {'a': 1, 'ab': 2, 'abc': 3})

    def test_dict_len(self):
        self.assertEqual(len(make_dict(self.keys, self.values_lt)), 3)
        self.assertEqual(len(make_dict(self.keys, self.values)), 3)
        self.assertEqual(len(make_dict(self.keys, self.values_gt)), 3)

    def test_None_values(self):
        d = make_dict(self.keys, self.values_lt)
        self.assertEqual(d['a'], 1)
        self.assertEqual(d['ab'], None)
        self.assertEqual(d['abc'], None)


if __name__ == '__main__':
    unittest.main()
