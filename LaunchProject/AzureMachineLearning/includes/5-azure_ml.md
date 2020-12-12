# Azure Machine Learning

For programmers, one great feature of Azure Machine Learning is that you can use it completely from Visual Studio Code. This makes it an efficient means of adding AI and ML to projects directly from the programming environment.

## Import Python Libraries and Create AzureML Resources

To start, import some initial libraries. Azureml.core is the AzureML SDK and is essential for the integration with Azure ML from VS Code. The scikit-learn and logging libraries will also help with the following steps. You can also print out the version of azureml.core to ensure that you are working with the most recent version.

```python
import azureml.core
import sklearn
import logging

print('AzureML SDK Version:', azureml.core.VERSION)
```

```output
AzureML SDK Version: 1.18.0
```

You will also need to set up workspace and experiment objects for Azure ML. The workspace is the fundamental resource for machine learning in Azure Machine Learning; you use a workspace to experiment, train, and deploy machine learning models. The experiment is your container of trials that represent multiple runs of the model that you develop in the workspace.

```python
from azureml.core import Workspace, Experiment

ws = Workspace.from_config()

experiment_name = 'nasa_data_exploration'

experiment = Experiment(ws, experiment_name)
```

Beyond the workspace and experiment, you will also need to create an Azure ML compute cluster, provision it with VMs, and associate it with your workspace object. Also, set this run in VS Code until it is complete so that you don't have to go to the Azure portal to check on its progress (or guess when the configuration is complete).

```python
from azureml.core.compute import AmlCompute
from azureml.core.compute import ComputeTarget

amlcompute_cluster_name = 'cpu-cluster'

provisioning_config = AmlCompute.provisioning_configuration(vm_size='STANDARD_D2_V2', max_nodes=4)

compute_target = ComputeTarget.create(ws, amlcompute_cluster_name, provisioning_config)

compute_target.wait_for_completion(show_output=True, min_node_count=None, timeout_in_minutes=20)
```

```output
Succeeded
AmlCompute wait for completion finished

Minimum number of nodes requested have been provisioned
```

## Upload Data to Azure

With the entire Azure ML workspace now set up, it is time to upload the dataset. Do this using the `get_default_datastore()` method for your workspace object. This will create a datastore object that you can in turn use to upload the data for your experiment via its `upload_files()` method. The relevant parameters for this method are:
* **`files`**: the list of file paths to upload to AzureML.
* **`target_path`**: the location to store the uploaded files; set to `'dataset/'`.
* **`overwrite`**: weather to overwrite files with the same name at the target location; set to `True`.
* **`show_progress`**: weather to show upload progress in Visual Studio Code; set to `True`.

We only one delayed launch in the dataset, so performing a classical training/test data split would not be appropriate. Instead, you will train the model on the entire dataset and then upload a set of synthasized data for testing (so you will need to upload that CSV file to AzureML as well).

```python
datastore = ws.get_default_datastore()
datastore.upload_files(files=['prepped_launch_data_raw.csv', 'test_data_full.csv'], target_path='dataset/', overwrite=True, show_progress=True)
```

```output
Uploading an estimated of 2 files
Uploading prepped_launch_data_raw.csv
Uploaded prepped_launch_data_raw.csv, 1 files out of an estimated total of 2
Uploading test_data_full.csv
Uploaded test_data_full.csv, 2 files out of an estimated total of 2
Uploaded 2 files
$AZUREML_DATAREFERENCE_edd7a136911249e4a505981b8d7c09c4
```

## Train the Model

Now it's time to train the dataset. To designate the training dataset and the target column for classification, use the `Dataset` from the `azureml.core` library. You can also display the first five rows of the training data set (basically as you would with a DataFrame).

```python
from azureml.core import Dataset

target_column_name = 'Launched'

train = Dataset.Tabular.from_delimited_files(path=[(datastore, 'dataset/prepped_launch_data_raw.csv')])
train.take(5).to_pandas_dataframe().reset_index(drop=True)
```

**output**

