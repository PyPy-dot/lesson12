import logging
import rt_with_exceptions
import runnertest
import unittest


class RunnerTest(runnertest.RunnerTest):
    def test_walk(self):
        try:
            runner_ = rt_with_exceptions.Runner('Fill', -1)
            for i in range(10):
                runner_.walk()
            self.assertEqual(runner_.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner"', exc_info=False)

    def test_run(self):
        try:
            runner_ = rt_with_exceptions.Runner(10, 5)
            for i in range(10):
                runner_.run()
            self.assertEqual(runner_.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=False)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,
                        filemode='w',
                        filename='runner_tests.log',
                        encoding='utf-8',
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    unittest.main()
