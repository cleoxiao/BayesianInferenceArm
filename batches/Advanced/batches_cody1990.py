import numpy as np
import config_ukf as c
import visualisation as vis


# batch_name = "cody_intensity2" # Defines folder name
batch_name = "cody_test9" # Defines folder name
save_results = True
param_grid = {
    "task_type": ["cody1990"],
    "j1_locked_angle": [30.0],
    "deg_j2_hand_init": [160.0],
    "deg_j2_target_init": [np.array([-30.0, -30.0])],
    "omega_j2_target_init": [0.0],
    "est_tau_ext": [False],
    "self_terminate": [False],
    "use_optimal_control_planner": [True],
    "time_to_max_force": [0.25],
    # "simulation_seed": [42],
    "elbow_down": [False],
    "n_runs": [1],
    "n_trials": [20],
    # "n_trials": [1],
    "max_time_per_trial": [1.0],
    "planned_max_time_target": [1.0],
    "min_time_before_movement": [0.0],
    "plan_trajectory_flag": [True],
    "v_radius_threshold": [5.0],
    "r_target": [0.025],
    "visual_offset": [np.array([0.0, 0.0])],
    "visual_feedback_rotation": [0.0],
    # "proprioceptive_offset_rad_j2": [0.0],                      # Proprioceptive pos. offset
    "proprioceptive_offset_omega_j2": [0.0, -5.0, -7.5, -10.0],       # Proprioceptive vel. offset
    # "proprioceptive_offset_omega_j2": [-100.0],       # Proprioceptive vel. offset
    "proprioceptive_intervention_bool": [True],
    "j2_motor_flexion_bias": [1.0],                             # Motor bias
    "j2_motor_extension_bias": [1.0],
    "Q_lqr": [np.diag([5.0, 5.0, 5.0, 5.0])],
    "R_lqr": [np.diag([1e3, 0.1])],
    "Q_lqr_final_multiplier_position": [5000.0],
    "Q_lqr_final_multiplier_velocity": [10.0],
    "prop_rad_sigma": [4.0],
    "prop_omega_sigma": [0.5],
    "proprioceptive_feedback_rad": [True],
    "proprioceptive_feedback_omega": [True],
    "ukf_external_force_noise_sigma": [0.05],
    "ukf_std_tau_ext_init": [0.01],
    "ukf_tau_ext_rw_sigma": [0.01],
    "torque_sigma_const": [0.01],
    "torque_sigma_prop": [0.01],
    "ukf_std_rad_j1_init": [1.0],                               # Initial state estimate covariance
    "ukf_std_rad_j2_init": [1.0],
    "ukf_std_omega_j1_init": [.05],
    "ukf_std_omega_j2_init": [.05],
}
# Define visualization functions to run for each batch iteration
plot_functions = [  
    # vis.plotly_animation,
    vis.plot_joint_angles_j1_locked
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
