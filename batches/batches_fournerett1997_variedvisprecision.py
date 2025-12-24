import numpy as np
import config_ukf as c
import visualisation as vis


batch_name = "fournerett1997_variedvisprecision10" # Defines folder name
save_results = True
param_grid = {
    "task_type": ["fournerett1997"],
    "elbow_down": [False],
    "use_optimal_control_planner": [True],
    "use_receeding_horizon": [True],
    "max_time_per_trial": [2.5],
    "planned_max_time_target": [2.5],
    "damping_factor_j1": [1.5],
    "damping_factor_j2": [1.5],
    "n_runs": [1],
    # "simulation_seed": [42],
    "n_trials": [25],
    # "n_trials": [1],
    "r_target": [0.002],
    # "visual_feedback_rotation": [0.0, 2, 5, 7, 10, -2, -5, -7, -10],
    # "visual_feedback_rotation": [0.0, 10, -10],
    "visual_feedback_rotation": [-10],
    "vis_p_sigma": [0.00025, 0.0005, 0.001, 0.002, 0.004],
    "proprioceptive_offset_rad_j1": [("normal", 0.0, 0.0)],
    "proprioceptive_offset_omega_j1": [("normal", 0.0, 0.0)],
    "proprioceptive_offset_rad_j2": [("normal", 0.0, 0.0)],
    "proprioceptive_offset_omega_j2": [("normal", 0.0, 0.0)],
    "j1_motor_flexion_bias": [("normal", 1.0, 0.0)],
    "j1_motor_extension_bias": [("normal", 1.0, 0.0)],
    "j2_motor_flexion_bias": [("normal", 1.0, 0.0)],
    "j2_motor_extension_bias": [("normal", 1.0, 0.0)],
    "Q_lqr": [np.diag([5.0, 5.0, 10.0, 10.0])],
    "R_lqr": [np.diag([0.1, 0.1])],
    "Q_lqr_final_multiplier_position": [5000.0],
    "Q_lqr_final_multiplier_velocity": [10.0],
    "prop_rad_sigma": [4.0],
    "prop_omega_sigma": [0.5],
    "proprioceptive_feedback_rad": [True],
    "proprioceptive_feedback_omega": [True],
    "visual_feedback": [True],
    "ukf_external_force_noise_sigma": [0.05],
    "ukf_std_tau_ext_init": [0.01],
    "ukf_tau_ext_rw_sigma": [0.01],
    "torque_sigma_const": [0.01],
    "torque_sigma_prop": [0.01],
    "ukf_std_rad_j1_init": [0.25],
    "ukf_std_rad_j2_init": [0.25],
    "ukf_std_omega_j1_init": [0.25],
    "ukf_std_omega_j2_init": [0.25],
}
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
reps_resample = 2 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used
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
