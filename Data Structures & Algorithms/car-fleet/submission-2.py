class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        

        # how many hours will it take car to reach the end?
        # how do we know if we will join another car fleet?
        # start with n fleets.. go from the closest car? or from the furthest car?
        cars = list(zip(position, speed))
        # sort by destination
        cars.sort()
        for i in range(len(cars)):
            # will we catch up? on what hour will it reach target?
            cars[i] = (target - cars[i][0]) / cars[i][1]
        print(cars)
        
        fleet = 1
        prev = cars.pop()
        while cars:
            curr = cars.pop()
            if curr > prev:
                fleet += 1
            prev = max(curr, prev)
        return fleet
            


        # fleets = 1
        # curr = float('-inf')
        # for i in range(len(cars)):
        #     # count the number of increasing sequences?
        #     if curr >= cars[i]:
        #         fleets += 1
        #     curr = cars[i]
        # return fleets
            