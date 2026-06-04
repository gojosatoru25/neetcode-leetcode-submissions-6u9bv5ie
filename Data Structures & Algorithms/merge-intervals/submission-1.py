class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda pair : pair[0])
        output = [intervals[0]]
        for start, end in intervals:
            #get the end of the interval which is already in the stack 
            last= output[-1][1]
            #check if the intervals overlap
            if start <= last :
                output[-1][1]= max(last,end)


            #if no overalpping then insert it as a seperate element
            else:
                output.append([start,end])
        return output




        