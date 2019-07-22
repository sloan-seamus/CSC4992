from constant import POPULATION_SIZE

class Belief:
    situational_knowledge = None
    situational_x = None
    normative_knowledge_min = None
    normative_knowledge_max = None

    def update_situational(self, arr):
        total = 0
        for i in arr:
            total += i.fitness
        self.situational_knowledge = total / (int(POPULATION_SIZE / 5))

    def update_normative(self, min, max):
        self.normative_knowledge_min = min.fitness
        self.normative_knowledge_max = max.fitness

    def update(self, sit, norm_min, norm_max):
        self.situational_knowledge = sit
        self.normative_knowledge_min = norm_min
        self.normative_knowledge_max = norm_max

