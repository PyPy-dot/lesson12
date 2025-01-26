import unittest
import runnertest
import tournamenttest


TestST = unittest.TestSuite()

TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(runnertest.RunnerTest))
TestST.addTest(unittest.TestLoader().loadTestsFromTestCase(tournamenttest.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(TestST)