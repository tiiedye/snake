# Snake project
from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_score()

    # Detect collision with wall
    snake_x = snake.head.xcor()
    snake_y = snake.head.ycor()
    if snake_x > 280 or snake_x < -280 or snake_y > 280 or snake_y < -280:
        game_is_on = False
        score.game_over()

# All code before exit
screen.exitonclick()
