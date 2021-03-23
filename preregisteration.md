# Working title: Test-retest reliability of the correlation between fMRI functional connectivity and physiology signal

Author: [Hao-Ting Wang](https://orcid.org/0000-0003-4078-2038)

Using [Secondary Data Preregistration](https://osf.io/x4gzt/).
The original design was intended for comfirmatory analysis.
The present analysis is exploratory.
Thus the author ignored certain sections or described alternative procedures.

## Study information

### Research Questions
<!-- List each research question included in this study.

When specifying your research questions, it is good practice to use only two new concepts per research question. For example, split up your questions into a simple format: “Does X lead to Y?” and “Is the relationship between X and Y moderated by Z?”. By splitting up the research questions here, you can more easily describe the statistical test for each research question later. -->
There's a standing debate of the impact of physiology singal on fMRI data.
In denoising literature, various methods has be developed to remove physiology based noise ([Glover et al. 2000]).
Although BOLD signal is, theoratically, heavily confounded by physiology signals, researchers still found functional relevance of physiology signal after removing relevant confunds.
Literature in dynamic resting state fMRI analysis has shown that physiology data is highly relevant to the default mode network after accounting for physiology related noise. ([Chang et al. 2009])
Acativity in bilarteral insula correlated with the interaction of high-frequency continuous heart rate variability and emotion-arrosing audio inputs in movie watching paradign ([Nguyen et al., 2015]) as well as resting state ([Kassinopoulos et al., 2019]).
A study simulating BOLD from physiology data has recovered networks similar to canonical resting state networks found through clustering functional connectivity data ([Chen et al., 2020]).
From the converging evidence above, we designed this analyisis to understand the relevance of physiology signal in resting state functional connectivity and explore the individual differences of its cognitive and psychiatric relevance.
- RQ1 - Understand the relevance of physiology signal in fMRI resting state functional connectivity.
- RQ2 - Assess the test-retest reliablilty of the impact of physiology data on functional connectivity.

### Hypotheses
<!-- For each of the research questions listed in the previous section, provide one or more specific and testable hypothesis. Please make clear whether the hypotheses are directional (e.g., A > B) or non-directional (e.g., A ≠ B). If directional, state the direction. You may also provide a rationale for each hypothesis. -->
The current study is primarily exploratory.
Based on past literature, we provide several speculations.
Overall:
H1, H2(1) = We found reliable functional connectivity based measure related to physiology recording of the same scan.
BOLD signal is highly relevant to heart rate and resperation, thus H1, H2(0) = it is possible that no reliable assocaition between physiology and fMRI functional connectivity.

## Data description

### Datasets Used
<!-- Name and briefly describe the dataset(s), and if applicable, the subsets of the data you plan to use.

Useful information to include here is the type of data (e.g., cross-sectional or longitudinal), the general content of the questions, and some details about the respondents. In the case of longitudinal data, information about the survey’s waves is useful as well. Mention the most relevant information so that readers do not have to search for the information themselves.
 -->
We use _enhanced NKI-Rockland dataset ([Nooner et al, 2012]) Test Retest Visits - Child Longitudinal Study specific visit - only MRI procedure_.
The enhanced NKI dataset provides restaing state fMRI scans and physiological recording using pulse oximeter and resperatory volume.
The test-retest sample (N = 209) is a subset of longtitudinal children data.
Thirty days after a full appointment, subjects were invited back to the lab and complete the retest of MRI session.
The dataset also provide rich phenotype assessments ranging from psychiatric conditions, cognitive performance, to physical performance.


### Data availability
<!-- Specify the degree to which the datasets are open or publicly available. -->
- [x] The dataset is publicly available.
- [x] The dataset is available through protected access.
- [ ] The dataset is not publicly available.

### Data Access
<!-- If there are any restrictions to accessing the dataset, please describe this here. -->
The neuro imaging data is fully availble on [FCP-INDI Amazon Web Servece S3 bucket](s3://fcp-indi/data/Projects/RocklandSample/RawDataBIDSLatest/).
The availibe information includes MRI data, physiological data obtained during scanning (cardiac and respiratory) and only basic phenotypic information (age, sex, handedness),
The phenotype data is restricted to applicants that completes a [data usage agreement](http://fcon_1000.projects.nitrc.org/indi/enhanced/phenotypicdata.html).

### Data Identifiers
<!-- Please provide a URL, DOI, or other persistent, unique identifier of the dataset. -->
Publication: https://doi.org/10.3389/fnins.2012.00152
Official website: http://fcon_1000.projects.nitrc.org/indi/enhanced/index.html

### Access Date
<!-- Specify the download or data access date. If the data were accessed multiple times by different team members, specify the download date for that data that will be used in the statistical analysis. -->
Physiology and fMRI data: 2021-03-20
Phenotype data: 2021-03-20

### Data Collection Procedures
<!-- If the data collection procedure is well documented, provide a link to that information. If the data collection procedure is not well documented, describe, to the best of your ability, how data were collected. Describe the representativeness of the sample and any possible biases stemming from the data collection. -->
Plese find details in [Nooner et al, 2012] and on their [official website](http://fcon_1000.projects.nitrc.org/indi/enhanced/studies.html).

### Codebook
<!-- Some studies offer codebooks to describe their data. If such a codebook is publicly available, link, cite, or upload the document. If not, provide other available documentation. Also provide guidance on what parts of the codebook or other documentation are most relevant. -->
[Access code book on their official website.](http://fcon_1000.projects.nitrc.org/indi/enhanced/assessments/NKI_RS_CODEBOOK.csv)

## Variables

### Manipulated Variables
<!-- If you are going to use any manipulated variables from the study variables, identify them here. Describe the variables and the levels or treatment arms of each variable. Note that this is not applicable for observational studies and meta-analyses. If you are collapsing groups across variables this should be explicitly stated, including the relevant formula. If your further analysis is contingent on a manipulation check, describe your decisions rules here. -->
N/A


### Measured Variables
<!-- Describe both outcome measures as well as predictors and covariates and label them accordingly. If you are using a scale or an index, state the construct the scale/index represents, which items the scale/index will consist of, and how these items will be aggregated. When the aggregation is based on exploratory factor analysis (EFA) or confirmatory factor analysis (CFA), also specify the relevant details (EFA: rotation, how the number of factors will be determined, how best fit will be selected, CFA: how loadings will be specified, how fit will be assessed, which residuals variance terms will be correlated). If you are using any categorical variables, state how you will code them in the statistical analyses. -->
The primary measure of interest is physology and fMRI.
We selected a subeset of the sample according to the following criteria:
* MPRAGE T1w scans collected in both sessions
* 9 minutes resting-state scan TR = 645 ms
* Physiology recording (cardiac and respiratory) during the resting state scan (sampling frequency: 62.5 hz)

After the above filtering, 189 out of 209 subejcts are selected.
Sample basic property:
* N = 189 (female N = 86)
* Age M = 12.25, SD = 3.02, range 6.64 - 20.37

We will use the phenotype assessment in the exploratory analysis.
A total of 97 cognitive assessments are availibe for the test-retest sample, but not all assessment were completed by the sample.
The analysis will be exploratory, thus we did not select assessments.


### Unit of Analysis
<!-- Which units of analysis (respondents, cases, etc.) will be included or excluded in your study? Taking these inclusion and exclusion criteria into account, indicate the expected sample size of the data you’ll be using for your statistical analyses. If you have a research question about a certain group you may need to exclude participants based on one or more characteristics. Be very specific when describing these characteristics so that readers will be able to redo your moves easily. -->
N/A

### Missing Data
<!-- What do you know about missing data in the dataset (i.e., overall missingness rate, information about differential dropout)? How will you deal with incomplete or missing data? Provide descriptive information, if available, on the amount of missing data for each variable you will use in the statistical analyses. Based on this information, provide a new expected sample size.  -->
The main measures of interests includes no missing data.
For phenotype data, we will explore assessments with at leat 60% (114 subjects) of the data present.
Excluding file logging administrative details or demographic information (`MRI`, `mri_log_sheet`, `blood_collection`, `age`, `dem*`, `Track`), the filter leaves us 47 assessments for the exploratory analysis.
Phenotype missing data will be imputed with either most frequent occurence or variable mean, depending on if data is categorical(frequent occurence), ordinal(frequent occurence), or scale (mean).

### Statistical Outliers
<!-- How will you define what a statistical outlier is in your data and what will you do when you encounter them? If you plan to remove outliers, provide a new expected sample size. If you expect to remove many outliers or if you are unsure about your outlier handling strategy, it is good practice to preregister analyses including and excluding outliers. Note that this will be the definitive expected sample size for your study and you will use this number to do any power analyses. -->
We will use motion as the outlier detection criteria for the imaging data.
Participants with less than 4.5 minutes of usable fMRI data ( > 450 high motion volumes) will be excluded from analysis.
Phenotype outlier will be defined as data point with a z-score above 3.
Outlier will be imputed with the same strategy as missing data.

### Sampling Weights
<!-- Are there sampling weights available with this dataset? If so, are you using them or are you using your own sampling weights? Sampling weights can be useful in secondary data analysis because the sample may not be entirely representative of the population you are interested in. -->
N/A

## Knowledge of data

### Prior Publication/Dissemination
<!-- List the publications, working papers, and conference presentations you have worked on that are based on the dataset you will use. For each work, list the variables you analyzed, but limit yourself to variables that are relevant to the proposed analysis. If the dataset is longitudinal, also state which wave of the dataset you analyzed. Specify the previous works for each co-author separately.

Listing previous works based on the data also helps to prevent a common practice identified by the American Psychological Association (2019) as unethical: the so-called “least publishable unit” practice (also known as “salami-slicing”), in which researchers publish multiple papers on closely related variables from the same dataset. -->
The author has published a study using the cross section resting state fMRI data (TR=2.5), MRI questionnaire (MRI-Q) and cognitive domain accessments ([Wang et. al., 2018]).
The current study uses different MRI measures and has excluded MRI-Q as more then 40% of the selected sample did not complete this key assessment.

### Prior Knowledge
<!-- What prior knowledge do you have about the dataset that may be relevant for the proposed analysis? Your prior knowledge could stem from working with the data first-hand, from reading previously published research, or from codebooks. Provide prior knowledge for every author separately.

Indirect knowledge about the hypothesized association does not preclude a confirmatory analysis but should be transparently reported in this section. However, direct knowledge about the association between the variables in your hypothesis may indicate that you are unable to make unbiased analytic decisions to test this hypothesis. -->
The author has not access the physiological data in this dataset, thus they have no prior knowledge on this measure.

## Analyses

### Statistical Models
<!-- For each hypothesis, describe the statistical model you will use to test the hypothesis. Include the type of model (e.g., ANOVA, multiple regression, SEM) and the specification of the model. Specify any interactions and post-hoc analyses and remember that any test not included here must be labeled as an exploratory test in the final paper. -->
#### fMRI data preprocessing
The data will be prerpoccessed with `fMRIprep v20.2.1`.
As suggested by previous literature ([Noble et al., 2019]), we used the `--longitudinal` flag to compute an average anatomical template for both sessions.
The preprocessed data is registered to the common standard `MNI152NLin2009cAsym` 2mm space.
See [`bin/fmriprep.sh`](bin/fmriprep.sh) for the cluster job submission file.

#### fMRI data denoising
We employ the denoising strategy detailed in ([Chen et al., 2020]) 2.2.2. with RETROICOR ([Glover et al. 2000]) calculated from physiology recording, six motion parameters and high-pass filtering.
The motion-related and high-pass filtering parameters are generated by fMRIprep and implemented with python library `load_confound`.
RETROICOR parameter will be created as closely as possible to the implementation in [Chen et al., 2020].

#### Physiological response functions
For the physiological response relevant to the functional connectivity analysis, we adopt strategy introduced by [Kassinopoulos et al., 2019].
The original MATLAB implementation can be found [here](https://github.com/mkassinopoulos/PRF_estimation).
<!---still need to read and research--->

#### Functional connectivity
We will first reproduce the general linear model detailed in [Kassinopoulos et al., 2019] to understand the generate the basic activation related to the physiological response functions.

The next step is to explore edge-based connectivity measures and find edges that are most relevant to the physiological response function.
We will use the [Schaefer2018 1000](https://github.com/ThomasYeoLab/CBIG/blob/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal/Parcellations/MNI/Schaefer2018_1000Parcels_7Networks_order_FSLMNI152_2mm.nii.gz) for cortical region parcels and [Tian S4 for subcortical parcels](https://github.com/yetianmed/subcortex/tree/master/Group-Parcellation/3T/Subcortex-Only).
For each ROI, we calculate an interaction term of signal and the physiological data, and then correlated this interaction with the remaining raw signal extracted from ROIs.
This step will result in an asymetric functional connectiviy matrix for each subject.
We will also compute a group lebel the difussion embedding map of this assymetrical connectivity for exploration purpose.

### Effect Size
<!-- If applicable, specify a predicted effect size or a minimum effect size of interest for all the effects tested in your statistical analyses. -->
Due to the multivariate nature of the analysis, the only possible effect size estimation strategy will be through simulation.
This is extremely difficult for neuroimaging exploratory study.
However, the author will use non-parametric permutation tests to resolve any significant testing and multiple comparison related issue.

### Statistical Power
<!-- Present the statistical power available to detect the predicted effect size or the smallest effect size of interest. Use the sample size after updating for missing data and outliers. -->
Due to the multivariate nature of the analysis, statistical power estimation strategy will be through simulation.
This is extremely difficult for neuroimaging exploratory study.
However, the author will use non-parametric permutation tests to resolve any significant testing and multiple comparison related issue.

### Inference Criteria
<!-- What criteria will you use to make inferences? Describe the information you will use (e.g. specify the p-values, effect sizes, confidence intervals, Bayes factors, specific model fit indices), as well as cut-off criteria, where appropriate. Will you be using one-or two-tailed tests for each of your analyses? If you are comparing multiple conditions or testing multiple hypotheses, will you account for this, and if so, how? -->

### Assumption Violation/Model Non-Convergence
<!-- What will you do should your data violate assumptions, your model not converge, or some other analytic problem arises? -->

### Reliability and Robustness Testing
<!-- Provide a series of decisions or tests about evaluating the strength, reliability, or robustness of your finding. This may include within-study replication attempts, additional covariates, cross-validation, applying weights, selectively applying constraints in an SEM context (e.g., comparing model fit statistics), overfitting adjustment techniques used, or some other simulation/sampling/bootstrapping method. -->
As the main aim of the analysis is to understand test-retest reliablity, we adopt measures described in the past literature. For both univariate and multivariate test-retest reliability measure, we will use interclass correlation coefficient (ICC), see: [Noble et al., 2020]
<!---still need to read and research--->


### Exploratory Analysis
<!-- If you plan to explore your dataset to look for unexpected differences or relationships, describe those tests here. If reported, add them to the final paper under a heading that clearly differentiates this exploratory part of your study from the confirmatory part. -->
If the functional connectivity-physiology interaction term was found stable, we intend to do two exploratory analysis using the two connectome derived feature.
1. Network based edges association with individula difference in phenotype data
2. connectivity-physiology interaction gradient score and phenotype data

Due to the high volumen of avalible assesments, we will use canoncial correlation analysis based method for data exploration.

<!-- Reference -->
[Nguyen et al., 2015]: https://doi.org/10.1016/j.neuroimage.2015.08.078
[Glover et al. 2000]: https://doi.org/10.1002/1522-2594(200007)44:1<162::AID-MRM23>3.0.CO;2-E
[Chang et al. 2009]: https://doi.org/10.1016/j.neuroimage.2008.09.029
[Chen et al., 2020]: https://doi.org/10.1016/j.neuroimage.2020.116707
[Kassinopoulos et al., 2019]: https://doi.org/10.1016/j.neuroimage.2019.116150
[Nooner et al, 2012]: https://doi.org/10.3389/fnins.2012.00152
[Wang et al., 2018]:https://doi.org/10.1016/j.neuroimage.2018.04.064
[Noble et al., 2019]: https://doi.org/10.1016/j.neuroimage.2019.116157
[Noble et al., 2020]: https://academic.oup.com/cercor/article/27/11/5415/4139668#113551820
[Hong et al., 2020]: https://doi.org/10.1016/j.neuroimage.2020.117322