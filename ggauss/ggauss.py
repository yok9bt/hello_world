import random
import matplotlib.pyplot as plt
import collections

class GaussGame():
    def __init__(self, draw_range = {min: 0, max: 100}, number_of_draws = 5, number_of_games = 100000) -> None:
        self.draw_range = draw_range
        self.number_of_draws = number_of_draws
        self.number_of_games = number_of_games

    def start(self):
        #Create win dictionary which contains amounts of possible wins as a key and, number of wins for each possible amounts as a value.
        win_dict = collections.OrderedDict()
        for x in range(self.draw_range[min]*self.number_of_draws, self.draw_range[max]*self.number_of_draws+1):
            win_dict[x]=0

        #Loop for all games
        for x in range(self.number_of_games):
            #Loop for one game
            d_sum = 0 #Sum of the drawn values
            d_sum
            for x in range(self.number_of_draws):
                d_sum += random.randrange(self.draw_range[min], self.draw_range[max]+1)
            win_dict[d_sum] += 1
        return win_dict

def main():
    #When I run game several times, with different number_of_draws parameter and draw it on one graph, then I can get interesting picture :-D
    g1 = GaussGame({min: 0, max: 100},1,10000000)
    g2 = GaussGame({min: 0, max: 100},2,10000000)
    g3 = GaussGame({min: 0, max: 100},3,10000000)
    g4 = GaussGame({min: 0, max: 100},4,10000000)
    g5 = GaussGame({min: 0, max: 100},5,10000000)

    d1 = g1.start()
    d2 = g2.start()
    d3 = g3.start()
    d4 = g4.start()
    d5 = g5.start()

    plt.plot(d1.keys(), d1.values(), 'r.')
    plt.plot(d2.keys(), d2.values(), 'g.')
    plt.plot(d3.keys(), d3.values(), 'b.')
    plt.plot(d4.keys(), d4.values(), 'b.')
    plt.plot(d5.keys(), d5.values(), 'b.')
    plt.show()

if __name__ == "__main__":
    main()