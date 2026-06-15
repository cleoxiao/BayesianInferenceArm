import numpy as np
import config_ukf as c
import visualisation as vis


batch_name = "batch_testing_all_tasks" # Defines folder name
save_results = True
param_grid = {
    "task_type": ["cody1990", "fournerett1997", "kordingwolpert2004","circular_following", 'seq_reaching'],
    "n_runs": [1],
    "n_trials": [1],
    "max_time_per_trial": [1.0],
    "planned_max_time_target": [1.0],
}
# Define visualization functions to run for each batch iteration
plot_functions = [  
    # vis.plotly_animation,
    # vis.plot_joint_angles_j1_locked
]
plot_extra_text = [
    "proprioceptive_offset_rad_j2", "proprioceptive_offset_omega_j2", 
    "j2_motor_flexion_bias", "j2_motor_extension_bias",
    "torque_j2_sigma_const", "torque_j2_sigma_prop"
]
plot_file_type = "png" # "pdf" or "png" # TODO: add png
reps_resample = 1 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used
reps_identical = 1

# Define all cols that should be saved after batch run
save_all_cols = False
save_cols = [ 
    'seed', 
    'step', 'time', 'trial', 'run', 
    'rad_j2_target', 
    'true_rad_j2', 'true_omega_j2','true_alpha_j2', 
    'posterior_rad_j2', 'posterior_omega_j2',
    'proprioceptive_offset_rad_j2', 'proprioceptive_offset_omega_j2',
    'posterior_sigma_rad_j2', 'posterior_sigma_omega_j2',
    'planned_max_time_target', 
    'j2_motor_flexion_bias', 'j2_motor_extension_bias',
    'run_name', 'run', 
    ]
manipulated_vars = list(param_grid.keys())

for param in manipulated_vars:
    if param not in save_cols:
        save_cols.append(param)
