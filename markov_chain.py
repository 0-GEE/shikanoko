import random

class MarkovState:
    def __init__(self, value, transitions: "list[MarkovState]") -> None:
        self.value = value
        self.transitions = transitions

    def choose_next(self) -> "MarkovState":
        return random.choice(self.transitions)
            


class MarkovChain:
    def __init__(self, initial: "MarkovState") -> None:
        self.curr = initial
        self.sofar = ""

    def next(self):
        self.curr = self.curr.choose_next()

    def run(self, num_steps: int):
        self.sofar += self.curr.value
        print(self.curr.value)
        for i in range(num_steps):
            self.next()
            self.sofar += self.curr.value
            print(self.curr.value)
        print("\nFINAL RESULT:\n\n" + self.sofar)

