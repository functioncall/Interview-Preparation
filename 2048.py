"""
Clone of 2048 game.
"""

import poc_2048_gui
import numeric
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}



    

def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    #creat a list of all the values in line
    merge_list = [cell for cell in line if cell != 0]
    index = 0
    #if the 2 cell next to each other have the same value 
    #multipy the first by 2 and drop the 2nd.
    for index in range(len(merge_list)):
        if index < len (merge_list)-1 and merge_list[index] == merge_list[index+1]:
            merge_list[index] = merge_list.pop(index+1) * 2
            index +=index  
    #add the missing zeros        
    merge_list.extend((len (line) - len(merge_list))*[0])
    return merge_list


#############################################
# You don't need the following.
# It's a dictionary of {1:1, 2:2, 3:3, 4:4}
# Just use UP, DOWN, LEFT, RIGHT in your code.
#############################################
# Commented out the following:
# DIRECTION = {UP:1, DOWN:2, LEFT:3, RIGHT:4}
# print DIRECTION[1]
#############################################


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._grid_height = grid_height
        self._grid_width = grid_width
        self.reset()
        #####################
        # Is this just test code?
        # You probably shouldn't leave it lying about.
        # Commenting out.
        # self.move(DIRECTION[1])

        

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        #creat a wXh matrix of zeros
        self._board =[[0 for dummy_col in range(self._grid_width)]
                    for dummy_row in range(self._grid_height)]
        self.new_tile()
        ########################################################
        # Moved the following line to self.new_tile()
        # self.set_tile(self._grid_height, self._grid_width, self._new_tile)

        self.new_tile()
        ########################################################
        # Moved the following line to self.new_tile()
        # self.set_tile(self._grid_height, self._grid_width, self._new_tile)
        
        #####################################
        # There's no need to return anything here.
        # In fact, it causes an error in OwlTest.
        # Commenting out.
        # return self._board
        

    
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        ######################
        # The grader will accept this.
        # There's no need for the temp variable, though.
        temp = list(self._board)
        return str(temp)
        

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        #########################
        # Check out __init__.
        # We're already storing
        # the height in an instance variable.
        # There's no need to compute the
        # height here. Commenting out next line.
        # return len (self._board)
        return self._grid_height

    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        #########################
        # See get_grid_height() above.
        # return len (self._board[0])
        return self._grid_width

    
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        
        #new_board = TwentyFortyEight(self._grid_height,self._grid_width)
        #if direction 3,4 take each row, merge then drop all zeros
        #if 3 (left) fill missing zeros on the right
        #if 4 (right) fill missing zeros on the left
        if direction == 3 or direction == 4: 
            for dummy_row in range(len(self._board)-1):
                line=self._board[dummy_row][:]
                newline=merge(line)
                new_merge_list = [cell for cell in newline]
                index = 0
                for index in range(len(new_merge_list)):
                    if new_merge_list[index] == 0:
                        new_merge_list.pop(index)
                        index +=index  
                        if direction == 3:
                            new_merge_list.extend((len (newline) - len(new_merge_list))*[0])
                        elif direction == 4:
                            for dummy_i in range(len (newline) - len(new_merge_list)):
                                new_merge_list.insert(0,[0])
        #if direction 1,2 take each col, merge then drop all zeros
        #if 1 (up) fill missing zeros at the end of the line
        #if 2 (down) fill missing zeros at the beginning of the line                        
        elif direction == 1 or direction == 2: 
            for dummy_col in range(len(self._board[0])-1):
                line=self._board[:][dummy_col]
                newline=merge(line)
                new_merge_list = [cell for cell in newline]
                index = 0
                for index in range(len(new_merge_list)):
                    if new_merge_list[index] == 0:
                        new_merge_list.pop(index)
                        index +=index  
                        if direction == 1:
                            new_merge_list.extend((len (newline) - len(new_merge_list))*[0])
                        elif direction == 2:
                            for dummy_i in range(len (newline) - len(new_merge_list)):
                                new_merge_list.insert(0,[0])
        return self._board
                
               
    ###############################
    # I added this helper function.
    def get_empties(self):
        """
        Return a list of (row number,col number) tuples
        representing the empty tiles on the board.
        """
        # Sorry for the ugly list comprehension.
        # I'm in a bit of a hurry.
        return [(r, c) for r, row in enumerate(self._board) \
                for c, col in enumerate(row) if col == 0]
        
        
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        #use random.random() to generate 2s & 4s

        ####################
        # This variable is only used in the body of this function
        # so there's no need for an instance variable here.
        # self._random_num = random.randint(0, 9)
        random_num = random.randint(0,9)
        
        #####################
        # I put a call to set_tile in the body
        # of this function, so this variable
        # can be local now.
        # self._new_tile = 0 
        new_tile = 0
        
        if random_num != 9:
            new_tile = 2
        else:
            new_tile = 4
        
        #####################
        # I moved set_tile here.
        # We need to pick an empty tile to place the new tile in.
        # Get all the empty tiles as (row, col) indices and pick one.
        empties = self.get_empties()
        if empties:
            row,col = random.choice(empties)
            self.set_tile(row, col, new_tile)    

        
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        #############################
        # Hmmm....
        # I think you misunderstood what was supposed to happen
        # here. You're just supposed to set the tile at 
        # row, col to value.
        # 
        # dummy_val=0
        # while dummy_val!=1: 
        #    cell_x=random.randint(0, row-1)
        #    cell_y=random.randint(0, col-1)
        #    if self._board[cell_x][cell_y] == 0:
        #        self._board[cell_x][cell_y]=value
        #        dummy_val=1
        #    else:
        #        self._board[cell_x][cell_y] = self._board[cell_x][cell_y]
        self._board[row][col] = value
         

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._board[row][col]



    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))

# http://www.codeskulptor.org/#user40_vKzxmDoPJW_7.py