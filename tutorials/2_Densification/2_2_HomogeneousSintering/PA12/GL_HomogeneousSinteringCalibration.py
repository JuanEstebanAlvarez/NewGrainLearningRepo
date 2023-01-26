from grainlearning import CalibrationToolbox
from grainlearning.models import IOModel

executable = './tutorials/2_Densification/2_2_HomogeneousSintering/PA12/Exec_S3_HomogeneousSintering'
def run_sim(model, **kwargs):
    from math import floor, log
    import os
    # keep the naming convention consistent between iterations
    magn = floor(log(model.num_samples, 10)) + 1
    curr_iter = kwargs['curr_iter']
    # check the software name and version
    print("*** Running external software... ***\n")
    # loop over and pass parameter samples to the executable
    for i, params in enumerate(model.param_data):
        description = 'Iter' + str(curr_iter) + '-Sample' + str(i).zfill(magn)
        print(" ".join([executable, '%.8e %.8e' % tuple(params), description]))
        os.system(' '.join([executable, '%.8e %.8e' % tuple(params), description]))


calibration = CalibrationToolbox.from_dict(
    {
        "num_iter": 3,
        "model": {
            "obs_data_file": 'Obs_Dilatometer_PA12.dat',
            "obs_names":['deltaL'],
            "ctrl_name": 'time',
            "sim_name": 'Test',
            "sim_data_dir": './tutorials/2_Densification/2_2_HomogeneousSintering/PA12/',
            "param_names": ['c', 'gamma'],
            "param_mins": [0.1, 0.002],
            "param_maxs": [120, 0.006],
            "num_samples": 40,
            "sim_data_file_ext": '.txt',
            "sigma_tol": 0.001,
            "callback": run_sim,
        },
        "calibration": {
            "inference": {"ess_target": 0.3},
            "sampling": {
                "max_num_components": 2,
                "n_init": 1,
                "seed": 0,
                "cov_type": "full",
            }
        },
        "save_fig": 0,
        "model_type": IOModel
    }
)

calibration.run()

most_prob_params = calibration.get_most_prob_params()
print(f'Most probable parameter values: {most_prob_params}')

error_tolerance = 0.4
#
# error = most_prob_params - [50,0.003,0.0001,1000,0.1]
# assert abs(
#     error[0]) / 5.0 < error_tolerance, f"Model parameters are not correct, expected 50.0 but got {most_prob_params[0]}"
# assert abs(
#     error[1]) / 5.0 < error_tolerance, f"Model parameters are not correct, expected 0.003 but got {most_prob_params[1]}"
# assert abs(
#     error[2]) / 5.0 < error_tolerance, f"Model parameters are not correct, expected 0.0001 but got {most_prob_params[2]}"
# assert abs(
#     error[3]) / 5.0 < error_tolerance, f"Model parameters are not correct, expected 1000 but got {most_prob_params[3]}"
# assert abs(
#     error[4]) / 5.0 <
#
# error = most_prob_params - [50,0.003,0.0001,1000,0.1]
# assert abs(
#     error[0]) / 5.0 < error_tolerance, f"Model parameters are not correct, expected 50.0 but got {most_prob_params[0]}"
# assert abs(
#     error[1]) / 5.0 < error_tolerance, f"Model parameters are not correct, expected 0.003 but got {most_prob_params[1]}"
# assert abs(
#     error[2]) / 5.0 < error_tolerance, f"Model parameters are not correct, expected 0.0001 but got {most_prob_params[2]}"
# assert abs(
#     error[3]) / 5.0 < error_tolerance, f"Model parameters are not correct, expected 1000 but got {most_prob_params[3]}"
# assert abs(
#     error[4]) / 5.0 < error_tolerance, f"Model parameters are not correct, expected 0.1 but got {most_prob_params[4]}"