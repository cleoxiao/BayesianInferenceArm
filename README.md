# Bayesian arm

## UKF Variables Glossary

This is a glossary of variables used in the Unscented Kalman Filter (UKF) implementation in `ukf_version/agent_ukf.py`.

### UKF Parameters
*   `L_ukf`: The number of states in the UKF state vector. It is set to 4, representing the four states: joint 1 angle (`rad_j1`), joint 2 angle (`rad_j2`), joint 1 angular velocity (`omega_j1`), and joint 2 angular velocity (`omega_j2`).
*   `ukf_alpha`: UKF parameter that determines the spread of the sigma points.
*   `ukf_beta`: UKF parameter used to incorporate prior knowledge of the distribution of the state. For Gaussian distributions, beta=2 is optimal.
*   `ukf_kappa`: Secondary UKF scaling parameter, usually set to 0.
*   `lambda_ukf`: UKF scaling parameter calculated from `ukf_alpha`, `L_ukf`, and `ukf_kappa`.

### State and Covariance
*   `x_ukf`: The true (simulated) state of the system, containing joint angles and velocities. Used to initialize the filter's state.
*   `x_est_ukf`: The estimated state vector of the UKF. This represents the filter's belief about the current state of the arm's joints and velocities.
*   `P_ukf`: The state covariance matrix. This matrix represents the uncertainty in the state estimate (`x_est_ukf`).
*   `x_pred_ukf`: The predicted state vector after the UKF prediction step.
*   `P_pred_ukf`: The predicted state covariance matrix after the prediction step.
*   `Q_ukf`: The process noise covariance matrix. It represents the uncertainty in the arm's dynamics (e.g., noise in motor execution).

### Measurement
*   `num_measurements_ukf`: The number of possible sensory measurements (6 in this case).
*   `z_ukf`: The measurement vector. It contains the sensory information available at a given time step: `[vis_x, vis_y, prop_rad1, prop_rad2, prop_omega1, prop_omega2]`. `vis_x` and `vis_y` are visual estimations of hand position, while the `prop_` variables are proprioceptive estimates of joint angles and velocities.
*   `R_ukf`: The measurement noise covariance matrix. It represents the uncertainty/noise in the sensory measurements.
*   `measurement_available_mask`: A boolean mask indicating which sensory measurements are available at the current time step.

### Sigma Points
*   `n_sigma_points`: The number of sigma points used in the UKF.
*   `sigmas_ukf`: The array holding the sigma points, which are sample points chosen to capture the state's mean and covariance.
*   `W_m_ukf`: The weights for the sigma points, used for calculating the mean of the state.
*   `W_c_ukf`: The weights for the sigma points, used for calculating the covariance of the state.
*   `sigmas_f_ukf`: The sigma points after being passed through the state transition function (these are the predicted sigma points).

### Cartesian Space
*   `L_cart_ukf`: The dimensionality of the Cartesian state space (6: `x_h, y_h, vx_h, vy_h, x_e, y_e`, representing hand and elbow positions and velocities).
*   `x_est_cartesian_ukf`: The estimated state in Cartesian space, derived from the joint-space estimate `x_est_ukf`.
*   `P_est_cartesian_ukf`: The covariance of the Cartesian state estimate.
*   `sigmas_cartesian_transformed`: Sigma points transformed into Cartesian space.

### Innovation and Kalman Gain
*   `full_innovation_ukf`: The raw innovation vector, which is the difference between the actual measurement (`z_k`) and the predicted measurement (`E[h(x_pred_k)]`).
*   `normalized_innovation_ukf`: The innovation normalized by its covariance. This serves as a measure of "surprise" for the filter.
*   `diag_P_z_full_ukf`: The diagonal of the predicted measurement covariance matrix, representing the variance of each predicted measurement.
*   `K_ukf`: The Kalman gain. It determines how much the state estimate is corrected based on the innovation.
*   `P_xz_available`: The cross-covariance matrix between the state and the available measurements.
*   `innovation_available`: The innovation for the available measurements.