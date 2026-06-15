import numpy as np
import config_ukf as c
import visualisation as vis


batch_name = "patterson_r_delta_13" # Defines folder name
save_results = True
param_grid = {
    "task_type": ["patterson2017"],
    "use_optimal_control_planner": [True],
    "use_receeding_horizon": [True],
    "apply_proprioceptive_noise": [True],
    "apply_visual_noise": [True],
    "apply_motor_noise": [True],
    "use_tv_planner": [False],
    # "straight_line_cost": [0.0, 1.0, 10.0, 100.0],
    "planned_max_time_target" : [1.6],
    "max_time_per_trial" : [1.6],
    "simulation_seed": [10],
    "planning_torque_mixing_time" : [0.01],
    "len_upper_arm_believed_offset": [0.0,],
    "len_lower_arm_believed_offset": [0.0,],
    # "len_upper_arm_believed_offset": [0.0, -0.02, -0.04],
    # "len_lower_arm_believed_offset": [0.0, 0.02, 0.04],
    "m_upper_arm_believed_offset": [0.0],
    "m_lower_arm_believed_offset": [0.0],
    # "m_upper_arm_believed_offset": [0.0, 0.25, -0.25],
    # "m_lower_arm_believed_offset": [0.0, 0.25, -0.25],
    "n_runs": [1],
    "n_trials": [5],
    "patterson_n_trials_visual_feedback": [0],
    "patterson_dir_final_target": [60],
    # "proprioceptive_offset_rad_j1": [("normal", 5.0, 0.0)],
    "proprioceptive_offset_rad_j1": [("normal", 0.0, 0.0)],
    "proprioceptive_offset_omega_j1": [("normal", 0.0, 0.0)],
    # "proprioceptive_offset_rad_j2": [("normal", -5.0, 0.0)],
    "proprioceptive_offset_rad_j2": [("normal", 0.0, 0.0)],
    "proprioceptive_offset_omega_j2": [("normal", 0.0, 0.0)],
    "proprioceptive_intervention_bool": [True],
    "j1_motor_flexion_bias": [("normal", 1.0, 0.0)],
    "j1_motor_extension_bias": [("normal", 1.0, 0.0)],
    "j2_motor_flexion_bias": [("normal", 1.0, 0.0)],
    "j2_motor_extension_bias": [("normal", 1.0, 0.0)],
    "Q_lqr": [np.diag([250.0, 250.0, 50.0, 50.0])],
    "R_lqr": [np.diag([0.1, 0.1])],
    "R_lqr_delta": [np.diag([0.0, 0.0])],
    "Q_lqr_final_multiplier_position": [1000.0],
    "Q_lqr_final_multiplier_velocity": [10.0],
    "use_dare": [False],
    "prop_rad_sigma": [4.0],
    "prop_omega_sigma": [0.5],
    "use_oscillator_controller": [True],
    "oscillator_omega": [2.0, 4.0, 6.0],
    "proprioceptive_feedback_rad": [True],
    "proprioceptive_feedback_omega": [True],
    "visual_feedback": [False],
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
    vis.plotly_animation,
    vis.plot_reaching_trajectories_patterson2017,
    vis.plot_joint_angles
]
plot_extra_text = [
    "Q_lqr",
    "R_lqr",
]
plot_file_type = "pdf" # "pdf" or "png" # TODO: add png
reps_resample = 1 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used
reps_identical = 1 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used


# Define all cols that should be saved after batch run
save_all_cols = False
save_cols = [
    "dt", 
    "visual_offset_x", "visual_offset_y", "circular_target_movement_c_x", "circular_target_movement_c_y", "circular_target_movement_r", "r_target",
    'seed', 
    'step', 'time', 'trial', 'run', 'run_name',
    'true_hand_x', 'true_hand_y', 'vis_hand_x', 'vis_hand_y','circular_target_rads_cum',
    'posterior_hand_x', 'posterior_hand_y',
    'torque_j1', 'torque_j2', 'torque_j1_ff', 'torque_j2_ff',
    'true_rad_j1', 'true_rad_j2', 'true_omega_j1', 'true_omega_j2', 'true_alpha_j1', 'true_alpha_j2',
    'posterior_rad_j1', 'posterior_rad_j2', 'posterior_omega_j1', 'posterior_omega_j2', 'posterior_alpha_j1', 'posterior_alpha_j2',
    'rad_j1_target', 'rad_j2_target', 
    'target_x', 'target_y',
    'p_target_home_x', 'p_target_home_y',
    'p_target_out_x', 'p_target_out_y',
    'p_target_final_x', 'p_target_final_y',
    ]
manipulated_vars = list(param_grid.keys())

for param in manipulated_vars:
    if param not in save_cols:
        save_cols.append(param)
