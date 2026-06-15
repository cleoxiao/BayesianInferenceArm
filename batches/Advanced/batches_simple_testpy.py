import numpy as np
import config_ukf as c
import visualisation as vis


batch_name = "simple_reaching_task_test" # Defines folder name
save_results = True
param_grid = {
    "task_type": ["simple_reaching_task"],
    "n_runs": [1], # number of runs of n_trials
    "n_trials": [1], # number of trials within a run
    "planned_max_time_target" : [2.0], # The amount of time in which the agent will try to reach the target 
    "max_time_per_trial": [3.0], # each trial will end after e.g. 2 seconds
    "self_terminate": [True], # if the agent shoulder end the trial when within dist r_target
    "r_target" : [0.005], # size of target, only relevant self_terminate = True
    # "apply_proprioceptive_noise": [False], # Whether to apply proprioceptive noise, useful for troubleshooting inference
    # "apply_visual_noise": [False], # Whether to apply visual noise, useful for troubleshooting inference
    # "apply_motor_noise": [False], # Whether to apply motor noise, useful for troubleshooting inference
    "visual_offset": [np.array([0.0, 0.0]), np.array([0.01, 0.0]), np.array([-0.01, 0.0])], # a cartesion offset added to visual feedback
    "vis_p_sigma": [0.001], # amount of visual noise
    "prop_rad_sigma": [0.06], # amount of proprioceptive positional noise, in joint space
    "prop_omega_sigma": [0.015], # amount of proprioceptive velocity noise, in joint space
    "p_target": [np.array([0.0, 0.3])], # position of the target, cartesian space
    "p_hand_init": [np.array([0.0, 0.0])], # hand start position
    "p_shoulder_init": [np.array([0.2, -0.2])], # shoulder position (stationary within trial)
    

}

# Define visualization functions to run for each batch iteration
plot_functions = [  
    vis.plotly_animation, 
    # vis.plot_joint_angles,
]
plot_file_type = "pdf" # "pdf" or "png" # TODO: add png
reps_resample = 1 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used
reps_identical = 1 # repetitions per parameter setting, spread across different cores, e.g. if param_grid gives 3 combinations and reps = 4, then 12 cores will be used


# Define all cols that should be saved after batch run
save_all_cols = False
save_cols = [
    "dt", 
    "visual_offset_x", "visual_offset_y", "r_target",
    'seed', 
    'step', 'time', 'trial', 'run', 'run_name',
    'true_hand_x', 'true_hand_y', 'vis_hand_x', 'vis_hand_y','circular_target_rads_cum',
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
