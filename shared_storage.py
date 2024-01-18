import copy
import pickle

import ray
import torch


@ray.remote
class SharedStorage:
    """
    Class which run in a dedicated thread to store the network weights and some information.
    """

    def __init__(self, checkpoint, config):
        self.config = config
        self.current_checkpoint = copy.deepcopy(checkpoint)

    def save_checkpoint(self, path=None, replay_buffer=None):
        if not path:
            path = self.config.results_path / "model.checkpoint"
            self.config.results_path.mkdir(parents=True, exist_ok=True)
        torch.save(self.current_checkpoint, path)
        if not replay_buffer:
            return
        path = self.config.results_path / "replay_buffer.pkl"
        print(f"\n\nPersisting replay buffer games to disk at {path}")
        info = self.get_info(["num_played_games", "num_played_steps", "num_reanalysed_games"])
        pickle.dump(
            {
                "buffer": replay_buffer,
                "num_played_games": info["num_played_games"],
                "num_played_steps": info["num_played_steps"],
                "num_reanalysed_games": info["num_reanalysed_games"],
            },
            open(path, "wb"),
        )


    def get_checkpoint(self):
        return copy.deepcopy(self.current_checkpoint)

    def get_info(self, keys):
        if isinstance(keys, str):
            return self.current_checkpoint[keys]
        elif isinstance(keys, list):
            return {key: self.current_checkpoint[key] for key in keys}
        else:
            raise TypeError

    def set_info(self, keys, values=None):
        if isinstance(keys, str) and values is not None:
            self.current_checkpoint[keys] = values
        elif isinstance(keys, dict):
            self.current_checkpoint.update(keys)
        else:
            raise TypeError
