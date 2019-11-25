Intrinsic Image Decomposition
=============================

This repository contains the decomposition algorithm presented in the [paper](https://dl.acm.org/citation.cfm?id=2601206):

	Sean Bell, Kavita Bala, Noah Snavely
	"Intrinsic Images in the Wild"
	ACM Transactions on Graphics (SIGGRAPH 2014)

	@article{bell14intrinsic,
		author = "Sean Bell and Kavita Bala and Noah Snavely",
		title = "Intrinsic Images in the Wild",
		journal = "ACM Trans. on Graphics (SIGGRAPH)",
		volume = "33",
		number = "4",
		year = "2014",
	}
as well as a simple Python wrapper to the C++ dense CRF inference code from [Krahenbuhl et al 2013](http://graphics.stanford.edu/projects/drf/):

	Philipp Krähenbühl and Vladlen Koltun
    "Parameter Learning and Convergent Inference for Dense Random Fields"
    International Conference on Machine Learning (ICML) 2013

The dataset is hosted at http://intrinsic.cs.cornell.edu/.
- Note : The paper linked here is from ACM Digital Library. Make sure you have a valid subscription.

Dependencies
------------

The following libraries are needed:

:heavy_check_mark: Eigen (http://eigen.tuxfamily.org/) 

On Ubuntu 16.04, you can install with: `sudo apt-get install libeigen3-dev`

:heavy_check_mark: SnakeViz 

On Ubuntu 16.04 you can use PyPI's command: `pip install snakeviz`

:rotating_light: Numba (Proceed with caution) (https://pypi.org/project/numba/) 

Please check dependencies and proceed.

:heavy_check_mark: Python 3.5.2

:heavy_check_mark: Python packages (newer packages will likely work, though these are the exact versions that we used):

      Pillow==6.2.1
      Cython==0.29.14
      numpy==1.17.3
      scipy==1.3.2
      scikit-image==0.15.0
      scikit-learn==0.21.3
      
:heavy_check_mark: cProfile is an optional requirement for advanced users. It is a package included with Python, however before proceeding please make sure cProfile exists.
 
 Setting up a virtual environment like `virtualenv`  will help keep your Python environment safe. We recommend installing all dependencies using this.
 
:heavy_check_mark: For people who want a `plug and play` solution to all installation hassles, an installation-cum-running script named install_deps.sh is provided. Run it using the following command:

    bash install_deps.sh decompose.py [name_of_image_file]

:rotating_light: Note :- This installs `virtualenv` and `virtualenvwrapper` and edits your .bashrc on your machine.You have been warned.

Compile
-------

If on Ubuntu and you have installed Eigen3 to its default directory (/usr/include/eigen3), then you can build the C++ extension with:

    cd krahenbuhl2013/
    make

:rotating_light: Here you might get a ton of warnings, make sure you have properly specified the python version you are using.

If you are on another operating system or `eigen3` is in another directory, edit `krahenbuhl2013/setup.py` to change the directory.


Running
-------

:heavy_check_mark: Basic usage:

    python3 decompose.py [image_filename]

:rotating_light: Advanced (Checking memory stack):

    python3 -m cProfile -o decompose.prof decompose.py [image_filename]

:heavy_check_mark: Visualising and seeing important memory heuristics (to target CPU/GPU optimisations):

     snakeviz decompose.prof

All arguments:

    usage: decompose.py [-h] [-r <file>] [-s <file>] [-m <file>] [-j <file>]
                        [-p <file>] [-l] [-q] [--show-labels]
                        <file>

    positional arguments:
      <file>                Input image

    optional arguments:
      -h, --help            show this help message and exit
      -r <file>, --reflectance <file>
                            Reflectance layer output name (saved as sRGB image)
      -s <file>, --shading <file>
                            Shading layer output name (saved as sRGB image)
      -m <file>, --mask <file>
                            Mask filename
      -j <file>, --judgements <file>
                            Judgements file from the Intrinsic Images in the Wild
                            dataset
      -p <file>, --parameters <file>
                            Parameters file (JSON format). See params.py
                            for a list of parameters.
      -l, --linear          if specified, assume input is linear and generate
                            linear output, otherwise assume input is sRGB and
                            generate sRGB output
      -q, --quiet           if specified, don't print logging info
      --show-labels         if specified, also output labels


Image style management
-----------------------

All input images are assumed to be sRGB, and the output reflectance and shading layers are tone-mapped to sRGB.  If using linear images (e.g., the MIT Intrinsic Images Dataset, http://www.cs.toronto.edu/~rgrosse/intrinsic/), specify `--linear` and both input/output will remain linear.

Memory Optimisation
-----------------------

- For advanced users who want more performance out of their rigs, we have added a memory profiling for you to target those number-crunching intensive loops and use Just-in-time compiling `jit` to optimise the runtime. A popular library is `numba` which we have attempted to use, but is moderately tough to configure.

:rotating_light: To use `numba` make sure you have proper CUDA drivers and CUDA toolkit installed. For CPU based optimisations `llvm` is used.

:heavy_check_mark: Snakeviz will give you memeory profiling based on which you can target the function you want

:rotating_light: Note - `numba` is still an experimental library, with potential chances to corrupt your system. You have been warned.

Embedding in other projects
---------------------------

Our code was written to be modular and can be embedded in larger projects. The basic code for constructing the input and parameters can be found in `decompose.py` or is listed below:

```python
from solver import IntrinsicSolver
from input import IntrinsicInput
from params import IntrinsicParameters
import image_util

input = IntrinsicInput.from_file(
	image_filename,
	image_is_srgb=sRGB,
	mask_filename=mask_filename,
	judgements_filename=judgements_filename,
)

params = IntrinsicParameters.from_dict({
	'param1': ...,
	'param2': ...,
})

solver = IntrinsicSolver(input,params)
r, s, decomposition = solver.solve()

image_util.save(r_filename, r, mask_nz=input.mask_nz, rescale=True)
image_util.save(s_filename, s, mask_nz=input.mask_nz, rescale=True)
```

Some results
---------------------------------
:heavy_check_mark: Input Image:
![Paul Walker](https://github.com/DefUs3r/Intrinsic-Image-Decomposition/blob/master/samples/89e1aca9c871a9cd785c918c70fafc6f.jpg)

:heavy_check_mark: Reflectance Layer:
![Paul Walker reflectance](https://github.com/DefUs3r/Intrinsic-Image-Decomposition/blob/master/samples/89e1aca9c871a9cd785c918c70fafc6f-r.png)

:heavy_check_mark: Shading Layer:
![Paul Walker Shading](https://github.com/DefUs3r/Intrinsic-Image-Decomposition/blob/master/samples/89e1aca9c871a9cd785c918c70fafc6f-s.png)
