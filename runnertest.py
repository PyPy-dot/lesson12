import unittest
import runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walker = runner.Runner('Fill')
        for i in range(10):
            walker.walk()
        self.assertEqual(walker.distance, 50)

    def test_run(self):
        runner_ = runner.Runner('Fill')
        for i in range(10):
            runner_.run()
        self.assertEqual(runner_.distance, 100)

    def test_challenge(self):
        run1 = runner.Runner('Fill')
        run2 = runner.Runner('Gabe')
        for i in range(10):
            run1.run()
            run2.walk()
        self.assertNotEqual(run1.distance, run2.distance)


if __name__ == '__main__':
    RunnerTest.test_challenge()
    RunnerTest.test_run()
    RunnerTest.test_walk()
