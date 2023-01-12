import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, *args, **kwargs):
        self.contents = []
        for color in kwargs:
            # append color multiple times according to no defined
            # color of ball        == color
            # no. of balls defined == kwargs[color]
            self.contents += int(kwargs[color]) * [color]

    def draw(self, num):
        if num > len(self.contents):
            self.hand = self.contents
            self.contents = []
        else:
            self.hand = random.sample(self.contents, k = num)
            # update self.content (remove self.hand from self.content)
            for color in self.hand:
                self.contents.remove(color)

        return self.hand

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # counter to check if drawn ball satisfy expected_balls
    satisfy = 0

    for exp in range(num_experiments):
        hat_cp = copy.deepcopy(hat)
        # print(f"\nfresh cp  : {hat_cp.contents}")
        hand = hat_cp.draw(num_balls_drawn)
        # print(f"expected  : {expected_balls}, (length: {len(expected_balls)})")

        i = 0
        # print(f"hand      : {hand}")
        for color in expected_balls:
            # print("\t" + color)
            if expected_balls[color] <= hand.count(color):
                i += 1
            # print(f"\ti: {i}")

        if i == len(expected_balls):
            satisfy += 1

        # print(f"\tsatisfy: {satisfy}")
    return satisfy/num_experiments