# Analysis plan

Author: Hao-Ting Wang

There's a standing debate of the impact of physiology singal on fMRI data.
In denoising literature, various methods has be developed to remove physiology based noise.
Although BOLD signal is, theoratically, heavily confounded by physiology signals, researchers still found functional relevance of physiology signal after removing relevant confunds.
Acativity in bilarteral insula correlated with the interaction of high-frequency continuous heart rate variability and audio imputs in movie watching paradigmn.
Recent literature in resting state fMRI has shown that physiology data is highly relevant to the default mode network after accounting for physiology related noise.
A study simulating BOLD from physiology data has recovered networks similar to canonical resting state networks found through clustering functional connectivity data.
Studies using PET imaging methods has demostrated relevance of heart rate variablilty and task-related brain activity.
From the converging evidence above, we designed this analyisis to understand the relevance of physiology signal in resting state functional connectivity and explore the individual differences of its cognitive relevance.

## Dataset and sample
We selected Enhanced NKI-rockland sample test-retest resting state data. The selection criteria is as followed:
* Resting-state scan TR = 645 ms
* T1w scan in both sessions
* Physiology recording during the resting state scan
Sample basic property: N = 189 (female N = 86); Age M = 12.25, SD = 3.02 range 6.64 - 20.37
A total of 85 cognitive assessments are availibe for the test-retest sample, and not all assessment ,