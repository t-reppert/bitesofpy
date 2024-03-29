from typing import List

import numpy as np
import pandas as pd
import re


class LightsGrid:

    def __init__(self, grid_size: int, instructions: List[str]):
        self.grid_size = grid_size
        self.grid = pd.DataFrame(np.zeros([grid_size, grid_size], dtype=int))
        self.instructions = instructions

    def process_grid_coordinates(self, s1: str, s2: str):
        """A helper function you might want to create to process
          the top left hand corner coordinates and the bottom
          right hand coordinates given in the instructions

        :param s1: The top left hand corner of the grid to operate on
        :param s2: The bottom right hand corner of the grid to operate on

        Suggested return are 4 integers representing x1, x2, y1, y2 [hint]"""
        x1 = int(s1.split(',')[0].strip())
        y1 = int(s1.split(',')[1].strip())
        x2 = int(s2.split(',')[0].strip())
        y2 = int(s2.split(',')[1].strip())
        return x1, y1, x2, y2

    def validate_grid(self):
        """A helper function you might want to write to verify that:
          - no lights are brighter than 5
          - no lights are less than 0"""
        temp_df = self.grid.copy()
        lights_above_5 = (temp_df > 5)
        lights_below_0 = (temp_df < 0)
        temp_df[lights_above_5] = 5
        temp_df[lights_below_0] = 0
        self.grid = temp_df

    def turn_on(self, s1: str, s2: str):
        """The turn_on function takes 2 parameters:

        :param s1: The top left hand corner of the grid to operate on
        :param s1: The bottom right hand corner of the grid to operate on

        For each light in the grid slice given:
          - If the light is already on, do nothing
          - If the light is off, turn it on at intensity 1
        """
        # Process grid coordinates
        x1, y1, x2, y2 = self.process_grid_coordinates(s1, s2)
        # First extract the slice of the grid into a new dataframe
        temp_df = self.grid.iloc[x1:x2+1,y1:y2+1]
        # Now create a mask of all lights == 0 in the slice
        lights_zero = (temp_df == 0)
        # # Now turn on all lights that are off
        temp_df[lights_zero] = 1
        # Finally overwrite the grid with the new values
        self.grid.iloc[x1:x2+1,y1:y2+1] = temp_df

    def turn_off(self, s1: str, s2: str):
        """The turn_off function takes 2 parameters:

        :param s1: The top left hand corner of the grid to operate on
        :param s1: The bottom right hand corner of the grid to operate on

        Turn off all lights in the grid slice given."""
        x1, y1, x2, y2 = self.process_grid_coordinates(s1, s2)
        self.grid.iloc[x1:x2+1,y1:y2+1] = 0

    def turn_up(self, amount: int, s1: str, s2: str):
        """The turn_up function takes 3 parameters:

        :param amount: The intensity to turn the lights up by
        :param s1: The top left hand corner of the grid to operate on
        :param s1: The bottom right hand corner of the grid to operate on

        For each light in the grid slice given turn the light up
          by the given amount. Don't turn a light up past 5"""
        x1, y1, x2, y2 = self.process_grid_coordinates(s1, s2)
        self.grid.iloc[x1:x2+1,y1:y2+1] += amount
        self.validate_grid()

    def turn_down(self, amount: int, s1: str, s2: str):
        """The turn down function takes 3 parameters:

        :param amount: The intensity to turn the lights down by
        :param s1: The top left hand corner of the grid to operate on
        :param s1: The bottom right hand corner of the grid to operate on

        For each light in the grid slice given turn the light down
          by the given amount. Don't turn a light down past 0"""
        x1, y1, x2, y2 = self.process_grid_coordinates(s1, s2)
        self.grid.iloc[x1:x2+1,y1:y2+1] -= amount
        self.validate_grid()

    def toggle(self, s1: str, s2: str):
        """The toggle function takes 2 parameters:

        :param s1: The top left hand corner of the grid to operate on
        :param s1: The bottom right hand corner of the grid to operate on

        For each light in the grid slice given:
          - If the light is on, turn it off
          - If the light is off, turn it on at intensity 3
        """
        # Process grid coordinates
        x1, y1, x2, y2 = self.process_grid_coordinates(s1, s2)
        # First extract the slice of the grid into a new dataframe
        temp_df = self.grid.iloc[x1:x2+1,y1:y2+1]
        # Now create a mask of all lights > 0 in the slice
        lights_on = (temp_df > 0)
        lights_off = (temp_df == 0)
        # Now turn off all lights that are on in the slice
        temp_df[lights_on] = 0
        # Set all lights that are off to 3 in the slice
        temp_df[lights_off] = 3
        # Finally overwrite the grid with the new values
        self.grid.iloc[x1:x2+1,y1:y2+1] = temp_df

    def follow_instructions(self):
        """Function to process all instructions.

        Each instruction should be processed in sequence,
          excluding the first instruction of course.
        """
        inst_regex = re.compile(r"^(turn (?:on|off|up ([0-9]+)|down ([0-9]+))|toggle) ([0-9,]+) through ([0-9,]+)")
        for instruction in self.instructions:
            matched = inst_regex.search(instruction)
            if matched:
                command = matched.group(1).strip()
                s1 = matched.group(4)
                s2 = matched.group(5)
                if "turn off" in command:
                    self.turn_off(s1, s2)
                elif "turn on" in command:
                    self.turn_on(s1, s2)
                elif "turn down" in command:
                    amount = int(matched.group(3))
                    self.turn_down(amount, s1, s2)
                elif "turn up" in command:
                    amount = int(matched.group(2))
                    self.turn_up(amount, s1, s2)
                elif command == "toggle":
                    self.toggle(s1, s2)
                
            

    @property
    def lights_intensity(self):
        """(given) get the total intensity of all lights"""
        return self.grid.to_numpy().sum()


