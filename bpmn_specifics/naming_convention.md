### How-to on creating your own specifics for the bpmn

All described here should be saved as a .csv file. The current convention of creating specifics:
1. The column names should be as follows: `task_name, time_dist, time_unit, costs_dist, costs_unit, profit_dists, profit_unit`
2. The `task_name` should be exactly the same as in the bpmn diagram file - otherwise the program will not work.
3. In the columns `time_dist, costs_dist, profit_dist` there should be written a distribution that we want the simulated data to be generetad from for the specific task. Currently supported distributions and their naming conventions:
    - linear
    - normal
    - lognormal   
