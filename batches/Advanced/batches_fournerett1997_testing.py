import numpy as np
import config_ukf as c
import visualisation as vis


batch_name = "test" # Defines folder name
save_results = False
param_grid = {
    "task_type": ["testing"],
    "use_optimal_control_planner": [True],
    "use_receeding_horizon": [True],
    "passive_movement": [True],
    "max_time_per_trial": [2.5],
    "planned_max_time_target": [2.5],
    "n_runs": [1],
    # "simulation_seed": [42],
    "n_trials": [1],
    "visual_feedback_rotation": [0.0],
    "vis_p_sigma": [0.001],
    "prop_rad_sigma": [0.015],
    "prop_omega_sigma": [0.015],
    "prop_unit": ["rad"],
    "visual_feedback": [False, True],
    "proprioceptive_feedback_rad": [False, True],
    "proprioceptive_feedback_omega": [False, True],
    "ukf_std_rad_j1_init": [1.0],
    "ukf_std_rad_j2_init": [1.0],
    "ukf_std_omega_j1_init": [1.0],
    "ukf_std_omega_j2_init": [1.0],
    "ukf_external_force_noise_sigma": [0.1],
    "torque_sigma_prop": [0.05]
}
# Define visualization functions to run for each batch iteration
plot_functions = [  
    vis.plotly_animation,
    vis.plot_joint_angles,
]
plot_extra_text = [
    "proprioceptive_offset_rad_j1", "proprioceptive_offset_omega_j1", 
    "proprioceptive_offset_rad_j2", "proprioceptive_offset_omega_j2", 
    "j1_motor_flexion_bias", "j1_motor_extension_bias", 
    "j2_motor_flexion_bias", "j2_motor_extension_bias"
]
plot_file_type = "png" # "pdf" or "png" # TODO: add png
reps_resample = 1 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used
reps_identical = 1 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used


# Define all cols that should be saved after batch run
save_all_cols = False
save_cols = [ 
    'seed',
    'step', 'time', 'trial', 'run', 
    'vis_p_sigma',
    'posterior_hand_x', 'posterior_hand_y',
    'true_hand_x', 'true_hand_y',
    'vis_hand_x', 'vis_hand_y',
    'torque_j1', 'torque_j2', 'torque_j1_ff', 'torque_j2_ff',
    'true_rad_j1', 'true_rad_j2', 'true_omega_j1', 'true_omega_j2', 'true_alpha_j1', 'true_alpha_j2',
    'rad_j1_target', 'rad_j2_target', 
    'target_x', 'target_y',
    ]
manipulated_vars = list(param_grid.keys())

for param in manipulated_vars:
    if param not in save_cols:
        save_cols.append(param)
