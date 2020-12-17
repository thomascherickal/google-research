# coding=utf-8
# Copyright 2020 The Google Research Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Utilities to run model training and evaluation."""

from deep_representation_one_class.contrastive import Contrastive
from deep_representation_one_class.unsup_embed import UnsupEmbed


def get_trainer(hparams):
  """Get trainer."""
  if hparams.method.lower() == 'unsupembed':
    trainer = UnsupEmbed(hparams)
  elif hparams.method.lower() == 'contrastive':
    trainer = Contrastive(hparams)

  return trainer
