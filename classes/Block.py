import pygame

class Block:
    def __init__(self, position:List[int], width:int, height:int):
        self.position = position
        self.width = width
        self.height = height
        self.status = "intact"

    def check_collision(self, ball):
        if self.status == "intact":
            if self.position[0] <= ball.position[0] <= self.position[0] + self.width:
                if self.position[1] <= ball.position[1] <= self.position[1] + self.height:
                    return True
        return False

    def destroy(self):
        self.status = "destroyed"