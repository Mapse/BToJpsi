from CRABClient.UserUtilities import config
import getpass

############################################################ To edit ############################################################
out_dir_base = '/store/group/uerj/' + getpass.getuser() + '/'
output_dataset = 'CRAB_PrivateMC_RunII_UL_2017_BToJpsi' # Comes after /store/user/mabarros/
storage_site = 'T2_US_Caltech'
############################################################ End editing ########################################################

config = config()
config.General.requestName = 'GS_BToJpsiTomumu_29-05-2025'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC' 
config.JobType.psetName = 'config/BToJpsiTomumu_GS.py'

config.Data.publication = True
config.Data.publishDBS = 'phys03'
config.Data.outputPrimaryDataset = output_dataset
config.Data.outputDatasetTag = 'BToJpsiTomumu' # Comes after outputPrimaryDataset
config.Data.splitting = 'EventBased' 
config.Data.unitsPerJob = 50000
config.JobType.eventsPerLumi = 1200
config.Data.totalUnits = config.Data.unitsPerJob * 10000
config.Data.outLFNDirBase = out_dir_base

config.Site.storageSite = storage_site