| | Name | Date | Time | Launched | Temp	Percipitation | Wind Speed | Visibility | Day Length | Condition |
|---|---|---|---|---|---|---|---|---|---|
| 0 | Pioneer 3 | 2058-12-06 | 1:45 | True | 62.00 | 0.00 | 11.00 | 10 | 10:25 | Cloudy |
| 1 | Pioneer 4 | 2059-03-03 | 13:10 | True | 78.00 | 0.00 | 12.00 | 7 | 11:38 | Cloudy |
| 2 | Ranger 1 | 2061-08-23 | 11:04 | True | 90.00 | 0.00 | 9.00 | 10 | 12:56 | Partly Cloudy |
| 3 | Ranger 2 | 2061-11-18 | 9:09 | True | 54.00 | 0.00 | 6.00 | 15 | 10:41 | Fair |
| 4 | Ranger 3 | 2062-01-26 | 21:30 | True | 53.00 | 0.00 | 17.00 | 10 | 10:45 | Fair |

You designate the test data in similar fashion.

```python
test = Dataset.Tabular.from_delimited_files(path=[(datastore, 'dataset/test_data_full.csv')])
test.take(5).to_pandas_dataframe().reset_index(drop=True)
```

**output**

| | Name | Date | Time | Temp | Percipitation | Wind Speed | Visibility | Day Length | Cloudy | Fair | Heavy T-Storm | Partly Cloudy | Rain | Launched |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | Test 1 | 338 | 1203 | 63 | 0.00 | 72 | 10 | 644 | 1 | 0 | 0 | 0 | 0 | 0 |
| 1 | Test 2 | 75 | 1061 | 79 | 0.00 | 4 | 1 | 702 | 1 | 0 | 0 | 0 | 0 | 1 |
| 2 | Test 3 | 154 | 879 | 83 | 0.28 | 6 | 15 | 801 | 0 | 0 | 0 | 0 | 1 | 1 |
| 3 | Test 4 | 155 | 781 | 69 | 16.00 | 6 | 15 802 | 0 | 0 | 1 | 0 | 0 | 0 |
| 4 | Test 5 | 140 | 993 | 78 | 0.00 | 25 | 10 | 778 | 0 | 1 | 0 | 0 | 0 | 1 |

You will also need to tell AzureML which metrics to optimize for in training the model. While want to make predictions about launch delays, we are not really extrapolating continuous data about future trends from our data, which is the hallmark of classical predictive ML. Instead, we are merely checking to see if a launch is likely to be delayed based on available data, which is a binary classification ML task. To view the list of available metrics, import and use the `get_primary_metrics` function for `'classification'`.

```python
from azureml.train.automl.utilities import get_primary_metrics

get_primary_metrics('classification')
```

```output
['precision_score_weighted',
 'AUC_weighted',
 'average_precision_score_weighted',
 'norm_macro_recall',
 'accuracy']
```

