# Group A - Game Engine

## Setup

### Install dependencies
$ make install

### Run game
$ make



## Move functionality
Moving is done by selecting the type of move in the options menu to the right, and then clicking squares in the game board on the left of the view. A move alters the 2d-array of Square objects that represents the game board. This is done by collecting the x-y coordinates of the clicked square and then addressing the corrseponding square. All of the high-level input processing is done in the function move_handler which is a member of the Board class. The moves that are currently supported are described in more detail below.

### Place lying or standing piece
When the option for placing a lying or standing piece is selected, a click on the game board will collect the coordinates of the selected square and call a member function of the corresponding Square object which adds a piece to it. The coordinates are fetched in the move_handler function of the Board class.

### Move a piece
When the option for moving a piece is selected, two clicks on the game board are required to make a move. First, the player clicks on the square from which a piece shall be moved. After this, the player clicks the square to which the piece shall be moved. The coordinates of both these squares are collected and processed in the move_handler function of the Board class.

### Move a stack
When the option for moving a stack is selected, the first click on the game board will result in the player picking up the stack. The following clicks on the game board will place pieces at the selected locations until the stack on hand is empty. The coordinates from which the player picks up a stack and places pieces are processed and accessible in the move_handler function of the Board class.
