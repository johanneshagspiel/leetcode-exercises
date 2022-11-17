class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        a_area = (ax2 - ax1) * (ay2 - ay1)
        b_area = (bx2 - bx1) * (by2 - by1)

        max_x_1 = max(ax1, bx1)
        min_x_2 = min(ax2, bx2)
        x_overlap = min_x_2 - max_x_1

        max_y_1 = max(ay1, by1)
        min_y_2 = min(ay2, by2)
        y_overlap = min_y_2 - max_y_1

        c_area = 0
        if x_overlap > 0 and y_overlap > 0:
            c_area = x_overlap * y_overlap

        return a_area + b_area - c_area
