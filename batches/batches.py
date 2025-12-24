import numpy as np
import config_ukf as c
import visualisation as vis


batch_name = "patterson_test" # Defines folder name
save_results = False
param_grid = {
    "task_type": ["patterson2017"],
    "sample_center": [False],
    "n_runs": [1],
    "n_trials": [99],
    # "patterson_dir_final_target": [60, 80, 100, 120, 140, 160, 180],
    # "proprioceptive_offset_rad_j1": [0, 5],
    # "proprioceptive_offset_omega_j1": [0, .5],
    # "proprioceptive_offset_rad_j2": [0],
    # "proprioceptive_offset_omega_j2": [0],
    "j1_motor_bias": [0, 1.15, 0.85],
    "j2_motor_bias": [0],
}
# Define visualization functions to run for each batch iteration
plot_functions = [  
    vis.plot_reaching_trajectories_patterson2017
]
plot_file_type = "png" # "pdf" or "png" # TODO: add png
reps = 1 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used


# Define all cols that should be saved after batch run
save_cols = [ 
    'seed',
    'step', 'time', 'trial', 'run', 'p_target', 
    'p_hand', 'vis_p_hand', 'p_hand_posterior_mu',
    'visual_offset', 
    'circular_target_rads_cum',
    'visual_feedback', 'proprioceptive_feedback_type', 'min_time_before_movement',
    'I_j1_est_mu', 'I_j2_est_mu', 'I_j1_est_sigma', 'I_j2_est_sigma', 'I_j1', 'I_j2',
    ]
manipulated_vars = list(param_grid.keys())

for param in manipulated_vars:
    if param not in save_cols:
        save_cols.append(param)
