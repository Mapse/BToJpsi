# BToJpsi - CMS Monte Carlo Generation

This repository contains the setup to run a **B → J/ψ** Monte Carlo simulation within the **CMSSW** framework.

## Setup Instructions

Follow the steps below to set up the environment and compile the CMSSW release necessary for the generation.

---

### Steps to configure

```bash

# Clones the BToJpsi repository to your local machine.
git clone git@github.com:Mapse/BToJpsi.git

# Enters the cloned repository directory.
cd BToJpsi/

# Switches to the 'cmssw-el7' environment, required for CMSSW_10_6_X releases.
# On lxplus, this ensures you are using a CentOS 7 compatible environment.
cmssw-el7

# Creates a new CMSSW release area with version CMSSW_10_6_20_patch1.
cmsrel CMSSW_10_6_20_patch1

# Navigates into the 'src' directory of the CMSSW release area.
cd CMSSW_10_6_20_patch1/src

# Sets up the CMSSW runtime environment.
# This configures the environment variables required to use CMSSW tools.
cmsenv
# Builds (compiles) the CMSSW environment and all the code in the src directory.
scram b


