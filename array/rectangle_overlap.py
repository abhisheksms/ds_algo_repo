class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

def will_they_overlap(r1, r2):
    if r1.y1 > r2.y2 and r1.x2 > r2.x1:
        return True
    else:
        return False

print(will_they_overlap(Rectangle(2,6,5,2),
                        Rectangle(3,7,6,4)))

print(will_they_overlap(Rectangle(3,7,6,4),
                        Rectangle(2,6,5,2)))

print(will_they_overlap(Rectangle(2,6,5,2),
                        Rectangle(6,10,8,8)))