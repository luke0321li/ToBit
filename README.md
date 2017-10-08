# ToBit
Converts images to simple pixel art, for example <br>
<a href="url"><img src="https://github.com/lukevastus/ToBit/blob/master/tests/cham.jpg?raw=true" width="200"></a>
<a href="url"><img src="https://github.com/lukevastus/ToBit/blob/master/tests/cham_output_large.png?raw=true" width="200"></a>


## Package dependencies
<b>Python3</b>, NumPy, Matplotlib, PIL

## Usage 
```
usage: ToBit [-h] [-c [COLOR_NUM]] [-s [BLOCK_SIZE]]
             [input_path] [output_path]

positional arguments:
  input_path            Input image file path
  output_path           Output image file path, default: tobit_output.png in
                        current directory

optional arguments:
  -h, --help            show this help message and exit
  -c [COLOR_NUM], --color_num [COLOR_NUM]
                        Number of colors in the final image, default 8.
  -s [BLOCK_SIZE], --block_size [BLOCK_SIZE]
                        Size of pixel blocks. Larger number indicates lower
                        resolution, default 4
```