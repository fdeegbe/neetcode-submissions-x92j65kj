class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        gass=0
        costs=0
        curr = 0
        idx = 0
        for i in range(len(gas)):
            gass += gas[i]
            costs += cost[i]
            # total += 
            if gas[i] + curr >= cost[i]:
                curr += (gas[i] - cost[i])
                print(curr)
            else:
                curr = 0
                idx = i+1
                print("hi",idx)
        print(gass,costs,idx)
        if gass >= costs:
            return idx
        return -1
        
        