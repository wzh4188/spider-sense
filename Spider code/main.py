from leg import Leg
from spider import *

deg1, deg2, deg3 = 90, 70, 90

def main():
    leg_1 = leg.Leg(1, [0, 1, 2], np.array([deg1, deg2, deg3]))
    leg_2 = leg.Leg(1, [3, 4, 5], np.array([deg1, deg2, deg3]))
    leg_3 = leg.Leg(1, [6, 7, 8], np.array([deg1, deg2, deg3]))
    leg_4 = leg.Leg(2, [0, 1, 2], np.array([deg1, deg2, deg3]))
    leg_5 = leg.Leg(2, [3, 4, 5], np.array([deg1, deg2, deg3]))
    leg_6 = leg.Leg(2, [6, 7, 8], np.array([deg1, deg2, deg3]))
    # Create a list of leg objects
    legs = [leg_1, leg_2, leg_3, leg_4, leg_5, leg_6]

    # Create the spider object
    spider = Spider(legs)

    # Perform actions using the spider object
    spider.standup()
    spider.walk_forward(steps=5)
    spider.tripod_turn(steps=3, direction='left')

if __name__ == "__main__":
    main()