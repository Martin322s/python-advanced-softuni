from project.student import Student
import unittest

class StudentTests(unittest.TestCase):
    def setUp(self):
        self.student = Student("Martin")

    def test_constructor_sets_name(self):
        self.assertEqual("Martin", self.student.name)

    def test_constructor_sets_empty_courses_when_none(self):
        self.assertEqual({}, self.student.courses)

    def test_constructor_sets_given_courses(self):
        courses = {"Python": ["intro"]}
        student = Student("Ivan", courses)
        self.assertEqual(courses, student.courses)

    def test_enroll_existing_course_updates_notes(self):
        self.student.courses = {"Python": ["intro"]}
        result = self.student.enroll("Python", ["loops"])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["intro", "loops"], self.student.courses["Python"])

    def test_enroll_new_course_with_Y_adds_notes(self):
        result = self.student.enroll("Python", ["intro"], "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["intro"], self.student.courses["Python"])

    def test_enroll_new_course_with_empty_string_adds_notes(self):
        result = self.student.enroll("Python", ["intro"])

        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(["intro"], self.student.courses["Python"])

    def test_enroll_new_course_without_notes_flag_adds_empty_list(self):
        result = self.student.enroll("Python", ["intro"], "N")

        self.assertEqual("Course has been added.", result)
        self.assertEqual([], self.student.courses["Python"])

    def test_add_notes_existing_course(self):
        self.student.courses = {"Python": ["intro"]}
        result = self.student.add_notes("Python", "loops")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["intro", "loops"], self.student.courses["Python"])

    def test_add_notes_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.student.add_notes("Java", "OOP")
        self.assertEqual("Cannot add notes. Course not found.", str(ctx.exception))

    def test_leave_existing_course_removes_it(self):
        self.student.courses = {"Python": ["intro"]}
        result = self.student.leave_course("Python")

        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, self.student.courses)

    def test_leave_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ctx:
            self.student.leave_course("Java")
        self.assertEqual("Cannot remove course. Course not found.", str(ctx.exception))


if __name__ == "__main__":
    unittest.main(verbosity=2)