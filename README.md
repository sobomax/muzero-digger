![supported platforms](https://img.shields.io/badge/platform-Linux%20%7C%20Mac%20%7C%20Windows%20(soon)-929292)
![supported python versions](https://img.shields.io/badge/python-%3E%3D%203.6-306998)
![dependencies status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen)
[![style black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
![license MIT](https://img.shields.io/badge/licence-MIT-green)
[![discord badge](https://img.shields.io/badge/discord-join-6E60EF)](https://discord.gg/GB2vwsF)


# MuZero Digger

Adaptation of the "MuZero General" self-training pipeline to the game of Digger.

## Few improvements along the way:

* All critical actors are labeled with resources, so it's easier to put data where it makes sense.
* Self-play inference is now batched via a new actor, this reduces memory pressure and optimizes
  inference, allowing for a faster self-play with limited resorces.
* Replay buffer is saved along with the model snapshot.

## Training Setup

* Main node: 64GB RAM, Intel A770 GPU, 16GB VRAM
* Self-player #1: 32GB RAM, Intel A770 GPU, 16GB VRAM
* Self-player #2: 16GB RAM, Intel A770 GPU, 16GB VRAM

## Links

* [MuZero General](https://github.com/werner-duvaud/muzero-general/): for non-digger specific issue and bug reports
