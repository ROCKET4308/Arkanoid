import pytest
from classes.Score import Score
from classes.Ball import Ball
from classes.Block import Block
from classes.Game import Game
from classes.Paddle import Paddle
from components.BlocksArray import blocks

def test_ball_move():
    ball = Ball([100, 100], [2, 2])
    ball.move()
    assert ball.position == [102, 102]

def test_paddle_move():
    paddle = Paddle([500, 500], 80, 20)
    paddle.move(5)
    assert paddle.position == [505, 500]

def test_paddle_collision():
    ball = Ball([100, 100], [2, 2])
    paddle = Paddle([100, 80], 80, 20)
    assert paddle.check_collision(ball) == True

def test_block_collision():
    ball = Ball([100, 100], [2, 2])
    block = Block([100, 80], 50, 20)
    assert block.check_collision(ball) == True

def test_block_destroy():
    block = Block([100, 80], 50, 20)
    block.destroy()
    assert block.status == "destroyed"

def test_score_increase():
    score = Score(0)
    score.increase()
    assert score.score == 1

def test_game_over():
    game = Game([800, 600])
    game.ball.position = [100, 700]  # Set ball position below screen height
    assert game.check_game_over() == True


def test_game_over_blocks():
    game = Game([800, 600])
    for block in blocks:
        block.destroy()
    assert game.check_game_over() == True

if __name__ == "__main__":
    pytest.main()

