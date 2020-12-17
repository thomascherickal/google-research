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

#!/bin/bash
set -e
set -x

virtualenv -p python3 env
source env/bin/activate

pip install -r flax_models/cifar/requirements.txt
python -m flax_models.cifar.datasets.dataset_source_test
python -m flax_models.cifar.datasets.auto_augment_test
python -m flax_models.cifar.models.load_model_test
python -m flax_models.cifar.training_utils.flax_training_test
