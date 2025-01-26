import unittest
import runner_and_tournament
import pprint


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []
        cls.results = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        pprint.pprint(cls.all_results)

    def tearDown(self):
        print(self.results)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament1(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.results = tournament.start()
        self.all_results.append(self.results)
        self.assertTrue(self.results[2].name, 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament2(self):
        tournament = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.results = tournament.start()
        self.all_results.append(self.results)
        self.assertTrue(self.results[2].name, 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_tournament3(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.results = tournament.start()
        self.all_results.append(self.results)
        self.assertTrue(self.results[3].name, 'Ник')


if __name__ == '__main__':
    unittest.main()
