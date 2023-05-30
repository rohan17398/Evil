import os
from utilities import ProcessGameState

# Create an instance of the ProcessGameState class

boundary_x_min = -2806
boundary_x_max = -1565
boundary_y_min = 250
boundary_y_max = 1233

current_directory = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(current_directory, "game_state.parquet")


game_state = ProcessGameState(dataset_path)

# Question 1: Check if entering via the light blue boundary is a common strategy used by Team2 on T side
is_common_strategy_used = game_state.is_common_strategy_used(boundary_x_min, boundary_x_max, boundary_y_min, boundary_y_max)
print("Is entering via the light blue boundary a common strategy used by Team2 on T side?  ---> ", is_common_strategy_used)
print("\n")
# Question 2: Calculate the average timer that Team2 on T side enters "BombsiteB" with at least 2 rifles or SMGs
avg_timer = game_state.avg_enter_time_with_rifles_smgs()
print("Average timer that Team2 on T side enters 'BombsiteB' with at least 2 rifles or SMGs --->  ", avg_timer)

# Question 3: Plot the heatmap of CT player positions inside "BombsiteB"
game_state.plot_ct_positions()