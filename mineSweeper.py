import sys, pygame

import param_var
import lib

import debug

gameSpec = param_var.gameLevel[input("Please select game level: ")]

lib.mine_setup(gameSpec['size'], gameSpec['no_of_mines'])
lib.gameDataInit(gameSpec['size'], param_var.minePos)

print(param_var.minePos)

debug.printGameLayout(param_var.gameDataLayout)