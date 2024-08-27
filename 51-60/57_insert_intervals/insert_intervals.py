class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals = sorted(intervals)
        count = 0
        while count < len(intervals) -1:
            if intervals[count+1][0] <= intervals[count][1]:
                intervals[count] = [intervals[count][0], max(intervals[count+1][1], intervals[count][1])]
                intervals.pop(count+1)
            else:
                count += 1
        print(intervals)
        return intervals