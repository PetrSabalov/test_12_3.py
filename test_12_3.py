import unittest
import test_12_1 as rn
import test_12_2 as trnt


class RunnerTest(unittest.TestCase):

    is_frozen = True

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_1 = rn.Runner('Олег')
        for walk in range(10):
            runner_1.walk()
        self.assertEqual(runner_1.distance, 50)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_2 = rn.Runner('Ольга')
        for run_ in range(10):
            runner_2.run()
        self.assertEqual(runner_2.distance, 100)

    @unittest.skipIf(is_frozen == False, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        runner_3 = test_12_1.Runner('Олеся')
        for walk in range(10):
            runner_3.walk()
        runner_4 = test_12_1.Runner('Олаф')
        for run in range(10):
            runner_4.run()
        self.assertNotEqual(runner_3.distance, runner_4.distance)


class TournamentTest(unittest.TestCase):

    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}


    def setUp(self):
        self.runner_1 = trnt.Runner('Усейн', 10)
        self.runner_2 = trnt.Runner('Андрей', 9)
        self.runner_3 = trnt.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):

        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            key_position = 1
            for key, value in test_value.items():
                print(f'\t{key_position}: {value.name}')
                key_position += 1

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn1(self):
        turn_1 = trnt.Tournament(90, self.runner_1, self.runner_3)
        result = turn_1.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results["Результат Усейна и Ника"] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn2(self):
        turn_2 = trnt.Tournament(90, self.runner_2, self.runner_3)
        result = turn_2.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results["Результат Андрея и Ника"] = result

    @unittest.skipIf(is_frozen == True, 'Тесты в этом кейсе заморожены')
    def test_turn3(self):
        turn_3 = trnt.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = turn_3.start()
        self.assertTrue(result[list(result.keys())[-1]] == 'Ник')
        self.all_results["Общий результат"] = result