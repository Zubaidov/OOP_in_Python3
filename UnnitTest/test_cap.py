import unittest
import cap
class TestCap(unittest.TestCase):
    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        text = 'monty python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Monty Python')

    def test_add_form(self):
        mynum = 4
        result = cap.add_num(mynum)
        self.assertEquals(result, 5)



if __name__ == '__main__':
    unittest.main()