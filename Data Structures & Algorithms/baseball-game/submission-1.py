class Solution:
    def calPoints(self, operations: List[str]) -> int:
      scores =[]
      for op in operations:
        if op =="D":
            scores.append(scores[-1]*2)
        elif op =="C":
            scores.pop() 
        elif op == "+":
            scores.append(scores[-1]+scores[-2])
        else :
            scores.append(int(op))
      return sum(scores)