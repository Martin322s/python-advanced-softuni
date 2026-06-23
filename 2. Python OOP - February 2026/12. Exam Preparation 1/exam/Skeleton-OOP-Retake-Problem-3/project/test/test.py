from project.gallery import Gallery
import unittest

class TestGallery(unittest.TestCase):
    def test_init_sets_attributes_and_empty_exhibitions(self):
        g = Gallery("Gallery1", "Sofia", 120.5)
        self.assertEqual("Gallery1", g.gallery_name)
        self.assertEqual("Sofia", g.city)
        self.assertEqual(120.5, g.area_sq_m)
        self.assertTrue(g.open_to_public)
        self.assertEqual({}, g.exhibitions)

    def test_init_open_to_public_false(self):
        g = Gallery("Gallery1", "Sofia", 10.0, open_to_public=False)
        self.assertFalse(g.open_to_public)

    def test_gallery_name_strips_spaces(self):
        g = Gallery("  Gallery1  ", "Sofia", 10.0)
        self.assertEqual("Gallery1", g.gallery_name)

    def test_gallery_name_raises_when_empty_or_spaces_only(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("   ", "Sofia", 10.0)
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

    def test_gallery_name_raises_when_contains_non_alnum(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("Gallery-1", "Sofia", 10.0)
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex.exception))

        with self.assertRaises(ValueError) as ex2:
            Gallery("G@llery1", "Sofia", 10.0)
        self.assertEqual("Gallery name can contain letters and digits only!", str(ex2.exception))

    def test_gallery_name_allows_letters_and_digits_only(self):
        g = Gallery("Abc123", "Sofia", 10.0)
        self.assertEqual("Abc123", g.gallery_name)

    def test_city_raises_when_empty(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("Gallery1", "", 10.0)
        self.assertEqual("City name must start with a letter!", str(ex.exception))

    def test_city_raises_when_does_not_start_with_letter(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("Gallery1", "1Sofia", 10.0)
        self.assertEqual("City name must start with a letter!", str(ex.exception))

        with self.assertRaises(ValueError) as ex2:
            Gallery("Gallery1", "-Sofia", 10.0)
        self.assertEqual("City name must start with a letter!", str(ex2.exception))

        with self.assertRaises(ValueError) as ex3:
            Gallery("Gallery1", " Sofia", 10.0)
        self.assertEqual("City name must start with a letter!", str(ex3.exception))

    def test_city_allows_starting_with_letter(self):
        g = Gallery("Gallery1", "Sofia", 10.0)
        self.assertEqual("Sofia", g.city)

    def test_area_sq_m_raises_when_zero(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("Gallery1", "Sofia", 0.0)
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_area_sq_m_raises_when_negative(self):
        with self.assertRaises(ValueError) as ex:
            Gallery("Gallery1", "Sofia", -1.0)
        self.assertEqual("Gallery area must be a positive number!", str(ex.exception))

    def test_area_sq_m_accepts_positive(self):
        g = Gallery("Gallery1", "Sofia", 1.0)
        self.assertEqual(1.0, g.area_sq_m)

    def test_add_exhibition_adds_when_missing(self):
        g = Gallery("Gallery1", "Sofia", 10.0)
        res = g.add_exhibition("Impressionism", 2024)
        self.assertEqual('Exhibition "Impressionism" added for the year 2024.', res)
        self.assertIn("Impressionism", g.exhibitions)
        self.assertEqual(2024, g.exhibitions["Impressionism"])

    def test_add_exhibition_returns_message_when_already_exists_and_does_not_override(self):
        g = Gallery("Gallery1", "Sofia", 10.0)
        g.add_exhibition("Impressionism", 2024)

        res = g.add_exhibition("Impressionism", 2025)
        self.assertEqual('Exhibition "Impressionism" already exists.', res)
        self.assertEqual(2024, g.exhibitions["Impressionism"])  # not overwritten

    def test_remove_exhibition_returns_not_found_when_missing(self):
        g = Gallery("Gallery1", "Sofia", 10.0)
        res = g.remove_exhibition("Missing")
        self.assertEqual('Exhibition "Missing" not found.', res)

    def test_remove_exhibition_removes_and_returns_message_when_exists(self):
        g = Gallery("Gallery1", "Sofia", 10.0)
        g.add_exhibition("Impressionism", 2024)

        res = g.remove_exhibition("Impressionism")
        self.assertEqual('Exhibition "Impressionism" removed.', res)
        self.assertNotIn("Impressionism", g.exhibitions)

    def test_list_exhibitions_returns_joined_lines_when_open_to_public_true(self):
        g = Gallery("Gallery1", "Sofia", 10.0, open_to_public=True)
        g.add_exhibition("A", 2020)
        g.add_exhibition("B", 2021)

        res = g.list_exhibitions()
        self.assertEqual("A: 2020\nB: 2021", res)

    def test_list_exhibitions_returns_closed_message_when_open_to_public_false(self):
        g = Gallery("Gallery1", "Sofia", 10.0, open_to_public=False)
        g.add_exhibition("A", 2020)

        res = g.list_exhibitions()
        self.assertEqual('Gallery Gallery1 is currently closed for public! Check for updates later on.', res)


if __name__ == "__main__":
    unittest.main()