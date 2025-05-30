import FWCore.ParameterSet.Config as cms
from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.MCTunes2017.PythiaCP5Settings_cfi import *
from GeneratorInterface.EvtGenInterface.EvtGenSetting_cff import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(0),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         comEnergy = cms.double(13000.0),
                         maxEventsToPrint = cms.untracked.int32(0),
                         ExternalDecays = cms.PSet(
        EvtGen130 = cms.untracked.PSet(
            decay_table = cms.string('GeneratorInterface/EvtGenInterface/data/DECAY_2010.DEC'),
            particle_property_file = cms.FileInPath('GeneratorInterface/EvtGenInterface/data/evt.pdl'),
            operates_on_particles = cms.vint32()
        ),
        parameterSets = cms.vstring('EvtGen130')
        ),
                         PythiaParameters = cms.PSet(
        pythia8CommonSettingsBlock,
        pythia8CP5SettingsBlock,
        processParameters = cms.vstring(

            'HardQCD:all = on',
            'PhaseSpace:pTHatMin = 15.',

            'PTFilter:filter = on',
            'PTFilter:quarkToFilter = 5',
            'PTFilter:scaleToFilter = 1.0',

            ),
        parameterSets = cms.vstring('pythia8CommonSettings',
                                    'pythia8CP5Settings',
                                    'processParameters',
                                    )
        )
                         )

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$1.0$'),
    name = cms.untracked.string('$Generic BBbar with a JPsi$'),
    annotation = cms.untracked.string('Generic BBbar with a JPsi')
    )

generator.PythiaParameters.processParameters.extend(EvtGenExtraParticles)

###########
# Filters #
###########
# Filter only pp events which produce a B:

bfilter = cms.EDFilter("PythiaFilter",
                       ParticleID = cms.untracked.int32(5)
                       )


oniafilter = cms.EDFilter("PythiaFilter",
                          Status = cms.untracked.int32(2),
                          MaxEta = cms.untracked.double(1.2),
                          MinEta = cms.untracked.double(-1.2),
                          MinPt = cms.untracked.double(25.0),
                          MaxPt = cms.untracked.double(100.0),
                          ParticleID = cms.untracked.int32(443)
                          )


mumugenfilter = cms.EDFilter("MCParticlePairFilter",
    Status = cms.untracked.vint32(1, 1),
    MinP = cms.untracked.vdouble(2.7, 2.7),
    MinPt = cms.untracked.vdouble(3.0, 3.0),
    MaxPt = cms.untracked.vdouble(150, 150),
    MaxEta = cms.untracked.vdouble(2.4, 2.4),
    MinEta = cms.untracked.vdouble(-2.4, -2.4),
    ParticleCharge = cms.untracked.int32(-1),
    ParticleID1 = cms.untracked.vint32(13),
    ParticleID2 = cms.untracked.vint32(13),
    MinInvMass = cms.untracked.double(2.95),
    MaxInvMass = cms.untracked.double(3.25),
)

ProductionFilterSequence = cms.Sequence(generator*bfilter*oniafilter*mumugenfilter)
