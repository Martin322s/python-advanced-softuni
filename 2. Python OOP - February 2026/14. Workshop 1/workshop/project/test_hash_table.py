import unittest

from custom_hash_table import HashTable

class TestHashTable(unittest.TestCase):
    def test_init_default_capacity_is_4(self):
        table = HashTable()
        self.assertEqual(4, len(table))
        self.assertIsInstance(table.array, list)
        self.assertEqual(4, len(table.array))

    def test_hash_returns_index_in_range(self):
        table = HashTable()
        idx = table.hash("name")
        self.assertTrue(0 <= idx < len(table))

    def test_hash_expected_value_with_capacity_4(self):
        table = HashTable()
        self.assertEqual(1, table.hash("a"))
        self.assertEqual(3, table.hash("ab"))

    def test_add_and_get_single_item(self):
        table = HashTable()
        table.add("name", "Peter")
        self.assertEqual("Peter", table.get("name"))

    def test_get_missing_key_raises_keyerror(self):
        table = HashTable()
        with self.assertRaises(KeyError) as ex:
            table.get("missing")
        self.assertEqual("Key not found", ex.exception.args[0])

    def test_add_updates_existing_key_without_duplicates(self):
        table = HashTable()
        table.add("age", 25)
        table.add("age", 26)

        self.assertEqual(26, table.get("age"))

        idx = table.hash("age")
        bucket = table.array[idx]
        occurrences = sum(1 for k, _ in bucket if k == "age")
        self.assertEqual(1, occurrences)

    def test_add_handles_collision_separate_chaining(self):
        table = HashTable()
        table.add("a", 1)
        table.add("e", 2)

        self.assertEqual(1, table.get("a"))
        self.assertEqual(2, table.get("e"))

        idx = table.hash("a")
        self.assertEqual(idx, table.hash("e"))
        self.assertEqual(2, len(table.array[idx]))

    def test_resize_doubles_capacity_when_load_factor_exceeded(self):
        table = HashTable()
        self.assertEqual(4, len(table))

        table.add("k1", "v1")
        table.add("k2", "v2")
        table.add("k3", "v3")

        self.assertEqual(8, len(table))

        self.assertEqual("v1", table.get("k1"))
        self.assertEqual("v2", table.get("k2"))
        self.assertEqual("v3", table.get("k3"))

    def test_resize_multiple_times(self):
        table = HashTable()

        for i in range(20):
            table.add(f"key{i}", i)

        self.assertTrue(len(table) >= 16)
        for i in range(20):
            self.assertEqual(i, table.get(f"key{i}"))

    def test_setitem_and_getitem_work(self):
        table = HashTable()
        table["name"] = "Peter"
        table["age"] = 25

        self.assertEqual("Peter", table["name"])
        self.assertEqual(25, table["age"])

    def test_getitem_missing_key_raises_keyerror(self):
        table = HashTable()
        with self.assertRaises(KeyError):
            _ = table["missing"]

    def test_len_returns_capacity_not_count(self):
        table = HashTable()
        self.assertEqual(4, len(table))
        table["a"] = 1
        table["b"] = 2
        self.assertEqual(4, len(table))

    def test_str_returns_string_representation_of_internal_array(self):
        table = HashTable()
        table["name"] = "Peter"
        self.assertEqual(str(table.array), str(table))


if __name__ == "__main__":
    unittest.main()