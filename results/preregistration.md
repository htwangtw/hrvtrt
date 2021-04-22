# Working title: Test-retest reliability of the correlation between fMRI functional connectivity and heart rate variability

Authors:

- [Hao-Ting Wang](https://orcid.org/0000-0003-4078-2038)
- Name here

Using [Secondary Data Preregistration](https://osf.io/x4gzt/).
The original design was intended for confirmatory analysis.
The present analysis is exploratory.
Thus the author ignored certain sections or described alternative procedures.

## Study information

### Research Questions

<!-- List each research question included in this study.

When specifying your research questions, it is good practice to use only two new concepts per research question. For example, split up your questions into a simple format: “Does X lead to Y?” and “Is the relationship between X and Y moderated by Z?”. By splitting up the research questions here, you can more easily describe the statistical test for each research question later. -->
There's a long-standing debate of the impact of physiology signals on fMRI data.
In the denoising literature, various methods have been developed to remove physiology based noise ([Glover et al., 2000]).
Although BOLD signal is, theoretically, heavily confounded by physiology signals, researchers still found functional relevance of physiology signal after removing relevant confounds.
Literature in dynamic resting state fMRI analysis has shown that heart rate variability is highly relevant to the default mode network after accounting for heart beat and respiration related noise ([Chang et al., 2013]).
Activity in bilateral insula correlated with the interaction of high-frequency continuous heart rate variability and emotion-arousing audio inputs in movie watching paradigm ([Nguyen et al., 2015]) as well as resting state ([Kassinopoulos et al., 2019]).
A study simulating BOLD from physiology data has recovered networks similar to canonical resting state networks found through clustering functional connectivity data ([Chen et al., 2020]).
From the converging evidence above, we designed this analysis to understand the relevance of heart rate variability in resting state functional connectome and explore the individual differences of its cognitive and psychiatric relevance.

- RQ1 - Understand the relevance of heart rate variability in fMRI resting state functional connectome.
- RQ2 - Assess the test-retest reliability of the impact of physiology data on functional connectome.

### Hypotheses
<!-- For each of the research questions listed in the previous section, provide one or more specific and testable hypothesis. Please make clear whether the hypotheses are directional (e.g., A > B) or non-directional (e.g., A ≠ B). If directional, state the direction. You may also provide a rationale for each hypothesis. -->
This experiment is exploratory so we do not have a prediction as to the outcome of our analyses.
To test RQ1, we will determine whether fMRI resting state functional connectivity, using the data from session 1, is significantly correlated with heart-rate variability.
We will expand the analysis in ([Chang et al., 2013]) from single ROI (dACC and amygdala) to the full connectome.
We will also explore novel connectivity-based gradients to understand the impact of heart rate variability on the whole brain.

To test RQ2, we will compare any significant associations found in our tests above with the associations for the session 2 data.
In this way, we will be assessing test-retest reliability.

## Data description

### Datasets Used

<!-- Name and briefly describe the dataset(s), and if applicable, the subsets of the data you plan to use.

Useful information to include here is the type of data (e.g., cross-sectional or longitudinal), the general content of the questions, and some details about the respondents. In the case of longitudinal data, information about the survey’s waves is useful as well. Mention the most relevant information so that readers do not have to search for the information themselves.
 -->
We will use _the enhanced NKI-Rockland dataset ([Nooner et al, 2012]) Test Retest Visits - Child Longitudinal Study specific visit - only MRI procedure_.
The dataset is selected based on the availability of imaging and physiology modality, as well as the wide range of cognitive and psychological assessments.
The NKI data set includes both cross-section and longitudinal elements, making it a good candidate for feature discovery and test-retest analysis.
The enhanced NKI dataset includes resting state fMRI scans and physiological recordings during the same scan in the form of pulse oximetry and respiratory volume.
The physiological and neuroimaging data were collected concurrently.
The test-retest sample of the NKI dataset is our subset of interest.  This data subset comprises longitudinal data from 209 children.
Thirty days after a full appointment that assessed the full phenotype battery (see participant schedule), subjects were invited back to the lab and completed the retest of the MRI session. The dataset also provides rich phenotype assessments ranging from psychiatric conditions, cognitive performance, to physical performance.

### Data availability
<!-- Specify the degree to which the datasets are open or publicly available. -->
- [x] The dataset is publicly available.
- [x] The dataset is available through protected access.
- [ ] The dataset is not publicly available.

### Data Access
<!-- If there are any restrictions to accessing the dataset, please describe this here. -->
The neuroimaging data is fully available on [FCP-INDI Amazon Web Service S3 bucket](s3://fcp-indi/data/Projects/RocklandSample/RawDataBIDSLatest/).
The available information includes MRI data, physiological data obtained during scanning (cardiac and respiratory) and only basic phenotypic information (age, sex, handedness).
The phenotype data is restricted to applicants that completes a [data usage agreement](http://fcon_1000.projects.nitrc.org/indi/enhanced/phenotypicdata.html).

### Data Identifiers
<!-- Please provide a URL, DOI, or other persistent, unique identifier of the dataset. -->
- Publication: https://doi.org/10.3389/fnins.2012.00152
- Official website: http://fcon_1000.projects.nitrc.org/indi/enhanced/index.html

### Access Date
<!-- Specify the download or data access date. If the data were accessed multiple times by different team members, specify the download date for that data that will be used in the statistical analysis. -->
- Physiology and fMRI data: 2021-03-20
- Phenotype data: 2021-03-20

### Data Collection Procedures
<!-- If the data collection procedure is well documented, provide a link to that information. If the data collection procedure is not well documented, describe, to the best of your ability, how data were collected. Describe the representativeness of the sample and any possible biases stemming from the data collection. -->
Please find details in [Nooner et al, 2012] and on their [official website](http://fcon_1000.projects.nitrc.org/indi/enhanced/studies.html).

### Codebook
<!-- Some studies offer codebooks to describe their data. If such a codebook is publicly available, link, cite, or upload the document. If not, provide other available documentation. Also provide guidance on what parts of the codebook or other documentation are most relevant. -->
[Access code book on their official website.](http://fcon_1000.projects.nitrc.org/indi/enhanced/assessments/NKI_RS_CODEBOOK.csv)

## Variables

### Measured Variables
<!-- Describe both outcome measures as well as predictors and covariates and label them accordingly. If you are using a scale or an index, state the construct the scale/index represents, which items the scale/index will consist of, and how these items will be aggregated. When the aggregation is based on exploratory factor analysis (EFA) or confirmatory factor analysis (CFA), also specify the relevant details (EFA: rotation, how the number of factors will be determined, how best fit will be selected, CFA: how loadings will be specified, how fit will be assessed, which residuals variance terms will be correlated). If you are using any categorical variables, state how you will code them in the statistical analyses. -->
We will consider the following variables only:

- Demographics and basic information: age; gender; session.
- Physiology:
    1. continuous pulse-oximetry recordings, collected at the same time as the resting-state fMRI
    2. continuous respiratory volume recordings (units mm3), collected at the same time as the resting-state fMRI
- Neuroimaging: MPRAGE T1w scans collected in both sessions; 9 minutes of resting-state EPI scan TR = 645 ms

Within this dataset, our primary measures of interest are the physiological variables and the fMRI.

### Inclusion Criteria

We will select a subset of the test-retest sample according to the following criteria to ensure all subject can go under the same preprocessing pipeline:

- Participant had MPRAGE T1w scans collected in both sessions
- Participant has at least 9 minutes of resting-state data per session, collected with TR = 645 ms
- Participant has both pulse-oximetry and respiratory volume data collecting during the resting state scan, in both sessions, and collected at a sampling frequency of 62.5 hz

After the above filtering, 189 out of 209 subjects are selected. Sample basic property:

- N = 189 (female N = 86)
- Age M = 12.25, SD = 3.02, range 6.64 - 20.37

Further sample exclusion will be done after preprocessing.

## Knowledge of data

### Prior Publication/Dissemination

<!-- List the publications, working papers, and conference presentations you have worked on that are based on the dataset you will use. For each work, list the variables you analyzed, but limit yourself to variables that are relevant to the proposed analysis. If the dataset is longitudinal, also state which wave of the dataset you analyzed. Specify the previous works for each co-author separately.

Listing previous works based on the data also helps to prevent a common practice identified by the American Psychological Association (2019) as unethical: the so-called “least publishable unit” practice (also known as “salami-slicing”), in which researchers publish multiple papers on closely related variables from the same dataset. -->
The lead author has published a study using the cross section resting state fMRI data (TR=2.5), MRI questionnaire (MRI-Q) and cognitive domain assessments ([Wang et al., 2018]).
The current study uses different MRI measures and has excluded MRI-Q as more than 40% of the selected sample did not complete this key assessment.

### Prior Knowledge

<!-- What prior knowledge do you have about the dataset that may be relevant for the proposed analysis? Your prior knowledge could stem from working with the data first-hand, from reading previously published research, or from codebooks. Provide prior knowledge for every author separately.

Indirect knowledge about the hypothesized association does not preclude a confirmatory analysis but should be transparently reported in this section. However, direct knowledge about the association between the variables in your hypothesis may indicate that you are unable to make unbiased analytic decisions to test this hypothesis. -->
The author has not accessed the physiological data in this dataset, thus they have no prior knowledge on this measure.

## Analyses

Methods below will specify software packages and parameters used if stated; otherwise, analysis will be developed on test data before applying to real data.
All code and test data will be hosted on [github](https://github.com/htwangtw/physiogradient/).
Due to the exploratory nature, the detail of the analysis will be subject to change.
However the full development history will be traceable on the above github repository.

### Preprocessing

#### fMRI data

The data will be prerpoccessed with `fMRIprep v20.2.1`.
As suggested by previous literature ([Noble et al., 2019]), we used the `--longitudinal` flag to compute an average anatomical template for both sessions.
Other options are set to default.
The preprocessed data is registered to the common standard `MNI152NLin2009cAsym` 2mm volume metric space and the equivalent of surface space (HCP `fsLR` 91k grayordinate).
See [`bin/fmriprep.sh`](bin/fmriprep.sh) for the cluster job submission file.
The analysis will be performed on surface grayordinate output to focus on grey matter related activity and subcortical regions.

#### Physiology data

The preprocessing procedure will be developed using simulated test data before applying it to real dataset.
The project will use `neurokit2` for its support in both respiratory volume data and pulse oximetry data.
The respiratory volume data will be processed with method developed by [Khodadad1 et al., 2018].
For pulse oximetry data, we preprocess the signal with peak detection methods reported in [Elgendi et al., 2013].

#### Exclusion criteria

After fMRI data preprocessing, we will exclude subjects with high motion volumes assesed by framewise displacement above 0.5 mm in over 50% (450 volumes) of the timeseries.
The metrics calculated by `fMRIprep`.

Physiology data would be excluded if its deemed corrupted (no algorithm detectable peaks).

We will use the phenotype assessment in the exploratory analysis.
A total of 97 cognitive assessments are available for the test-retest sample, but not all assessments were completed by the sample.
We will explore phenotype assessments with at least 60% (114 subjects) of the data present.
Excluding file logging administrative details or demographic information (`MRI`, `mri_log_sheet`, `blood_collection`, `age`, `dem*`, `Track`), the filter leaves us 47 assessments for the exploratory analysis.
Phenotype missing data will be imputed with either most frequent occurrence or variable mean, depending on if data is categorical(frequent occurrence), ordinal(frequent occurrence), or scale (mean).
The analysis will be exploratory, thus we did not select assessments further.
Phenotype outliers will be defined as data points with a z-score above 3.
Outliers will be imputed with the same strategy as missing data.

#### Denoising parameters

We employ the denoising strategy detailed in ([Chen et al., 2020]) 2.2.2. with `RETROICOR` ([Glover et al., 2000]) calculated from physiology recording, scanner temporal drifts, and six motion parameters on minimally processed HCP data.
Corresponding to `fMRIprep`, the motion-related and scanner temporal drifts can be addressed with high-pass filtering and motion parameters generated by fMRIprep.
This is implemented with python library `load_confound method` `Para6`.
`RETROICOR` parameters will include measure up to the 2nd order as the implementation in [Chen et al., 2020].
The `RETROICOR` implementation is adapted from [Kassinopoulos et al., 2019] into Python. The original MATLAB implementation can be found [here](https://github.com/mkassinopoulos/PRF_estimation).

#### Parcellation of fMRI signal

We will use the [Schaefer2018 7 network 1000](https://github.com/ThomasYeoLab/CBIG/blob/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal/Parcellations/) for cortical region parcels and [Tian S4 for subcortical parcels](https://github.com/yetianmed/subcortex/tree/master/Group-Parcellation/3T/Subcortex-Only).
This results in connectomes of the size 1054 by 1054.

### Heart rate variability

We adopt an alternative approach from [Barbieri et al. 2005] that yields alternative definitions of heart rate and heart rate variability (HRV) with point-process analysis.
Point processes can be used as models for random events in time.
A point process can be described completely by the (random) time of occurrence of the events.
Common methods treat the R-R interval or heart rate series as continuous-valued signals, rather than model them to reflect the point-process structure and the stochastic nature of the underlying R-wave events.
[Barbieri et al. 2005] modeled heartbeat intervals as a history-dependent inverse Gaussian (HDIG) point process and derive from it an explicit probability density that yields alternative definitions of heart rate and heart rate variability.

The implementation of point process analysis of the original study is achieved by python library [pointprocess (v0.3, 3346078)](https://github.com/andreabonvini/pointprocess).
The MATLAB source code of [Barbieri et al., 2005] can be found [here](http://users.neurostat.mit.edu/barbieri/pphrv).

We will focus on with the following time-varying HRV measures derived from HDIG reported in [Napadow et al., 2013]:

- Standard deviation of heart rate (bpm)
- LF/HF

### Dynamic functional connectome
<!-- For each hypothesis, describe the statistical model you will use to test the hypothesis. Include the type of model (e.g., ANOVA, multiple regression, SEM) and the specification of the model. Specify any interactions and post-hoc analyses and remember that any test not included here must be labeled as an exploratory test in the final paper. -->
We will explore dynamic connectivity measures and find edges that are most relevant to heart rate variability.
We select atlas that’s available in fsLR-32k space and covers the whole brain.
We plan to explore the following connectivity based measures.
All measures will be computed for the two sessions respectively.

1. Continuous HRV in a simple GLM [Napadow et al., 2013]

2. Dynamic functional connectome [Chang et al., 2013]
    We will expand the analysis in ([Chang et al., 2013]) from single ROI (dACC and amygdala) to the full connectome.

3. ROI-HRV interaction
    We compute interaction terms of each ROI and HRV, and then correlate each interaction with the remaining ROI, resulting an asymmetrical connectome.

### Reliability and Robustness Testing
<!-- Provide a series of decisions or tests about evaluating the strength, reliability, or robustness of your finding. This may include within-study replication attempts, additional covariates, cross-validation, applying weights, selectively applying constraints in an SEM context (e.g., comparing model fit statistics), overfitting adjustment techniques used, or some other simulation/sampling/bootstrapping method. -->
As the main aim of the analysis is to understand test-retest reliability of the impact of HRV on connectome, we adopt measures described in the past literature.
We will use intraclass correlation coefficient (ICC), see: [Noble et al., 2020].
ICC can be interpreted as follows ([Cicchetti and Sparrow 1981]):

- <0.4 poor
- 0.4–0.59 fair
- 0.60–0.74 good
- \> 0.74 excellent

For dynamic functional connectome and ROI-HRV interaction, ICC will be calculated at edge-level.

### Effect Size
<!-- If applicable, specify a predicted effect size or a minimum effect size of interest for all the effects tested in your statistical analyses. -->
Due to the multivariate nature of the analysis, the only possible effect size estimation strategy will be through simulation.
This is extremely difficult for neuroimaging exploratory study.
However, the author will use non-parametric permutation tests to resolve any significant testing and multiple comparison related issues.

### Statistical Power
<!-- Present the statistical power available to detect the predicted effect size or the smallest effect size of interest. Use the sample size after updating for missing data and outliers. -->
Due to the multivariate nature of the analysis, statistical post hoc power estimation strategy will be through simulation.
This is extremely difficult for neuroimaging exploratory study.
However, the author will use non-parametric permutation tests to resolve any significant testing and multiple comparison related issues.

### Assumption Violation/Model Non-Convergence
<!-- What will you do should your data violate assumptions, your model not converge, or some other analytic problem arises? -->
The authors expect to cover all quantifiable details in the simulated test data through the process to ensure reproducibility and continuous integration of the analysis.
Due to the exploratory nature, the authors will simply accept the null-results and discuss the potential reasons in the report.

### Exploratory Analysis
<!-- If you plan to explore your dataset to look for unexpected differences or relationships, describe those tests here. If reported, add them to the final paper under a heading that clearly differentiates this exploratory part of your study from the confirmatory part. -->
We will also compute a group level the cortical diffusion embedding map of dynamic functional connectome and ROI-HRV interaction respectively to exploration the impact of physiology on whole brain gradient.
We will compare those to standard diffusion embedding map calculated with the original method in [Margulies et al., 2016].
As the two set of maps might have not spatial correspondence, we will not perform reliability tests on this measure.
Diffusion embedding map calculation is implemented by python library [BrainSpace](https://brainspace.readthedocs.io/en/latest/).

If the functional connectivity-HRV interaction term was found stable, we intend to do two exploratory analysis using the connectomes derived features.

1. Network based edges association with individual difference in phenotype data
2. connectivity-physiology interaction gradient score and phenotype data

Due to the high volume of available assessments, we will use canonical correlation analysis based methods for data exploration.

<!-- Reference -->
[Nguyen et al., 2015]: https://doi.org/10.1016/j.neuroimage.2015.08.078
[Glover et al., 2000]: https://doi.org/10.1002/1522-2594(200007)44:1<162::AID-MRM23>3.0.CO;2-E
[Chang et al., 2009]: https://doi.org/10.1016/j.neuroimage.2008.09.029
[Chang et al., 2013]: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3746190/
[Chen et al., 2020]: https://doi.org/10.1016/j.neuroimage.2020.116707
[Kassinopoulos et al., 2019]: https://doi.org/10.1016/j.neuroimage.2019.116150
[Nooner et al, 2012]: https://doi.org/10.3389/fnins.2012.00152
[Wang et al., 2018]:https://doi.org/10.1016/j.neuroimage.2018.04.064
[Noble et al., 2019]: https://doi.org/10.1016/j.neuroimage.2019.116157
[Noble et al., 2020]: https://academic.oup.com/cercor/article/27/11/5415/4139668#113551820
[Cicchetti and Sparrow 1981]: https://pubmed.ncbi.nlm.nih.gov/7315877/
[Elgendi et al., 2013]: https://doi.org/10.1371/journal.pone.0076585
[Khodadad1 et al., 2018]: https://doi.org/10.1088/1361-6579/aad7e6
[Margulies et al., 2016]: https://doi.org/10.1073/pnas.1608282113
[Barbieri et al., 2005]: https://doi.org/10.1152/ajpheart.00482.2003
[Napadow et al., 2013]: https://doi.org/10.1016/j.neuroimage.2008.04.238