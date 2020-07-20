import argparse
import json
import os

from src.models.amazing_model import run_model


def parse_args():
    global args
    parser = argparse.ArgumentParser()
    parser.add_argument('--train-data-dir', type=str, default=os.environ.get('SM_CHANNEL_TRAINING'))
    parser.add_argument('--output-data-dir', type=str, default=os.environ.get('SM_OUTPUT_DATA_DIR'))
    parser.add_argument('--training-env', type=str, default=os.environ.get('SM_TRAINING_ENV'))
    args, _ = parser.parse_known_args()


if __name__ == '__main__':
    parse_args()

    hyperparameters = json.loads(args.training_env)['hyperparameters']

    run_model(hyperparameters)