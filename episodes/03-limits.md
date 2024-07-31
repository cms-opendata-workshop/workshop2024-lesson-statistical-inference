---
title: "Limits"
teaching: 10
exercises: 0
---

:::::::::: questions

- What are limits?
- What are expected and observed limits?
- How do we calculate limits?
- 
::::::::::

:::::::::: objectives

- Understand the concept of limits, expected limits, and observed limits.
- Familiarize with the steps of calculating limits.
- Familiarize with the concepts of hypothesis testing, test statistic, p-values and confidence level.

:::::::::::

## What are limits?

**Limits** are constraints placed on the parameters of a theoretical model based on the experimental data. They help determine the range within which new particles or interactions could exist.

**Observed limits:** These are limits derived directly from the experimental data. They represent the actual constraint on the parameter of interest based on the measurements taken during the experiment.

**Expected limits:** These are limits are based on simulated data assuming no new phenomena exist (i.e., that the null hypothesis is true). They provide a benchmark for comparing the observed limits to what would be expected if only known physics were at play.

## Calculating limits

The process of calculating limits typically involves the following steps:

1. **Define the statistical model and construct the likelihood** : 

2. **Perform Hypothesis Testing**:
   - **Null hypothesis (or background-only hypothesis) ($H_0$)**: This hypothesis assumes that there is no new physics, meaning the data can be fully explained by the standard model or another established theory.
   - **Alternative hypothesis or signal+background hypothesis ($H_1$)**: This hypothesis posits the presence of new physics, implying deviations from the predictions of the null hypothesis.
   - **Test statistic**: Calculate a test statistic, such as the profile likelihood ratio, which compares how well the data fits under both $H_0$ and $H_1$. The profile likelihood ratio is defined as:$$\lambda(\mu) = \frac{\mathcal{L}(\mu, \hat{\hat{\nu}})}{\mathcal{L}(\hat{\mu}, \hat{\nu})}$$
where $\mathcal{L}$ is the likelihood function, $\mu$ and $\nu$ represent the parameters of interest and nuisance parameters, $\hat{\mu}$ and $\hat{\nu}$ are the best-fit parameters, and $\hat{\hat{\nu}}$ is the conditional maximum likelihood estimator of the nuisance parameters given $\mu$.  Note that in the current LHC analyses, we use more complex test statistics such as the LHC-style test statistic.  However, despite the added complexity, the main idea is the same.  The test statistic is evaluated for observed data or pseudo-data 
   - **p-value**: Determine the p-value, which quantifies the probability of obtaining data as extreme as observed under the null hypothesis. A small p-value indicates that the null hypothesis is unlikely.
   - **Confidence level**: Set a confidence level (e.g., 95%) to determine the exclusion limits. The confidence level represents the probability that the true parameter values lie within the calculated limits if the experiment were repeated many times.

3. **Calculate limits**: The p-values for the signal-only and signal+BG hypotheses are combined in a certain way to obtain limits.  At the LHC, we use the so-called **$\mathrm{CL_s}$** quantity. 
   
   - **Expected limits:** Obtain by comparing observed data with 1) signal MC + estimated BG and 2) with only estimated BG. Observed limits check the consistency of the observation with the signal + BG hypothesis and compares it to the BG-only hypothesis.
   - **Expected limits:** Get the null hypothesis, e.g. background estimation from simulation or a data-driven method. Obtain the limits by comparing estimated BG with signal + estimated BG. Useful for predicting the analysis sensitivity.

4. **Compare and interpret**:

   - Compare the observed limits with the expected limits to interpret the results. If the observed limits are significantly different from the expected limits, this may indicate potential new physics.