In reality, NASA has to schedule launches far in advance. Just getting a rocket on the launch pad and fueling it is an expensive affair, so scheduling a launch and having to ultimately delay it is far less preferable than foregoing possible launch days. In short, we are far more worried about false positives (the model telling decision-makers that things look good for a launch when it turns out to be a delay) than we are about false negatives (the model erroneously reporting that conditions on a given day will likely cause a delay when in fact they wouldn't). Because of this reality, focus Azure ML on precision for this model.

The AutoMLConfig class represents configuration for submitting an automated ML experiment in Azure Machine Learning. It has a lot of parameters; here are the ones to use here:
* **task**: the type of task to run; set to `'classification'`.
* **primary_metric**: the metric that Automated Machine Learning will optimize for model selection; set to `'precision_score_weighted'`.
* **experiment_timeout_minutes**: maximum amount of time in hours that all iterations combined can take before the experiment terminates; set to `30`.
* **training_data**: the training data to be used within the experiment; set to `'train'`.
* **label_column_name**: the name of the label column; set to `'target_column_name'`.
* **compute_target**: the Azure Machine Learning compute target to run the Automated Machine Learning experiment on; set to `'compute_target'`.
* **enable_early_stopping**: whether to enable early termination if the score is not improving in the short term; set to `'True'`.
* **n_cross_validations**: how many cross validations to perform when user validation data is not specified; set to `5`.
* **max_concurrent_iterations**: represents the maximum number of iterations that would be executed in parallel; set to `4`.
* **max_cores_per_iteration**: the maximum number of threads to use for a given training iteration; set to `-1`.
* **verbosity**: the verbosity level for writing to the log file; set to `'logging.INFO'`.

```python
from azureml.train.automl import AutoMLConfig

automl_config = AutoMLConfig(task='classification',
                             primary_metric='precision_score_weighted',
                             experiment_timeout_minutes=30,
                             training_data=train,
                             label_column_name=target_column_name,
                             compute_target=compute_target,
                             enable_early_stopping=True,
                             n_cross_validations=5,
                             max_concurrent_iterations=4,
                             max_cores_per_iteration=-1,
                             verbosity=logging.INFO)
```

Now it is time to run the experiment remotely using the `submit` method of your experiment object. Pass to `submit` the `automl_config` object you just created; set the `show_output` parameter to `False` (we will look at the details after the experiment runs) and view the object.

```python
remote_run = experiment.submit(automl_config, show_output=False)
remote_run
```

```output
Running on remote.
Experiment	Id	Type	Status	Details Page	Docs Page
nasa_data_exploration	AutoML_e7f148b1-2375-476e-a6df-3d0dab303fd5	automl	NotStarted	[Link to Azure Machine Learning studio]	[Link to Documentation](https://docs.microsoft.com/en-us/python/api/overview/azure/ml/?view=azure-ml-py)
```

(Note that `Link to Azure Machine Learning studio` will point to your own Azure Machine Learning subscription when you run this code.)

Now use the `wait_for_completion()` method to actually run the experiment in Azure Machine Learning. (Note that a large chunk of the output is redacted below for brevity.)

```python
remote_run.wait_for_completion()
```

```output
{'runId': 'AutoML_e7f148b1-2375-476e-a6df-3d0dab303fd5',
 'target': 'cpu-cluster',
 'status': 'Completed',
 'startTimeUtc': '2020-11-21T00:09:04.007501Z',
 'endTimeUtc': '2020-11-21T00:34:06.487894Z',
 'properties': {'num_iterations': '1000',
  'training_type': 'TrainFull',
  'acquisition_function': 'EI',
  'primary_metric': 'precision_score_weighted',
  'train_split': '0',
  'acquisition_parameter': '0',
  'num_cross_validation': '5',
  'target': 'cpu-cluster',
  'AMLSettingsJsonString': 
  ⋮
  'EnableSubsampling': None,
  'runTemplate': 'AutoML',
  'azureml.runsource': 'automl',
  'display_task_type': 'classification',
  'dependencies_versions': '{"azureml-train": "1.18.0", "azureml-train-restclients-hyperdrive": "1.18.0", "azureml-train-core": "1.18.0", "azureml-train-automl": "1.18.0", "azureml-train-automl-runtime": "1.18.0.post1", "azureml-train-automl-client": "1.18.0", "azureml-telemetry": "1.18.0", "azureml-sdk": "1.18.0", "azureml-pipeline": "1.18.0", "azureml-pipeline-steps": "1.18.0", "azureml-pipeline-core": "1.18.0", "azureml-model-management-sdk": "1.0.1b6.post1", "azureml-interpret": "1.18.0", "azureml-explain-model": "1.18.0", "azureml-defaults": "1.18.0", "azureml-dataset-runtime": "1.18.0", "azureml-dataprep": "2.4.2", "azureml-dataprep-rslex": "1.2.2", "azureml-dataprep-native": "24.0.0", "azureml-core": "1.18.0.post1", "azureml-automl-runtime": "1.18.0", "azureml-automl-core": "1.18.0"}',
  '_aml_system_scenario_identification': 'Remote.Parent',
  'ClientType': 'SDK',
  'environment_cpu_name': 'AzureML-AutoML',
  'environment_cpu_version': '44',
  'environment_gpu_name': 'AzureML-AutoML-GPU',
  'environment_gpu_version': '32',
  'root_attribution': 'automl',
  'attribution': 'AutoML',
  'Orchestrator': 'AutoML',
  'CancelUri': 'https://westus2.experiments.azureml.net/jasmine/v1.0/subscriptions/c819623b-1397-47f6-aa43-4635420ecead/resourceGroups/DevIntroDS_RG/providers/Microsoft.MachineLearningServices/workspaces/DevIntroDS/experimentids/1eafce1b-a485-43ea-8fee-7bc64a006363/cancel/AutoML_e7f148b1-2375-476e-a6df-3d0dab303fd5',
  'ClientSdkVersion': '1.17.0',
  'snapshotId': '00000000-0000-0000-0000-000000000000',
  'SetupRunId': 'AutoML_e7f148b1-2375-476e-a6df-3d0dab303fd5_setup',
  'SetupRunContainerId': 'dcid.AutoML_e7f148b1-2375-476e-a6df-3d0dab303fd5_setup',
  'FeaturizationRunJsonPath': 'featurizer_container.json',
  'FeaturizationRunId': 'AutoML_e7f148b1-2375-476e-a6df-3d0dab303fd5_featurize',
  'ProblemInfoJsonString': '{"dataset_num_categorical": 0, "is_sparse": true, "subsampling": false, "dataset_classes": 2, "dataset_features": 18, "dataset_samples": 58, "single_frequency_class_detected": true}',
  'ModelExplainRunId': 'AutoML_e7f148b1-2375-476e-a6df-3d0dab303fd5_ModelExplain'},
 'inputDatasets': [{'dataset': {'id': 'da36f1f0-0192-472e-b360-4fff030b620e'}, 'consumptionDetails': {'type': 'RunInput', 'inputName': 'training_data', 'mechanism': 'Direct'}}],
 'outputDatasets': [],
 'logFiles': {}}
```

Note that Azure Machine Learning is going to perform several runs (the 5-fold cross-validation) of many algorithms to find the best model for this data, so this step could take anywhere from several minutes to an hour to conclude.

Once the run concludes, let's examine the model that Azure Machine Learning found to be the best performing on this data. The `get_output()` method produces two outputs and we are interested in `fitted_model`.

```python
best_run, fitted_model = remote_run.get_output()
fitted_model.steps
```

```output
[('datatransformer',
  DataTransformer(enable_dnn=None, enable_feature_sweeping=None,
                  feature_sweeping_config=None, feature_sweeping_timeout=None,
                  featurization_config=None, force_text_dnn=None,
                  is_cross_validation=None, is_onnx_compatible=None, logger=None,
                  observer=None, task=None, working_dir=None)),
 ('MaxAbsScaler', MaxAbsScaler(copy=True)),
 ('ExtraTreesClassifier',
  ExtraTreesClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                       criterion='entropy', max_depth=None, max_features=0.3,
                       max_leaf_nodes=None, max_samples=None,
                       min_impurity_decrease=0.0, min_impurity_split=None,
                       min_samples_leaf=0.01,
                       min_samples_split=0.056842105263157895,
                       min_weight_fraction_leaf=0.0, n_estimators=25, n_jobs=-1,
                       oob_score=True, random_state=None, verbose=0,
                       warm_start=False))]
```

This large tuple can be hard to read; if the classifier is unclear, try just looking at the third element of this tuple.

```python
fitted_model[2]
```

```output
ExtraTreesClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,
                     criterion='entropy', max_depth=None, max_features=0.3,
                     max_leaf_nodes=None, max_samples=None,
                     min_impurity_decrease=0.0, min_impurity_split=None,
                     min_samples_leaf=0.01,
                     min_samples_split=0.056842105263157895,
                     min_weight_fraction_leaf=0.0, n_estimators=25, n_jobs=-1,
                     oob_score=True, random_state=None, verbose=0,
                     warm_start=False)
```

The classifier that Azure Machine Learning settled on is Extra Trees. Extra Trees is like Random Forest: it builds multiple decision trees and splits nodes on those trees using random subsets of features. However, unlike Random Forest, Extra Trees sub-samples the data without replacement and splits nodes using random splits rather than the best splits. (The algorithm does this to improve predictive accuracy and control over-fitting.)

We can also see which features Azure Machine Learning ended up using to build the best-perfoming model through the `get_featurization_summary` method. (For convenience reading the output, place it in a DataFrame.)

```python
featurization_summary = fitted_model.named_steps['datatransformer'].get_featurization_summary()
pd.DataFrame.from_records(featurization_summary)
```

**output**

| | RawFeatureName | TypeDetected | Dropped | EngineeredFeatureCount | Transformations |
|--:|--:|--:|--:|--:|--:|
| 0 | Name | Hashes | Yes | 0 | [] |
| 1 | Time | Hashes | Yes | 0 | [] |
| 2 | Date | DateTime | No | 10 | \[ModeCatImputer-StringCast-DateTimeTransformer\] |
| 3 | Temp | Numeric | No | 1 | \[MeanImputer\] |
| 4 | Percipitation | Numeric | No | 1 | \[MeanImputer\] |
| 5 | Wind Speed | Numeric | No | 1 | \[MeanImputer\] |
| 6 | Visibility | Numeric | No | 1 | \[MeanImputer\] |
| 7 | Day Length | Ignore | Yes | 0 | [] |
| 8 | Condition | CategoricalHash | No | 4 | \[StringCast-HashOneHotEncoder\] |

## Test the Model

***Sarah, I'm afraid that I need help with this section.***