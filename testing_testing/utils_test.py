import unittest
import utils


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("I run only once")

    @classmethod
    def tearDownClass(cls) -> None:
        print("I run after all")

    def setUp(self) -> None:
        print("I run before any test case")

    def tearDown(self) -> None:
        print("I run after every test case")

    # def test_for_error(self):
    #     # with self.assertRaises(TypeError) as e:
    #     #     utils.add("4", 2)
    #     #     or
    #     self.assertRaisesRegex(TypeError, "anything", utils.add, "4", 2)

    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_add(self):
        """
            GIVEN:

            WHEN:

            THEN:

        """
        self.assertEqual(5, utils.add(2, 3))

    def test_lis(self):
        self.assertEqual([1, 4, 9], utils.square_list([1, 2, 3]))


if __name__ == '__main__':
    unittest.main()
