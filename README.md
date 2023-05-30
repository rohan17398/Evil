# Evil Geniuses

This repository contains the code and documentation for the EvilGenius project.

## Project Documentation
 The Project report (Evil Genius Project Documentation.pdf)  is present in the Output folder in the repo along with the screenshots of the ouput

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)


## Introduction

The Evil Genius project is a data analysis and visualization tool designed to analyze gameplay data from a first-person shooter (FPS) game (CS-Go). The project aims to provide insights into player strategies and behaviors, specifically focusing on Team2's tactics on the Terrorist (T) side. By processing and analyzing the game state data, the project offers valuable information to understand common strategies, average entry times, and player positions within specific areas of interest.

The main features of the project include:

Common Strategy Analysis: The project allows users to determine if entering via a specific boundary, represented by a light blue area, is a common strategy used by Team2 on the T side. By calculating the frequency of Team2's entry via the boundary, users can assess its significance in their gameplay strategy.

Average Entry Timer Calculation: The project provides the average timer for Team2's entry into "BombsiteB" with at least 2 rifles or SMGs. This metric helps identify the typical timing of Team2's approach and their weapon choices during specific game scenarios.

Heatmap Visualization: The project offers a heatmap visualization of Counter-Terrorist (CT) player positions inside "BombsiteB." This heatmap provides a visual representation of CT player density and distribution, enabling users to analyze positioning patterns and potential strategies employed by the defending team.

## Installation

1. Clone the repository to your local machine:
2. Navigate to the project directory
3. Install the required dependencies by running the following command:
   
   pip install -r requirements.txt

## Usage

1.Run the orchestrator.py file using the following command:
  
  python3 orchestrator.py
  
The program will execute and provide the following outputs:

1. The result of the common strategy check for entering via the light blue boundary.
2. The average timer for entering "BombsiteB" with at least 2 rifles or SMGs.
3. A heatmap of CT player positions inside "BombsiteB".



   



