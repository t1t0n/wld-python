# Weber Local Descriptor
This is Python implementation of Weber Local Descriptor described in [this paper](https://ieeexplore.ieee.org/abstract/document/5204092). Current implementation is simplified version of one described in paper, it only uses Differential Excitation component. It's implemented using convolution operator from Scipy package for better performance.

### Requirements
This implementation requires Python version 3.5 or later to run.
It also needs Scipy and OpenCV packages. All dependencies are described in requirements.txt

### Usage
Example of usage:
```sh
$ python3 test.py 
```

### References:
J. Chen et al., "WLD: A Robust Local Image Descriptor," in IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 32, no. 9, pp. 1705-1720, Sept. 2010. [(Link)](https://ieeexplore.ieee.org/abstract/document/5204092)