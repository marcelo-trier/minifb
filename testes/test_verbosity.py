
# from: https://gist.github.com/pitrk/11755d23fd6ca441b1ef6c09f644a103
import io
import unittest
import unittest.mock


# -- function --
def print_hello_world() -> None:
    print('Hello World!')


#  - test-- 
class TestFunction(unittest.TestCase):
    def test_print_hello_world_prints_correctly_with(self):
        with unittest.mock.patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            print_hello_world()
            mystr = mock_stdout.getvalue()
            self.assertEqual(
                mystr,
                'Hello World!\n'  # It's important to remember about '\n'
            )
        print(mystr)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hello_world_prints_correctly_decorator(self, mock_stdout):
        print_hello_world()
        self.assertEqual(
            mock_stdout.getvalue(),
            'Hello World!\n'  # It's important to remember about '\n'
        )