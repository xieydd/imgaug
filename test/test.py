"""
Automatically run tests for this library.
Run tests from imgaug/ via
    python -m test.test

"""
from __future__ import print_function, division, absolute_import

import time

from . import test_imgaug
from . import test_parameters
from .augmenters import test_arithmetic
from .augmenters import test_blur
from .augmenters import test_color
from .augmenters import test_contrast
from .augmenters import test_convolutional
from .augmenters import test_flip
from .augmenters import test_geometric
from .augmenters import test_meta
from .augmenters import test_mixed_files
from .augmenters import test_overlay
from .augmenters import test_segmentation
from .augmenters import test_size


def main():
    time_start = time.time()

    test_imgaug.main()
    test_parameters.main()
    test_arithmetic.main()
    test_blur.main()
    test_color.main()
    test_contrast.main()
    test_convolutional.main()
    test_flip.main()
    test_geometric.main()
    test_meta.main()
    test_mixed_files.main()
    test_overlay.main()
    test_segmentation.main()
    test_size.main()

    time_end = time.time()
    print("Finished all tests without errors in %.4fs." % (time_end - time_start,))


if __name__ == "__main__":
    main()
