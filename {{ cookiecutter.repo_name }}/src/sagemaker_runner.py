from sagemaker.sklearn import SKLearn
import os
import tempfile
from pathlib import Path
from src import utils

role = '{{ cookiecutter.sagemaker_role }}'


if __name__ == '__main__':

    with tempfile.TemporaryDirectory() as tmpdir:

        entry_point = 'remote_main.py'
        utils.copy_source_dir(utils.get_source_root_dir(),
                              tmpdir,
                              entry_point)

        runner = SKLearn(entry_point=entry_point,
                         source_dir=tmpdir,
                         role=role,
                         py_version='py3',
                         framework_version='0.23-1',
                         train_instance_type='ml.m4.xlarge',
                         hyperparameters={'Hello': 'World'},
                         base_job_name='demo',
                         tags=[{'Key': 'User', 'Value': utils.get_running_user()}],
                         metric_definitions=[{'Name': 'Test error', 'Regex': 'Test error ([0-9.]*)'},
                                             {'Name': 'Train error', 'Regex': 'Train error ([0-9.]*)'}]
                         )

        runner.fit(wait=True)