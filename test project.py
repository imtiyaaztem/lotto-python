from unittest import TestCase
from lottery import mytext  # You first import your function.
class TestProject(TestCase):
    def test_mytext(self):
        self.assertEqual(mytext(18), True, "Should be True")  # Then you call your function here and do the test. That is why your function cannot be doing many things.
        self.assertEqual(mytext(14), False, "Should be False")