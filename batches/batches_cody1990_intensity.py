import numpy as np
import config_ukf as c
import visualisation as vis


batch_name = "cody_int_sim" # Defines folder name
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
    # "simulation_seed": [42],
    "n_runs": [1],
    "n_trials": [10],
    "max_time_per_trial": [1.0],
    "planned_max_time_target": [1.0],
    "r_target": [0.025],
    "proprioceptive_intervention_on_angle": [0.0],
    "proprioceptive_intervention_bool": [True],
    "R_lqr": [np.diag([1e3, 0.1])], # High cost of shoulder torque (which is locked)
    "ukf_external_force_noise_sigma": [0.1],
    "torque_sigma_prop": [0.05],
    "prop_rad_sigma": [0.015, 0.06],
    "prop_omega_sigma": [0.015, 0.06],
    "prop_unit": ["rad"],
    "proprioceptive_offset_rad_j2":   [0.0, -5.0, -10.0, -15.0],
    "proprioceptive_offset_omega_j2": [0.0, -5.0, -10.0, -15.0],
    "visual_feedback": [False],
    "ukf_std_rad_j1_init": [1.0],
    "ukf_std_rad_j2_init": [1.0],
    "ukf_std_omega_j1_init": [1.0],
    "ukf_std_omega_j2_init": [1.0],
}

allowed_pairs = [
    {"prop_rad_sigma": 0.015, "prop_omega_sigma": 0.06, "proprioceptive_offset_rad_j2": 0.0, "proprioceptive_offset_omega_j2": 0.0},
    {"prop_rad_sigma": 0.015, "prop_omega_sigma": 0.06, "proprioceptive_offset_rad_j2": -5.0, "proprioceptive_offset_omega_j2": 0.0},
    {"prop_rad_sigma": 0.015, "prop_omega_sigma": 0.06, "proprioceptive_offset_rad_j2": -10.0, "proprioceptive_offset_omega_j2": 0.0},
    {"prop_rad_sigma": 0.015, "prop_omega_sigma": 0.06, "proprioceptive_offset_rad_j2": -15.0, "proprioceptive_offset_omega_j2": 0.0},
    {"prop_rad_sigma": 0.06, "prop_omega_sigma": 0.015, "proprioceptive_offset_rad_j2": 0.0, "proprioceptive_offset_omega_j2": 0.0},
    {"prop_rad_sigma": 0.06, "prop_omega_sigma": 0.015, "proprioceptive_offset_rad_j2": 0.0, "proprioceptive_offset_omega_j2": -5.0},
    {"prop_rad_sigma": 0.06, "prop_omega_sigma": 0.015, "proprioceptive_offset_rad_j2": 0.0, "proprioceptive_offset_omega_j2": -10.0},
    {"prop_rad_sigma": 0.06, "prop_omega_sigma": 0.015, "proprioceptive_offset_rad_j2": 0.0, "proprioceptive_offset_omega_j2": -15.0},
]
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
reps_resample = 50 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used
# reps_resample = 5 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used
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
    'torque_j2_ff', 'torque_j2', 'torque_j2_sigma_scaled',
    'proprioceptive_intervention_on_angle',
    ]
manipulated_vars = list(param_grid.keys())

for param in manipulated_vars:
    if param not in save_cols:
        save_cols.append(param)
