# Sudoku Solver

This is a suite of scripts developed 100% on my iPhone using [Pythonista](http://omz-software.com/pythonista/). It was developed for use with the [Sudoku Extreme App](https://apps.apple.com/us/app/sudoku-extreme-classic-number/id1451683705).

The main program accepts a screenshot of the board, converts that input into a list-of-lists for processing, then solves the board using the [Dancing Links algorithm](https://en.wikipedia.org/wiki/Dancing_Links#:~:text=In%20computer%20science%2C%20dancing%20links,for%20the%20exact%20cover%20problem.).

## Contents
- `constants.py` - Defines size of Sudoku (9x9) and constants for cropping
- `utils.py` - Defines functions to crop the board to the proper size and extract numbers from the image
- `sudoku.py` - Defines a `Sudoku` class and methods to solve a sudoku puzzle via the Dancing Links algorithm using [`dlx`](https://pypi.org/project/dlx/) under the hood
- `main.py` - Simple wrapper to accept a screenshot, interpret it, and solve it
- `images/`
  - Contains directories holding each number (1-9 and empty) in each possible position in the board, as well as a combined average of the 81 images per number
  - `split_board.py` - A throwaway script used to split the board into 81 images and save them
  - `generate_baseline.py` - The script used to combine the 81 individual images into an average image

## Demo
![Demo](media/demo.gif)

## How to
The source code can be installed on your iPhone in one of three ways:

1. It can be cloned directly to your iPhone using Pythonista and [StaSh](https://github.com/ywangd/stash) (`git clone` only works when running using Python 2.7). 
2. It can be uploaded to your iCloud and imported into Pythonista
3. It can be downloaded to your computer and sent to your phone via email or Airdrop

You will need StaSh installed regardless to install the requirements. Unfortunately StaSh does not support the `-r` flag of `pip install`, so they have to be installed one-by-one (`Pillow` and `numpy` are installed with Pythonista, so you will just need `dlx`).

Once imported, configure it to be part of the share sheet via the following steps:

- Settings > Share Extension Shortcuts
- Click "+"
- Select `sudoku-solver/main.py` as the entry point
- Click "Add"

Once set up, follow the steps in the demo above to run it!

### Limitations
This program _only_ works with Pythonista, as it uses a Pythonista-specific module (`appex`) to get the input image. Additionally, it has only been tested on an iPhone XR running iOS 13.6.1 and Pythonista 3.3

## Acknowledgements
This program is the combination of other people's projects, so I would like to take the time to thank them!

- [Ole Zorn](https://omz-software.com/) - [Pythonista](https://omz-software.com/pythonista/index.html)
- [Pranoy Chowdhury](https://apps.apple.com/us/developer/pranoy-chowdhury/id952263202) - [Sudoku Extreme](https://apps.apple.com/us/app/sudoku-extreme-classic-number/id1451683705)
- [Nicolas Hahn](https://github.com/nicolashahn) - [`diffimg` library](https://github.com/nicolashahn/diffimg)
- [Jonathan Allan](https://github.com/jjallan) - [Sudoku solver using `dlx`](https://github.com/jjallan/sudoku)