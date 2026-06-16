import numpy as np
import config_ukf as c
import visualisation as vis


# Simple reaching task - Baseline
# Full, clean visual feedback throughout the reaching movement. No spatial distortion, no added noise.
# Models an ideal interaction technique with perfect cursor-hand correspondence.
# visual_feedback=True keeps the cursor visible for the entire trial.
batch_name = "simple_reaching_task_baseline"
save_results = True
param_grid = {
    "task_type": ["simple_reaching_task"],
    "planned_max_time_target": [2.0], # The amount of time in which the agent will try to reach the target
    "max_time_per_trial": [3.0], # each trial will end after e.g. 2 seconds
    "p_target": [np.array([0.0, 0.3])], # position of the target, cartesian space
    "p_hand_init": [np.array([0.0, 0.0])], # hand start position
    "p_shoulder_init": [np.array([0.2, -0.2])], # shoulder position (stationary within trial)
    "self_terminate": [True], # if the agent shoulder end the trial when within dist r_target
    "r_target": [0.005], # size of target, only relevant self_terminate = True
    "n_runs": [1], # number of runs of n_trials
    "n_trials": [1], # number of trials within a run
    "visual_feedback": [True], # cursor always visible
    "visual_intervention_bool": [False], # no spatial distortion
    "visual_feedback_rotation": [0.0], # no rotational distortion
    "visual_offset": [np.array([0.0, 0.0])], # no visual offset
    "vis_p_sigma": [0.001], # amount of visual noise
    "apply_visual_noise": [False], # perfectly clean cursor signal
    "prop_rad_sigma": [0.06], # amount of proprioceptive positional noise, in joint space
    "prop_omega_sigma": [0.015], # amount of proprioceptive velocity noise, in joint space
    "prop_unit": ["rad"], # unit of the proprioceptive feedback in radians
    "ukf_std_rad_j1_init": [1.0], # Initial uncertainty for rad_j1 (degrees)
    "ukf_std_rad_j2_init": [1.0], # Initial uncertainty for rad_j2 (degrees)
    "ukf_std_omega_j1_init": [1.0], # Initial uncertainty for omega_j1 (degrees/sec)
    "ukf_std_omega_j2_init": [1.0], # Initial uncertainty for omega_j2 (degrees/sec)
    "ukf_external_force_noise_sigma": [0.1], # Set to 0 to disable external force noise; assumes that all forces are correctly modelled by the agent UKF
    "torque_sigma_prop": [0.05], # proportional torque noise density factor (unitless, scales efferent torque, then effectively becomes Nm/sqrt(s))
}

plot_functions = [
    vis.plotly_animation,
    vis.plot_movement_path_with_endpoints
]
plot_file_type = "png"
reps_resample = 1
reps_identical = 1

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
