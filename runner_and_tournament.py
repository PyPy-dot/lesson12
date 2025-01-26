class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        for participant in self.participants:
            participant.distance = 0
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


if __name__ == '__main__':
    runner1 = Runner('Усэйн', 10)
    runner2 = Runner('Андрей', 9)
    runner3 = Runner('Ник', 3)
    tournaments = []
    tournaments.append(Tournament(90, runner1, runner3).start())
    print(runner1.distance, runner2.distance, runner3.distance)
    tournaments.append(Tournament(90, runner2, runner3).start())
    print(runner1.distance, runner2.distance, runner3.distance)
    tournaments.append(Tournament(90, runner1, runner2, runner3).start())
    print(runner1.distance, runner2.distance, runner3.distance)
    print(tournaments)