# Main function that can be used to test the Class methods
if __name__ == "__main__":
    instructions = """create grid of length 100
    turn on 46,55 through 56,90
    turn off 37,3 through 42,83
    turn up 2 46,85 through 83,91
    turn off 81,38 through 86,87
    turn on 59,98 through 80,99
    turn down 1 37,41 through 76,54
    turn on 60,36 through 89,60
    turn off 44,20 through 64,68
    toggle 5,47 through 45,78
    toggle 20,41 through 70,82
    turn up 4 53,33 through 90,87
    toggle 85,49 through 98,97
    turn off 63,95 through 89,97
    turn off 38,1 through 72,70
    turn down 3 51,84 through 58,94
    toggle 51,55 through 66,88
    turn off 26,80 through 87,84
    turn up 3 14,51 through 71,77
    turn off 99,93 through 99,98
    toggle 46,66 through 55,95
    turn on 95,41 through 95,84
    turn up 2 56,22 through 94,88
    turn on 21,31 through 80,72
    toggle 53,27 through 63,84
    toggle 61,8 through 68,50
    turn on 39,70 through 88,72
    toggle 1,63 through 53,76
    toggle 70,44 through 834,44
    turn up 5 31,20 through 49,53
    toggle 69,18 through 83,34
    turn down 4 56,67 through 74,71
    toggle 34,48 through 95,48
    toggle 3,79 through 98,87
    turn on 58,54 through 84,71
    turn off 36,66 through 59,87
    turn on 80,43 through 96,99
    turn up 2 20,58 through 51,80
    turn off 10,49 through 26,77
    turn on 97,2 through 98,62
    turn off 31,68 through 36,87
    turn off 3,30 through 25,55
    turn off 39,68 through 86,94
    toggle 22,74 through 85,82
    turn down 4 38,60 through 55,87
    turn off 70,79 through 79,96
    turn off 57,80 through 99,87
    turn up 3 99,93 through 99,95
    turn on 80,22 through 86,72
    turn off 3,72 through 68,75"""

    # Create a list of all the instructions
    instructions = [line.strip() for line in instructions.splitlines()]

    # The grid size instruction is first
    # Extract it and convert to int
    grid_size = int(instructions[0].split(" ")[4])

    # Create a LightsGrid Class instance
    lights = LightsGrid(grid_size, instructions[1:])

    # Follow the instructions
    lights.follow_instructions()

    # Print the total intensity of the lights
    # The correct answer is 12317
    print(f"Total intensity of Lights on: {lights.lights_intensity}\n")