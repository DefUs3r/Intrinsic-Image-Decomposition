import copy
import json
import random
import hashlib
import numpy as np

ALL_PARAMS = [
        'n_iters',
        'n_crf_iters',
        'split_clusters',
        'kmeans_n_clusters',
        'kmeans_max_samples',
        'shading_blur_init_method',
        'shading_blur_method',
        'shading_blur_log',
        'shading_blur_sigma',
        'shading_blur_bilateral_sigma_range',
        'shading_blur_iteration_pow',
        'shading_smooth_k',
        'kmeans_intensity_scale',
        'abs_reflectance_weight',
        'abs_shading_log',
        'abs_shading_weight',
        'abs_shading_gray_point',
        'shading_target_weight',
        'shading_target_norm',
        'shading_target_chromaticity',
        'chromaticity_weight',
        'chromaticity_norm',
        'pairwise_intensity_log',
        'pairwise_intensity_chromaticity',
        'pairwise_weight',
        'theta_p',
        'theta_l',
        'theta_c',
        'stage2_norm',
        'stage2_chromaticity',
        'stage2_maintain_median_intensity',
    ]