class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:

        def calculate_area(x1, y1, x2, y2):
            x_len = x2-x1
            y_len = y2-y1
            return x_len * y_len

        def find_closes_point(a1, a2, b1):
            if a1 <= b1 and b1 <= a2:
                c1 = b1
            else:
                dist1 = abs(b1-a1)
                dist2 = abs(b1-a2)

                if dist1 <= dist2:
                    c1 = a1
                else:
                    c1 = a2

            return c1


        cx1 = find_closes_point(ax1, ax2, bx1)
        cx2 = find_closes_point(ax1, ax2, bx2)
        cy1 = find_closes_point(ay1, ay2, by1)
        cy2 = find_closes_point(ay1, ay2, by2)

        area1 = calculate_area(ax1, ay1, ax2, ay2)
        area2 = calculate_area(bx1, by1, bx2, by2)
        area3 = calculate_area(cx1, cy1, cx2, cy2)

        result = area1 + area2 - area3

        return result
