#!/usr/bin/env python3

import sys, os
import numpy as np
from skimage.color import rgb2lab


def color_distance(color_1, color_2, delta_e=False):
    # return np.sqrt(np.sum((color_1 - color_2) ** 2))
    # return np.absolute(np.sum((color_1 - color_2)))
    # return np.sqrt(np.sum((color_1 - color_2) * np.asarray([2, 4, 3]) ** 2))
    color_1_lab = rgb2lab(color_1)
    color_2_lab = rgb2lab(color_2)
    return np.sqrt(np.sum((color_1_lab - color_2_lab) ** 2))

def cluster_pixels(image, num_centroids, max_iter=20):
    output = np.zeros(image.shape)
    x = np.random.choice(image.shape[0], num_centroids, replace=False)
    y = np.random.choice(image.shape[1], num_centroids, replace=False)
    # centroids = image[x, y, :]
    centroids = [image[x[i], y[i], :] for i in range(num_centroids)]

    centroid_map = np.zeros(image.shape[:-1])
    old_centroids = centroids
    new_centroids = [np.ones(old_centroids[0].shape) for i in range(num_centroids)]
    counter = 0

    while not all(np.allclose(x, y) for x, y in zip(old_centroids, new_centroids)):
        if counter == max_iter:
            break

        print('Iteration %d' % counter)

        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                distances = np.zeros(num_centroids)
                for k in range(num_centroids):
                    distances[k] = np.sqrt(np.sum(centroids[k] - image[i, j, :]) ** 2)
                centroid_map[i, j] = np.argmin(distances)

        old_centroids = centroids.copy()
        for i in range(num_centroids):
            if image[centroid_map == i].size:
                new_centroids[i] = np.mean(image[centroid_map == i], axis=0)
            else:
                new_centroids[i] = old_centroids[i]

        centroids = new_centroids.copy()
        # print(centroids)
        counter += 1

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            output[i, j, :] = centroids[int(centroid_map[i, j])]

    return output


def convert_blocks(image, block_size, color_mode):
    if block_size > min(image.shape[0], image.shape[1]) or block_size <= 0:
        raise ValueError('Invalid block size')

    new_height = image.shape[0] // block_size
    new_width = image.shape[1] // block_size
    output = np.zeros((new_height, new_width, image.shape[2]))

    for i in range(new_height):
        for j in range(new_width):
            block = image[i * block_size:(i + 1) * block_size, j * block_size:(j + 1) * block_size, :]
            if color_mode == 'mean':
                output[i, j, :] = np.mean(block, axis=(0, 1))
            # elif color_mode == 'mode':
            #     output[i, j, :] = np.argmax([np.bincount(x) for x in block.reshape(-1, 3).T], axis=1)
            # elif color_mode == 'max':
            #     output[i, j, :] = np.max(block, axis=(0, 1))
            else:
                raise ValueError('Unknown option for color_mode')

    return output



