import argparse
import os

def get_train_test_args():
    train_data = ','.join(os.listdir('datasets_augment/indomain_train'))

    parser = argparse.ArgumentParser()
    parser.add_argument('--batch-size', type=int, default=32)
    parser.add_argument('--num-epochs', type=int, default=5)
    parser.add_argument('--lr', type=float, default=3e-5)
    parser.add_argument('--num-visuals', type=int, default=10)
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--save-dir', type=str, default='save/')
    parser.add_argument('--train', action='store_true')
    parser.add_argument('--eval', action='store_true')
    parser.add_argument('--train-datasets', type=str, default=train_data)
    parser.add_argument('--run-name', type=str, default='multitask_distilbert')
    parser.add_argument('--recompute-features', action='store_true')
    parser.add_argument('--train-dir', type=str, default='datasets_augment/indomain_train')
    parser.add_argument('--val-dir', type=str, default='datasets_augment/indomain_val')
    parser.add_argument('--eval-dir', type=str, default='datasets/oodomain_val')
    parser.add_argument('--eval-datasets', type=str, default='race,duorc,relation_extraction')
    parser.add_argument('--do-train', action='store_true')
    parser.add_argument('--do-eval', action='store_true')
    parser.add_argument('--sub-file', type=str, default='')
    parser.add_argument('--visualize-predictions', action='store_true')
    parser.add_argument('--eval-every', type=int, default=10000)
    args = parser.parse_args()
    return args
