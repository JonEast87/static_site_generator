# Static Site Generator

--- --- --- --- --- ---

## What this does
Translates your `.md` files into `.html`, including any assets located in `./static` for additional styling or photos.

### How to use
If you are interested in using this for fun then a few things:

1. `./static` holds all the css and images you desire to style your page.
2. `./content` is where you will put your `.md` files, make folders that **include only one** `.md` file each, if you want multiple pages.
3. `./public` will hold all generated pages after running the primary command with the folders nested exactly as they are in `./content`

### Commands
* `sh main.sh` will run the program to generate the pages and host the page locally at port 8888
* `sh test.sh` will run the suite of tests previously treated when creating this program