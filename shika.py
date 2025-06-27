from markov_chain import *

def rep(o, num):
    return [o for i in range(num)]


def shikanoko_init():
    shi = MarkovState("shi", [])
    ka = MarkovState("ka", [])
    no = MarkovState("no", [])
    ko = MarkovState("ko", [])
    ta = MarkovState("ta", [])
    n = MarkovState("n", [])
    blank = MarkovState(" ", [])

    shi.transitions = [ka, ta]
    ka.transitions = [no]
    no.transitions = [ko]
    ko.transitions = [ko, shi, no, no]
    ta.transitions = [n]
    n.transitions = [ta, blank]
    blank.transitions = [blank, shi]

    return [shi, ka, no, ko, ta, n, blank]


def main():
    states = shikanoko_init()
    chain = MarkovChain(states[0])
    chain.run(200)


if __name__ == "__main__":
    main()
