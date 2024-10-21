import logging
import gymnasium as gym
from gymsnake.envs.controller import Action  # performs the registration of snake-v1 with gymnasium
from gymsnake.envs.controller import ObsType
from gymsnake.envs import snake_env

log = logging.getLogger("snake_challenge")
log.setLevel(logging.INFO)
if not log.hasHandlers(): log.addHandler(logging.StreamHandler())

env = gym.make('snake-v1', disable_env_checker=True, grid_size=(7, 7), obs_type = ObsType.COORDS)
obs, info = env.reset()
env.unwrapped.render(frame_speed=0.1)


def move(action):
    global env
    global total_reward
    global done
    if not done:
        obs_, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated
        total_reward += reward
        env.unwrapped.render(frame_speed=0.1)
    return done

def getStepCloserToFood() :
    (snake_x, snake_y) = snake.head
    print(snake_x)
    print(snake_y)
    (food_x, food_y) = env.controller.foods[0]
    print("SNAKE X: " + str(snake_x) + " SNAKE Y: " + str(snake_y))
    print("FOOD X: " + str(food_x) + " FOOD Y: " + str(food_y))
    if(food_y > snake_y): 
        return Action.UP
    elif(food_y < snake_y) : 
        return Action.DOWN
    elif(food_x > snake_x) : 
        return Action.RIGHT
    elif(food_x < snake_x) :  
        return Action.LEFT




done = False
total_reward = 0
snake = env.controller.snakes[0]
def move_to_start_position():
    global env
    snake = env.controller.snakes[0]
    while snake.head[1] > 0:
        move(Action.DOWN)
    while snake.head[0] > 0:
        move(Action.LEFT)

# move_to_start_position()
obs_, reward, terminated, truncated, info = env.step(Action.DOWN)
print(reward)
# for i in range(10) :
move_to_start_position()
while not done:
    # getStepCloserToFood()
    move(getStepCloserToFood())






