# ToBit
Converts images to simple pixel art, for example <br>
<a href="url"><img src="https://github.com/lukevastus/ToBit/blob/master/tests/mountain.jpeg?raw=true" width="400"></a>
<a href="url"><img src="https://github.com/lukevastus/ToBit/blob/master/tests/mountain_output_large.png?raw=true" width="400"></a>


## Package dependencies
<b>Python3</b>, NumPy, Matplotlib, PIL

## How it works
It uses <a href="https://en.wikipedia.org/wiki/K-means_clustering">K-Means</a> clustering for color segmentation (to reduce the number of colors, i.e. pixels with similar colors in the input image will now have the <b>same</b> color) in the L * a * b color space, and then merges adjacent pixels to create the blocky final image. 

## Usage 
```
usage: ToBit [-h] [-c [COLOR_NUM]] [-s [BLOCK_SIZE]] [-i MAX_ITER] [-m] [-n]
             [-r]
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
                        Size of pixel blocks to be merged. Larger number
                        indicates lower resolution, default 4
  -i MAX_ITER, --max_iter MAX_ITER
                        Maximum iterations for K-means clustering, default 20
  -m, --mode            During block conversion, adjacent pixels are merged
                        and the most frequent color would be kept
  -n, --no_clustering   Skip color clustering, overrides -c option
  -r, --reverse_pipeline
                        Revert the pipeline order: merge adjacent pixels first
                        then do clustering
```
