---
title: Setup
---

This exercise uses Combine, the CMS statistical analysis and combination tool. 
Combine is built around ROOT, RooFit and RooStats. It provides a command-line interface to several common workflows used in HEP statistical analysis.  

More information on Combine can be found in 

* the Combine paper: [CMS-CAT-23-001 / arXiv:2404.06614](https://arxiv.org/abs/2404.06614)
* detailed user manual: [Combine github pages](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/latest/)

CMS users can use Combine as part of CMS software. But Combine was also recently released for public use ([public use instructions](https://cms-analysis.github.io/HiggsAnalysis-CombinedLimit/latest/#oustide-of-cmssw-recommended-for-non-cms-users)).

:::::::::::: prereq

For this exercise, we will use a standalone version of Combine available in a Docker container.

Install the Combine container using

```bash
docker run --name combine -it gitlab-registry.cern.ch/cms-cloud/combine-standalone:v9.2.1
```

You can start the container using

```bash
docker start -i combine
```

::::::::::::





