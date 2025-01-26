import unittest
import runner_and_tournament
import pprint


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        pprint.pprint(cls.all_results)

    def tournament_test1(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[2], 'Ник')

    def tournament_test2(self):
        tournament = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[2], 'Ник')

    def tournament_test3(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.all_results = tournament.start()
        self.assertTrue(self.all_results[3], 'Ник')


if __name__ == '__main__':
    unittest.main()
