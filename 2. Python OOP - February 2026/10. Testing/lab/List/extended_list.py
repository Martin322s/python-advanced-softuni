class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)
 
    def get_data(self):
        return self.__data
 
    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()
 
    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a
 
    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]
 
    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")
 
        self.get_data().insert(index, el)
 
    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]
 
    def get_index(self, el):
        return self.get_data().index(el)
    
import unittest


class IntegerListTests(unittest.TestCase):

    def setUp(self):
        self.integer_list = IntegerList(1, 2, 3, "test", 4.5)

    def test_constructor_stores_only_integers(self):
        self.assertEqual([1, 2, 3], self.integer_list.get_data())

    def test_add_valid_integer(self):
        result = self.integer_list.add(5)
        self.assertEqual([1, 2, 3, 5], result)

    def test_add_non_integer_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.integer_list.add("string")
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_remove_index_returns_removed_element(self):
        removed = self.integer_list.remove_index(1)
        self.assertEqual(2, removed)

    def test_remove_index_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.remove_index(10)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_get_returns_correct_element(self):
        element = self.integer_list.get(0)
        self.assertEqual(1, element)

    def test_get_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.get(10)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert_valid_data(self):
        self.integer_list.insert(1, 10)
        self.assertEqual([1, 10, 2, 3], self.integer_list.get_data())

    def test_insert_out_of_range_raises_index_error(self):
        with self.assertRaises(IndexError) as context:
            self.integer_list.insert(10, 5)
        self.assertEqual("Index is out of range", str(context.exception))

    def test_insert_non_integer_raises_value_error(self):
        with self.assertRaises(ValueError) as context:
            self.integer_list.insert(1, "string")
        self.assertEqual("Element is not Integer", str(context.exception))

    def test_get_biggest_returns_largest_element(self):
        biggest = self.integer_list.get_biggest()
        self.assertEqual(3, biggest)

    def test_get_index_returns_correct_index(self):
        index = self.integer_list.get_index(2)
        self.assertEqual(1, index)


if __name__ == "__main__":
    unittest.main()