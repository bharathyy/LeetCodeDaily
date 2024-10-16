import heapq
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        lst = [(-a, "a"), (-b, "b"), (-c, "c")]
        lst = [(count, char) for count, char in lst if count != 0]
        heapq.heapify(lst)

        s=""
        last=""
        while lst:
            x,y=heapq.heappop(lst)
            if last == y and len(s) >= 2 and s[-2:] == y*2:
                if not lst:
                    break
                x2, y2 = heapq.heappop(lst)
                s += y2
                x2 += 1
                if x2 != 0:
                    heapq.heappush(lst, (x2, y2))
                heapq.heappush(lst, (x, y))
            else:
                repeat = min(2, -x)
                s += y * repeat
                x += repeat
                last = y
                if x != 0:
                    heapq.heappush(lst, (x, y))

        return s

                



            
        

               