import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math
import warnings
warnings.filterwarnings("ignore")

def hasRequiredUtilities(inventory):
    count = 0
    # if inventory is not None:
    if inventory is not None:
        for entry in inventory:
            if entry is not None:
                weapon_class = entry['weapon_class']
                if weapon_class.lower() == 'smg' or weapon_class.lower() == 'rifle':
                    count += 1
    return count


class ProcessGameState:
    def __init__(self, file_path):
        pd.set_option('display.max_rows', None)
        pd.set_option('display.max_columns', None)
        self.df = pd.read_parquet(file_path)
       

    def hasRequiredUtilities(self, inventory, weaponClass):
        count = 0
        for entry in inventory:
            weapon_class = entry['weapon_class'].lower()
            if weapon_class == weaponClass.lower():
                count += 1
        return count

    def getTimer(self, timer):
        timerArr = timer.split(":")
        return int(timerArr[0]) * 60 + int(timerArr[1])

    
    def filter_within_boundary(self, x_min, x_max, y_min, y_max, z_min, z_max):
        return self.df[(self.df['x'] >= x_min) & (self.df['x'] <= x_max) &
                       (self.df['y'] >= y_min) & (self.df['y'] <= y_max) &
                       (self.df['z'] >= z_min) & (self.df['z'] <= z_max)]
    
    def extract_weapon_classes(self):
        temp = [None] * len(self.df)  # Create a list of None values with the same length as the DataFrame's index
        for i, item in enumerate(self.df['inventory']):
            arr=[]
            if item is not None:
                for weapon_class in item:
                    weapon = weapon_class['weapon_class']
                    arr.append(weapon)
            temp[i] = arr  # Assign the weapon class at the corresponding position in the list
        
        self.df['weapon_classes'] = temp
        return self.df['weapon_classes']
    

        
    def is_common_strategy_used(self,boundary_x_min, boundary_x_max, boundary_y_min, boundary_y_max):
        # Filter rows within the provided boundary
                
        filtered_rows = self.filter_within_boundary(boundary_x_min, boundary_x_max, boundary_y_min, boundary_y_max, 285, 421)
        
        # Count the occurrences of Team2 on T side
        team2_t_count = filtered_rows[(filtered_rows['team'] == 'Team2') & (filtered_rows['side'] == 'T')].shape[0]
        
        # Calculate the total count of rows within the boundary
        total_count = filtered_rows.shape[0]
        
        # Calculate the frequency
        frequency = team2_t_count / total_count
    
        if frequency > 0.5 :
            return "It is a common stratergy to enter via light blue boundary"
        else:
            return "It is not a common stratergy to enter via light blue boundary"
          # Return True if the frequency is greater than 0.5, indicating a common strategy

    def avg_enter_time_with_rifles_smgs(self) -> float:
        filtered_data = self.df[self.df["inventory"].notnull() 
                                & (self.df["team"]=="Team2")
                                & (self.df["side"]=="T") 
                                & (self.df["area_name"] == "BombsiteB")
                                & ~(self.df["bomb_planted"])
                                ]
        
        

        filtered_data.loc[:, "smgCnt"] = filtered_data["inventory"].apply(lambda x: self.hasRequiredUtilities(x, "smg"))
        filtered_data.loc[:, "rifleCnt"] = filtered_data["inventory"].apply(lambda x: self.hasRequiredUtilities(x, "rifle"))


        grouped_data = filtered_data.groupby(["tick", "clock_time"]).agg({"rifleCnt": "sum","smgCnt": "sum"}).reset_index()

        grouped_data = grouped_data.rename(columns={"rifleCnt": "tolRifleCnt", "smgCnt": "tolSmgCnt"})
        
        filtered_data = grouped_data[(grouped_data["tolRifleCnt"] >= 2) | (grouped_data["tolSmgCnt"] >= 2)]

        filtered_data.loc[:, "timer"] = filtered_data["clock_time"].apply(lambda x: self.getTimer(x))

        
        avg_timer = filtered_data["timer"].mean()
        avg_timer = math.floor(avg_timer)

        # print(avg_timer)
        # avg_timer /= 60
        avg_timer_str = f"{math.floor(avg_timer/60)}:{avg_timer%60}"
        # print(avg_timer_str)

        return avg_timer_str
    
    
    def heatmap_waiting_spots(self):
        heatmap = self.df[(self.df['team'].eq('Team2')) & (self.df['side'].eq('CT')) &
                          (self.df['area_name'].eq('BombsiteB'))].groupby(['x', 'y']).size().unstack(fill_value=0)
        return heatmap
    
    def plot_ct_positions(self):
        ct_positions = self.df[(self.df['team'] == 'Team2') & (self.df['side'] == 'CT')]

        # Extract X and Y coordinates
        x = ct_positions['x']
        y = ct_positions['y']

        # Calculate 2D histogram
        heatmap, xedges, yedges = np.histogram2d(x, y, bins=100)

        # Plot the heatmap with colorbar
        plt.figure(figsize=(10, 8))
        plt.imshow(heatmap.T, origin='lower', cmap='magma', extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]])
        plt.colorbar(label="Density")
        plt.title("CT Player Positions in BombsiteB")
        plt.xlabel("X-coordinate")
        plt.ylabel("Y-coordinate")
        plt.show()


