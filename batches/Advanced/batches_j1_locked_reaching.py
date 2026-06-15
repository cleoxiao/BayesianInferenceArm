import numpy as np
import config_ukf as c
import visualisation as vis


batch_name = "j1_locked_reaching_1" # Defines folder name
save_results = True
param_grid = {
    "task_type": ["j1_locked_reaching"],
    "j1_locked_angle": [30.0],
    "deg_j2_hand_init": [160.0],
    "deg_j2_target_init": [np.array([-80.0, -40.0])],
    "self_terminate": [True],
    # "deg_j2_target_init": [np.array([-80.0, -80.0])],
    "omega_j2_target_init": [0.0],
    "sample_center": [False],
    # "simulation_seed": [42],
    "elbow_down": [False],
    "n_runs": [1],
    "n_trials": [100],
    "max_time_per_trial": [5.0],
    "planned_move_speed_ds_intercept_mu": [19.0],
    "planned_move_speed_ds_intercept_sigma": [5.0],
    "planned_move_speed_ds_slope_mu": [0.34],
    "planned_move_speed_ds_slope_sigma": [0.1],
    "min_time_before_movement": [0.0],
    "plan_trajectory_flag": [True],
    "v_radius_threshold": [5.0],
    "r_target": [0.025],
    "visual_offset": [np.array([0.0, 0.0])],
    "visual_feedback_rotation": [0.0],
    "proprioceptive_offset_rad_j2": [0.0],                      # Proprioceptive pos. offset
    "proprioceptive_offset_omega_j2": [0.0, 10.0, -10.0],       # Proprioceptive vel. offset
    "j2_motor_flexion_bias": [1.0],                             # Motor bias
    "j2_motor_extension_bias": [1.0],
    "prop_rad_j2_sigma": [6.25],                                 # Proprioceptive noise
    "prop_omega_j2_sigma": [5.0],
    "torque_j2_sigma_const": [0.002],                           # Motor noise
    "torque_j2_sigma_prop": [0.03],
    "kgain_j2": [100.0],                                        # PID gains
    "kp_j2": [1.0],
    "ki_j2": [0.2],
    "kd_j2": [1.0],
    "ki_max_j2": [0.0],
    "max_acceleration_j2": [10.0],
    "ukf_std_rad_j1_init": [2.0],                               # Initial state estimate covariance
    "ukf_std_rad_j2_init": [2.0],
    "ukf_std_omega_j1_init": [1.0],
    "ukf_std_omega_j2_init": [1.0],
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
reps_resample = 8 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used
reps_identical = 1

# Define all cols that should be saved after batch run
save_cols = [ 
    'seed', 
    'step', 'time', 'trial', 'run', 
    'rad_j2_target', 
    'true_rad_j2', 'true_omega_j2','true_alpha_j2', 
    'posterior_joint_rad_j2', 'posterior_joint_omega_j2',
    'proprioceptive_offset_rad_j2', 'proprioceptive_offset_omega_j2',
    'planned_max_time_target', 
    'j2_motor_flexion_bias', 'j2_motor_extension_bias'
    ]
manipulated_vars = list(param_grid.keys())

# The varying parameters from param_grid are now automatically added to the saved columns
# in batch_runs_parallel.py.
# for param in manipulated_vars:
#     if param not in save_cols:
#         save_cols.append(param)
