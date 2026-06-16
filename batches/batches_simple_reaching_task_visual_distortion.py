import numpy as np
import config_ukf as c
import visualisation as vis


# Simple reaching task - Visual distortion (spatial mapping error)
# Models interaction scenarios where the cursor position does not match hand position:
#   - Rotation: cursor moves at an angle relative to hand direction
#     (e.g., rotated display, unusual tablet-to-screen mapping, prism adaptation)
#
# visual_intervention_bool=True enables the distortion pipeline (rotate_visual_feedback).
# visual_feedback_rotation is in degrees. visual_feedback=True keeps cursor visible throughout.
#
batch_name = "simple_reaching_task_visual_distortion"
save_results = True
param_grid = {
    "task_type": ["simple_reaching_task"],
    "planned_max_time_target": [2.0],
    "max_time_per_trial": [3.0],
    "p_target": [np.array([0.0, 0.3])],
    "p_hand_init": [np.array([0.0, 0.0])],
    "p_shoulder_init": [np.array([0.2, -0.2])],
    "self_terminate": [True],
    "r_target": [0.005],
    "n_runs": [10],
    "n_trials": [1],
    "visual_feedback": [True],
    "visual_intervention_bool": [True],               # enable distortion pipeline
    "visual_feedback_rotation": [0.0, 10.0, -10.0, 20.0, -20.0],  # degrees; positive = CCW
    "vis_p_sigma": [0.001],
    "apply_visual_noise": [False],
    "prop_rad_sigma": [0.06],
    "prop_omega_sigma": [0.015],
    "prop_unit": ["rad"],
    "ukf_std_rad_j1_init": [1.0],
    "ukf_std_rad_j2_init": [1.0],
    "ukf_std_omega_j1_init": [1.0],
    "ukf_std_omega_j2_init": [1.0],
    "ukf_external_force_noise_sigma": [0.1],
    "torque_sigma_prop": [0.05],
}


plot_functions = [
    vis.plotly_animation,
    vis.plot_movement_path_with_endpoints
]
plot_extra_text = [
    "visual_feedback_rotation"
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
