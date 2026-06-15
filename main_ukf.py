import pandas as pd
import time
from tqdm import tqdm
import numpy as np
import visualisation as vis
import os

from agent_ukf import Agent
import config_ukf as c


def main():
    """
    Runs the main simulation loop for the agent.

    Initializes the agent, then iterates through runs, trials, and steps,
    calling the agent's methods to update its state and record results.
    Finally, completes and returns the simulation results.

    Returns:
        pd.DataFrame: A DataFrame containing the results of the simulation.
    """
    agent = Agent()
    agent.initiate_agent()
    print(f"n_steps_max: {agent.n_steps_max}")
    agent.row_saver = 0
    run_range = tqdm(range(c.n_runs), desc=f"Seqs of each {c.n_trials} trials") if c.n_runs >= c.n_trials else range(c.n_runs)
    for run in run_range:
        agent.start_new_run(run = run)
        step_run = 0
        
        trial_range = tqdm(range(c.n_trials), desc=f"Trials in seq {run+1}/{c.n_runs}") if c.n_runs < c.n_trials else range(c.n_trials)
        for trial in trial_range:
            agent.start_new_trial(trial = trial)

            step_range = tqdm(range(agent.n_steps_max), desc=f"Steps in trial {trial+1}/{c.n_trials}") if c.n_trials == 1 else range(agent.n_steps_max)
            for step in step_range:
                if agent.trial_ended_by_agent:
                    break
                agent.start_new_step(step = step, step_run = step_run)
                step_run += 1

            # End of step
        # End of trial
    # End of run
    agent.complete_results()
    r = agent.unpack_ukf_results_vectorized(agent.results)
    # Convert radians to degrees for all columns containing 'rad' or 'omega'
    cols_to_convert = [
        col for col in r.columns 
        if ('rad' in col or 'omega' in col) and 'cum' not in col
    ]

    if cols_to_convert:
        # Coerce to numeric, turning non-numeric into NaN, then convert to degrees
        r[cols_to_convert] = r[cols_to_convert].apply(pd.to_numeric, errors='coerce')
        r[cols_to_convert] = np.rad2deg(r[cols_to_convert])

    results = r.copy() # defragment
    return results

if __name__ == '__main__':
    time1 = time.time()
    results = main()
    time2 = time.time()
    print(f'Simulation complete in {round(time2 - time1, 2)} s')


    file_name = 'outputs/results.csv'
    
    # Ensure output directory exists
    output_dir = os.path.dirname(file_name)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
        print(f"Created output directory: {output_dir}")
    results.to_csv(file_name, index=False)

    def make_out_path(func_name):
        base_path = f"outputs/{func_name}/{func_name}"
        out_dir = os.path.dirname(base_path)
        if out_dir and not os.path.exists(out_dir):
            os.makedirs(out_dir)
        return base_path

    # Matplotlib plots
    vis.plot_joint_angles(results, output_filename=make_out_path('plot_joint_angles'))

    # Generate Plotly animation
    vis.plotly_animation(
        results[results['trial'] <= c.trials_to_animate-1], # -1 because trial 0 is the initial state
        frame_decimation = c.frame_decimation,
        annimation_speedup = 1,
        output_filename = make_out_path('plotly_animation')
    )


    # vis.plot_proprioceptive_errors(results)

    vis.plot_normalized_innovations(results, output_filename=make_out_path('plot_normalized_innovations'))

    vis.plot_sigma_contributions(results, output_filename=make_out_path('plot_sigma_contributions'))

    vis.plot_trajectory_analysis(results, output_filename=make_out_path('plot_trajectory_analysis'))

    vis.plot_visual_feedback_impact(results, output_filename=make_out_path('plot_visual_feedback_impact'))

    if c.task_type == 'patterson2017':
        vis.plot_reaching_trajectories_patterson2017(results, output_filename=make_out_path('plot_reaching_trajectories_patterson2017'))

    # vis.analyze_visual_feedback_impact_statistics(results)

    # results.to_csv('outputs/results_with_degrees.csv', index=False)

