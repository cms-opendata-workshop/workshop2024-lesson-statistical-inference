# Script to construct a count datacard from a ROOT file
# from a Zprime analysis, CMS Open Data workshop, 2024
# Author: Sezen Sekmen

#!/usr/bin/env python

import os,sys
from string import *
import argparse
import ROOT

dcargs = argparse.ArgumentParser()
dcargs.add_argument('--startbin', type=int, default=1)
dcargs.add_argument('--stat', action='store_true')
dcargs.add_argument('--lm', action='store_true')

# parse the command line
args = dcargs.parse_args()

startbin = args.startbin
stat = args.stat
lm = args.lm

# Processes:
procs = ['signal','tt_semilep', 'tt_had', 'tt_lep', 'wjets']
# Nuisances
nuis = ['pu', 'muId']

# Open the input ROOT file
fin = ROOT.TFile("Zprime_hists_FULL.root", "READ")

# Create a new ROOT file to save the modified histograms
dcname = 'datacard_count.txt'
if startbin > 1: 
    dcname = 'datacard_count_bin'+str(startbin)+'.txt'
    print('Integrating from bin '+str(startbin))

fdc = open(dcname, "w")

# Write the header and the observation
header = '''imax 1 # number of channels
jmax %s # number of backgrounds
kmax * # number of nuisances
# --------------------------------------
bin             ch1
observation     %s
# --------------------------------------
''' 

hdt = fin.Get("mtt__data_obs")
endbin = int(hdt.GetXaxis().GetNbins())
ndt = hdt.Integral(startbin,endbin)
nbgs = len(procs) - 1

fdc.write(header % (str(nbgs), str(ndt)))

# Write the processes and rates:
line1 = '%-27s' % 'bin'
line2 = '%-27s' % 'process'
line3 = '%-27s' % 'process'
line4 = '%-27s' % 'rate'
print('%15s %15s %15s %8s' % ('process', 'unweighted evts', 'weighted evts', 'weight'))
i = 0
for p in procs:
    hc = fin.Get('mtt__'+p)
    line1 = line1 + "%-15s" % 'ch1'
    line2 = line2 + "%-15s" % p
    line3 = line3 + "%-15d" % i
    line4 = line4 + "%-15.2f" % hc.Integral(startbin,endbin)
    entryforselbins = hc.GetEntries() * (hc.Integral(startbin, endbin) / hc.Integral())
    w = hc.Integral(startbin, endbin) / entryforselbins
    print('%15s %15d %15.2f %8.4f' % (p, entryforselbins, hc.Integral(startbin, endbin), w))
    i = i + 1
fdc.write(line1+'\n')
fdc.write(line2+'\n')
fdc.write(line3+'\n')
fdc.write(line4+'\n')
fdc.write('# -------------------------------------- \n')

# Write the nuisances and their effects on processes:
for n in nuis:
    line = '%-16s' % n
    line = line + '%-11s' % 'lnN'
    for p in procs:
        hc = fin.Get('mtt__'+p)
        hu = fin.Get('mtt__'+p+'__'+n+'Up')
        hd = fin.Get('mtt__'+p+'__'+n+'Down')
        rup = hu.Integral(startbin,endbin) / hc.Integral(startbin,endbin)
        rdn = hd.Integral(startbin,endbin) / hc.Integral(startbin,endbin)
        x = "%.4f/%.4f" % (rup, rdn)
        line = line + '%-15s' % x
    fdc.write(line+'\n')

# Add the random lumi systematic
if lm:
    line = '%-16s' % 'lumi'
    line = line + '%-11s' % 'lnN'
    for p in procs:
        line = line + '%-15s' % '1.025'
    fdc.write(line+'\n')

# Add statistical uncertainties
if stat:
    i = 0
    for p in procs:
        line = '%-16s' % ('stat_'+p)
        line = line + '%-4s' % 'gmN'
        hc = fin.Get('mtt__'+p)
        entryforselbins = hc.GetEntries() * (hc.Integral(startbin, endbin) / hc.Integral())
        line = line + '%-7d' % entryforselbins
        w = hc.Integral(startbin, endbin) / entryforselbins
        line = line + ('%-15s' % '-') * i + ('%-15.4f' % w) + ('%-15s' % '-') * (len(procs) - i - 1)
        fdc.write(line+'\n')
        i = i + 1

# close the files
fin.Close()

print('The datacard ** '+dcname+' ** is created.\n')
