path_hadronizer=Configuration/GenProduction/python/BToJpsiTomumu.py
py_gs=BToJpsiTomumu_GS.py
root_gs=BToJpsiTomumu_GS.root
nevt=1

cmsDriver.py $path_hadronizer --fileout file:$root_gs --mc --eventcontent RAWSIM --datatier GEN-SIM --conditions 106X_mc2017_realistic_v8 --beamspot Realistic25ns13TeVEarly2017Collision --step GEN,SIM --customise Configuration/DataProcessing/Utils.addMonitoring --geometry DB:Extended --era Run2_2017 --python_filename $py_gs -n $nevt --no_exec

cmsRun $py_gs

mv $py_gs GS/