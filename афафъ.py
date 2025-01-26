import runner_and_tournament
import pprint


class TournamentTest():
    def __init__(self):
        self.runner1 = runner_and_tournament.Runner('Усэйн', 10)
        self.runner2 = runner_and_tournament.Runner('Андрей', 9)
        self.runner3 = runner_and_tournament.Runner('Ник', 3)
        self.all_results = []

    def test_tournament1(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner3)
        self.results = tournament.start()
        self.all_results.append(self.results)

    def test_tournament2(self):
        tournament = runner_and_tournament.Tournament(90, self.runner2, self.runner3)
        self.results = tournament.start()
        self.all_results.append(self.results)

    def test_tournament3(self):
        tournament = runner_and_tournament.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.results = tournament.start()
        self.all_results.append(self.results)

    def start(self):
        TournamentTest.test_tournament1()
        TournamentTest.test_tournament2()
        TournamentTest.test_tournament3()


if __name__ == '__main__':
    TournamentTest().start()

