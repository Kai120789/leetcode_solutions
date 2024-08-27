class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        count = 0
        while count < len(intervals)-1:
            if intervals[count+1][0] <= intervals[count][1]:
                intervals[count] = [intervals[count][0], max(intervals[count][1], intervals[count+1][1])]
                intervals.pop(count+1)
            else:

                count += 1
        print(intervals)
        return intervals