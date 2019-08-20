import unittest
def pipe_fix(pipe):
    print("<< Inside the method >> ".format(pipe))
    if not pipe: return None
    else:
        pipe_fixed = [i for i in range(pipe[0], pipe[-1] + 1)]
        print("Inside the else >> ".format(pipe))
        return pipe_fixed

class TestPipeFixer(unittest.TestCase):
    def test_fixer_1(self):
        pipe_fixed = pipe_fix([1, 5, 8, 10])
        self.assertEqual(pipe_fixed, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_fixer_2(self):
        pipe_fixed = pipe_fix([])
        self.assertIsNone(pipe_fixed)

    def test_fixer_3(self):
        pipe_fixed = pipe_fix([3])
        self.assertEqual(pipe_fixed, [3])

    def test_fixer_4(self):
        pipe_fixed = pipe_fix([8, 8, 8])
        self.assertEqual(pipe_fixed, [8])

    def test_fixer_5(self):
        pipe_fixed = pipe_fix([-3, 2, 3])
        self.assertEqual(pipe_fixed, [-3, -2, -1, 0, 1, 2, 3])

    def test_fix_simple_pipe(self):
        pipe_fixed = pipe_fix([1, 2, 3, 5, 6, 8, 9])
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9], pipe_fixed, )

    def test_fix_complex_pipe(self):
        pipe_fixed = pipe_fix([1, 2, 3, 12])
        self.assertEqual([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], pipe_fixed, )

    def test_fix_short_from_6_pipe(self):
        pipe_fixed = pipe_fix([6, 9])
        self.assertEqual([6, 7, 8, 9], pipe_fixed, )

    def test_fix_simple_and_negative_pipe(self):
        pipe_fixed = pipe_fix([-1, 4])
        self.assertEqual([-1, 0, 1, 2, 3, 4], pipe_fixed, )

    def test_fix_already_fixed_pipe(self):
        pipe_fixed = pipe_fix([1, 2, 3])
        self.assertEqual([1, 2, 3], pipe_fixed, )

if __name__ == '__main__':
    unittest.main()