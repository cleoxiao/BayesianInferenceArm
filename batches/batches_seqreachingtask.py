import numpy as np
import config_ukf as c
import visualisation as vis


batch_name = "seq_reaching_task_sim" # Defines folder name
save_results = True
param_grid = {
    "task_type": ["seq_reaching"],
    "use_optimal_control_planner": [True],
    "use_receeding_horizon": [True],
    # "apply_proprioceptive_noise": [False],
    # "apply_visual_noise": [False],
    # "apply_motor_noise": [False],
    "planned_max_time_target": [1.0],
    "max_time_per_trial": [1.0],
    "vary_p_shoulder_init": [False],
    "p_target_even": [np.array([0.0, 0.38])],
    "p_target_odd": [np.array([0.0, 0.0])],
    "n_runs": [10],
    # "simulation_seed": [42],
    "n_trials": [3],
    # "visual_feedback_rotation": [-7.5],
    "visual_feedback_rotation": [0, 7.5, -7.5],
    "vis_p_sigma": [0.001],
    # "prop_rad_sigma": [0.06],
    "prop_rad_sigma": [0.015, 0.06],
    # "prop_omega_sigma": [0.015],
    "prop_omega_sigma": [0.015, 0.06],
    "prop_unit": ["rad"],
    "visual_feedback": [False],
    "visual_intervention_bool": [True],
    "visual_feedback_bool_onset": [0.1],
    "visual_feedback_duration": [0.5],
    "ukf_std_rad_j1_init": [1.0],
    "ukf_std_rad_j2_init": [1.0],
    "ukf_std_omega_j1_init": [1.0],
    "ukf_std_omega_j2_init": [1.0],
    "ukf_external_force_noise_sigma": [0.1],
    "torque_sigma_prop": [0.05]
}

allowed_pairs = [
    {"prop_rad_sigma": 0.015, "prop_omega_sigma": 0.06},
    {"prop_rad_sigma": 0.06, "prop_omega_sigma": 0.015},
]
# Define visualization functions to run for each batch iteration
plot_functions = [  
    # vis.plotly_animation,
    # vis.plot_joint_angles
]
plot_extra_text = [
    "proprioceptive_offset_rad_j1", "proprioceptive_offset_omega_j1", 
    "proprioceptive_offset_rad_j2", "proprioceptive_offset_omega_j2", 
    "j1_motor_flexion_bias", "j1_motor_extension_bias", 
    "j2_motor_flexion_bias", "j2_motor_extension_bias"
]
plot_file_type = "png" # "pdf" or "png" # TODO: add png
reps_resample = 5 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used
reps_identical = 1 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used


# Define all cols that should be saved after batch run
save_all_cols = False
save_cols = [ 
    "dt", 
    "visual_offset_x", "visual_offset_y", "r_target",
    'seed', 
    'step', 'time', 'trial', 'run', 'run_name',
    'true_hand_x', 'true_hand_y', 'vis_hand_x', 'vis_hand_y',
    'posterior_hand_x', 'posterior_hand_y',
    'torque_j1', 'torque_j2', 'torque_j1_ff', 'torque_j2_ff',
    'true_rad_j1', 'true_rad_j2', 'true_omega_j1', 'true_omega_j2', 'true_alpha_j1', 'true_alpha_j2',
    'posterior_rad_j1', 'posterior_rad_j2', 'posterior_omega_j1', 'posterior_omega_j2',
    'posterior_sigma_rad_j1', 'posterior_sigma_omega_j1',
    'posterior_sigma_rad_j2', 'posterior_sigma_omega_j2',
    'vis_hand_j1', 'vis_hand_j2',
    'rad_j1_target', 'rad_j2_target', 
    'target_x', 'target_y', 'vis_p_sigma',
    'visual_feedback',
    'rad_j1_target', 'rad_j2_target',
    ]
manipulated_vars = list(param_grid.keys())

for param in manipulated_vars:
    if param not in save_cols:
        save_cols.append(param)
