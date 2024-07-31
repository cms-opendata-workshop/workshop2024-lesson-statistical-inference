---
title: "The CMS Combine statistical analysis and combination software"
teaching: 10
exercises: 0
---

:::::::::: questions

- What is Combine? 
- How do I input a statistical model into Combine?
- What tasks does Combine perform?
- Can I use Combine outside CMS? Where can I find detailed documentation?
- What does it mean to publish a statistical model, and why is it so important?

::::::::::

:::::::::: objectives

- Get introduced to the Combine tool.
- Learn the principles of how to input a statistical model
- Learn the set of tasks performed by Combine.
- Learn how to access information on how to run Combine outside CMS, and access documentation.
- Learn the concept of statistical model publication and how to access the first model published by CMS.

:::::::::::

## What is Combine?

**Combine** is the statistical analysis software used in CMS, built around the ROOT, RooFit and RooStats packages. 
It provides a command-line interface to several common workflows used in HEP statistical analysis. Combine provides a standardized access to these workflows, which makes it a very practical and reliable tool. As of 2024, more than 90% of the analyses in CMS use Combine for statistical inference.  

## Models and the datacard

Combine implements the statistical model and the corresponding likelihood in a RooFit-based custom class.  The inputs to the model are encapsulated in a human-readable configuration file called the **datacard**.
Datacard  includes information such as 

- signal and background processes, shapes and rates
- systematic and statistical uncertainties incorporated as nuisance parameters and their effects on the rates, along with their correlations
- multiplicative scale factors that modify the rate of a given process in a given channel

Combine supports building models for counting analyses, template shape analyses and parametric shape analyses. Though the main datacard syntax is similar for these three cases, there are minor differences reflecting the model input.  For example, in the case for a template shape model, one needs to specify a ROOT file with input histograms, and in the case of a parametric shape model, one needs to specify the process probability distribution functions.

Constructing a datacard is usually the level most users input information to Combine.  However, there are some cases where the statistical model requires modifications.  An example case is where we need a model with multiple parameters of interest associated with different signal processes (e.g. measurement of signal strengths for two different Higgs production channels, gluon-gluon fusion and vector boson fusion). Combine also allows to build custom models by introducing modified model classes.

Combine scales well with model complexity

is a powerful tool for combining a large number of 

Powerful for combinations, scales well with model complexity

## Tasks performed by Combine

Combine is capable of performing many statistical tasks.  The main interface is with the command below

```
combine <datacard.[txt|root]> -M <method>
```

where one enters a datacard (either as text or in a ROOT-converted format) and specifies the method pointing to a task.

Here is a set of methods used for extracting results:

- [http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/commonstatsmethods/#computing-limits-with-toys](**HybridNew:**) compute modified frequentist limits with pseudo-data, p-values, significance and confidence intervals with several options, --LHCmode LHC-limits is the recommended one.
- [http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/commonstatsmethods/#asymptotic-frequentist-limits](**AsymptoticLimits:**) limits calculated according to the asymptotic formulas in arxiv:1007.1727, valid for large event counts.
- [http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/commonstatsmethods/#asymptotic-significances](**Significance:**) simple profile likelihood approximation for calculating significances.
- [http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/commonstatsmethods/#bayesian-limits-and-credible-regions](**BayesianSimple:**) and [http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/commonstatsmethods/#computing-the-observed-bayesian-limit-for-arbitrary-models](**MarkovChainMC**) compute Bayesian upper limits and credible intervals for simple and arbitrary models.
- [http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/commonstatsmethods/#likelihood-fits-and-scans](**MultiDimFit:**) perform maximum likelihood fit, with multiple POIs, estimate CI from likelihood scans.

Combine also provides an extensive toolset for validation and diagnosis:

- [https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/commonstatsmethods/#goodness-of-fit-tests](**GoodnessOfFit:**) perform a goodness of fit test for models including shape information using several GoF estimators (saturated, Kolmogorov-Smirnov, Anderson-Darling) 
- [https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/nonstandard/#nuisance-parameter-impacts](**Impacts:**) evaluate the shift in POI from ￼ variation for each nuisance parameter.
- [http://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/commonstatsmethods/#channel-compatibility](**ChannelCompatibiltyCheck:**) check how consistent are the individual channels of a combination are
- [https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/part3/runningthetool/#generate-only](**GenerateOnly:**) generate random or Asimov pseudo-datasets for use as input to other methods

## Running Combine and detailed references

In 2024 Combine tool became available to the public along with

- a detailed paper: [CMS-CAT-23-001 / arXiv:2404.06614](https://arxiv.org/abs/2404.06614) and a 
- detailed user manual: [Combine github pages](https://cms-analysis.github.io/HiggsAnalysis-Combined
Limit/latest/)

The easiest way to run Combine is to use a Docker containerized version of it (which we will do in the next exercise).  However there are other ways to 

## Publishing statistical models

Statistical models provide an excellent resource for the community.  
Publishing them will help maximize the scientific impact of the analysis, and facilitate

- Preservation and documentation: the mathematical construction of the analysis in full detail.
Combination of multiple analyses
- Reinterpretation and reuse (within and outside the collaborations): 
- Education on statistics procedures
- Tool development: Statistical software updates can use real world examples to test and debug their recent developments.
- there will certainly be other use cases!

In December 2023, CMS Collaboration took the decision to release statistical models for all forthcoming analyses by default.
In accordance with open access policy of CERN and CMS.
Must be well-documented and understandable.
Publishing has always been highly desirable.  The difficulty was technical implementation. Now we have a way.




