import numpy as np
from qcengine.programs.tests.standard_suite_ref import answer_hash, compute_derived_qcvars, _std_suite, _std_generics


# in-repo extensions for _std_suite above
# * ideally empty. PR to QCEngine ASAP and empty this after QCEngine release.
_std_suite_psi4_extension = [
    # <<<  CONV-AE-CONV  >>>
    {
        "meta": {
            "system": "bh3p",
            "basis": "cc-pvdz",
            "scf_type": "pk",
            "reference": "rohf",
            "fcae": "ae",
            "corl_type": "conv",
            "sdsc": "sd",
        },
        "data": {
            "CISD CORRELATION ENERGY": -0.08142433,  # detci != cfour's vcc ???  # locally, replacing the rohf cisd vcc=tce value (stored in qcng) by the detci=guga value. correct sdsc label unclear.
            "FCI CORRELATION ENERGY": -0.084637876308811,  # detci
        },
    },
    {
        "meta": {
            "system": "nh2",
            "basis": "aug-cc-pvdz",
            "scf_type": "pk",
            "reference": "rohf",
            "fcae": "ae",
            "corl_type": "conv",
            "sdsc": "sd",
        },
        "data": {
            "CISD CORRELATION ENERGY": -0.1723668643052676,  # detci != vcc ???
        },
    },
    {
        "meta": {
            "system": "nh2",
            "basis": "cfour-qz2p",
            "scf_type": "pk",
            "reference": "rohf",
            "fcae": "ae",
            "corl_type": "conv",
            "sdsc": "sd",
        },
        "data": {
            "CISD CORRELATION ENERGY": -0.21038651,  # detci != vcc ???
        },
    },
    {
        "meta": {
            "system": "hf",
            "basis": "cc-pvdz",
            "scf_type": "pk",
            "reference": "rhf",
            "fcae": "ae",
            "corl_type": "conv",
            "sdsc": "sd"
        },
        "data": {
            "SVWN TOTAL HESSIAN": np.array(
                [
                    -0.011158529195,
                    -0.,
                    -0.,
                    0.011158509954,
                    -0.,
                    -0.,
                    -0.,
                    -0.011158529195,
                    -0.,
                    0.,
                    0.011158509954,
                    0.,
                    -0.,
                    -0.,
                    0.642213454497,
                    0.,
                    0.,
                    -0.642213457165,
                    0.011158509954,
                    0.,
                    0.,
                    -0.011155887562,
                    -0.,
                    -0.,
                    -0.,
                    0.011158509954,
                    0.,
                    -0.,
                    -0.011155887564,
                    -0.,
                    -0.,
                    0.,
                    -0.642213457165,
                    -0.,
                    -0.,
                    0.642216280292,
                ]).reshape((6,6)),
        },
    },
    {
        "meta": {
            "system": "h2o",
            "basis": "aug-cc-pvdz",
            "scf_type": "pk",
            "reference": "rhf",
            "fcae": "ae",
            "corl_type": "conv",
            "sdsc": "sd"
        },
        "data": {
            "SVWN TOTAL HESSIAN": np.array(
                [
                     -0.015282137109,
                     0.,
                     -0.,
                     0.007667256256,
                     0.,
                     -0.,
                     0.007667256256,
                     0.,
                     -0.,
                     0.,
                     0.714169890673,
                     0.000000000001,
                     -0.,
                     -0.357096356198,
                     0.282430177213,
                     -0.,
                     -0.357096356198,
                     -0.282430177213,
                     -0.,
                     0.000000000001,
                     0.45653162932,
                     0.,
                     0.223223468116,
                     -0.228270944088,
                     -0.,
                     -0.223223468116,
                     -0.228270944088,
                     0.007667256256,
                     -0.,
                     0.,
                     -0.008305196866,
                     0.,
                     0.,
                     0.000637932765,
                     -0.,
                     0.,
                     0.,
                     -0.357096356198,
                     0.223223468116,
                     0.,
                     0.385967088688,
                     -0.252826811188,
                     -0.,
                     -0.028870808826,
                     0.029603353817,
                     -0.,
                     0.282430177213,
                     -0.228270944088,
                     0.,
                     -0.252826811188,
                     0.219004239874,
                     0.,
                     -0.029603353817,
                     0.009266633228,
                     0.007667256256,
                     -0.,
                     -0.,
                     0.000637932765,
                     -0.,
                     0.,
                     -0.008305196866,
                     -0.,
                     0.,
                     0.,
                     -0.357096356198,
                     -0.223223468116,
                     -0.,
                     -0.028870808826,
                     -0.029603353817,
                     -0.,
                     0.385967088688,
                     0.252826811188,
                     -0.,
                     -0.282430177213,
                     -0.228270944088,
                     0.,
                     0.029603353817,
                     0.009266633228,
                     0.,
                     0.252826811188,
                     0.219004239874,
                ]).reshape((9, 9)),
        },
    },
    {
        "meta": {
            "system": "h2o",
            "basis": "cfour-qz2p",
            "scf_type": "pk",
            "reference": "rhf",
            "fcae": "ae",
            "corl_type": "conv",
            "sdsc": "sd"
        },
        "data": {
            "SVWN TOTAL HESSIAN": np.array(
                [
                     -0.010015602973,
                     -0.000000000001,
                     0.000000000002,
                     0.005034918743,
                     0.,
                     -0.,
                     0.005034918743,
                     -0.,
                     0.,
                     -0.000000000001,
                     0.699200093422,
                     -0.000000000002,
                     -0.,
                     -0.349611743856,
                     0.274596771974,
                     -0.,
                     -0.349611743856,
                     -0.274596771974,
                     0.000000000002,
                     -0.000000000002,
                     0.449624843917,
                     -0.,
                     0.216250731357,
                     -0.224817271283,
                     -0.,
                     -0.216250731357,
                     -0.224817271283,
                     0.005034918743,
                     -0.,
                     -0.,
                     -0.005839372129,
                     -0.,
                     0.,
                     0.000803489613,
                     0.,
                     0.,
                     0.,
                     -0.349611743856,
                     0.216250731357,
                     -0.,
                     0.379671911068,
                     -0.245424063175,
                     0.,
                     -0.030060195243,
                     0.029173021276,
                     -0.,
                     0.274596771974,
                     -0.224817271283,
                     0.,
                     -0.245424063175,
                     0.215395274362,
                     0.,
                     -0.029173021276,
                     0.009421810131,
                     0.005034918743,
                     -0.,
                     -0.,
                     0.000803489613,
                     0.,
                     0.,
                     -0.005839372129,
                     0.,
                     -0.,
                     -0.,
                     -0.349611743856,
                     -0.216250731357,
                     0.,
                     -0.030060195243,
                     -0.029173021276,
                     0.,
                     0.379671911068,
                     0.245424063175,
                     0.,
                     -0.274596771974,
                     -0.224817271283,
                     0.,
                     0.029173021276,
                     0.009421810131,
                     -0.,
                     0.245424063175,
                     0.215395274362,
                ]).reshape((9, 9)),
        },
    },

    # <<<  CONV-FC-CONV  >>>
    {
        "meta": {
            "system": "bh3p",
            "basis": "cc-pvdz",
            "scf_type": "pk",
            "reference": "rohf",
            "fcae": "fc",
            "corl_type": "conv",
            "sdsc": "sd",
        },
        "data": {
            "CISD CORRELATION ENERGY": -0.08045048714872,  # detci only != vcc ???
            "FCI CORRELATION ENERGY": -0.083612606639434,  # detci
        },
    },
    {
        "meta": {
            "system": "nh2",
            "basis": "aug-cc-pvdz",
            "scf_type": "pk",
            "reference": "rohf",
            "fcae": "fc",
            "corl_type": "conv",
            "sdsc": "sd",
        },
        "data": {
            "CISD CORRELATION ENERGY": -0.170209639586457,  # detci only != vcc ???
        },
    },
    {
        "meta": {
            "system": "nh2",
            "basis": "cfour-qz2p",
            "scf_type": "pk",
            "reference": "rohf",
            "fcae": "fc",
            "corl_type": "conv",
            "sdsc": "sd",
        },
        "data": {
            "CISD CORRELATION ENERGY": -0.186640254417867,  # detci only != vcc ???
        },
    },

    # <<<  DF-AE-DF  >>>
    {
        "meta": {
            "system": "hf",
            "basis": "cc-pvdz",
            "scf_type": "df",
            "reference": "rhf",
            "fcae": "ae",
            "corl_type": "df",
            "sdsc": "sd"
        },
        "data": {
            "SVWN TOTAL HESSIAN": np.array(
                [
                     -0.011171616682,
                     0.,
                     -0.,
                     0.011171597439,
                     0.,
                     -0.,
                     0.,
                     -0.011171616682,
                     -0.,
                     -0.,
                     0.01117159744,
                     0.,
                     -0.,
                     -0.,
                     0.642262891185,
                     0.,
                     0.,
                     -0.642262893846,
                     0.011171597439,
                     -0.,
                     0.,
                     -0.011168975069,
                     0.000000000001,
                     -0.000000000001,
                     0.,
                     0.01117159744,
                     0.,
                     0.000000000001,
                     -0.01116897507,
                     -0.,
                     -0.,
                     0.,
                     -0.642262893846,
                     -0.000000000001,
                     -0.,
                     0.64226571697,
                ]).reshape((6, 6)),
        },
    },
    {
        "meta": {
            "system": "h2o",
            "basis": "aug-cc-pvdz",
            "scf_type": "df",
            "reference": "rhf",
            "fcae": "ae",
            "corl_type": "df",
            "sdsc": "sd"
        },
        "data": {
            "SVWN TOTAL HESSIAN": np.array(
                [
                     -0.015306108227,
                     -0.,
                     -0.,
                     0.007679241821,
                     -0.,
                     0.,
                     0.007679241834,
                     -0.,
                     -0.,
                     -0.,
                     0.714095826016,
                     0.000000000011,
                     -0.,
                     -0.357059323956,
                     0.282410783964,
                     0.,
                     -0.357059323952,
                     -0.282410784003,
                     -0.,
                     0.000000000011,
                     0.456485072062,
                     0.,
                     0.22318907951,
                     -0.228247665448,
                     0.,
                     -0.22318907952,
                     -0.228247665506,
                     0.007679241821,
                     -0.,
                     0.,
                     -0.008316923332,
                     -0.,
                     -0.,
                     0.000637673685,
                     0.,
                     -0.,
                     -0.,
                     -0.357059323956,
                     0.22318907951,
                     -0.,
                     0.3859291338,
                     -0.252799920245,
                     0.,
                     -0.028869886253,
                     0.029610851501,
                     0.,
                     0.282410783964,
                     -0.228247665448,
                     -0.,
                     -0.252799920245,
                     0.218979358918,
                     -0.,
                     -0.029610851534,
                     0.009268235563,
                     0.007679241834,
                     0.,
                     0.,
                     0.000637673685,
                     0.,
                     -0.,
                     -0.008316923345,
                     -0.,
                     -0.,
                     -0.,
                     -0.357059323952,
                     -0.22318907952,
                     0.,
                     -0.028869886253,
                     -0.029610851534,
                     -0.,
                     0.385929133855,
                     0.252799920322,
                     -0.,
                     -0.282410784003,
                     -0.228247665506,
                     -0.,
                     0.029610851501,
                     0.009268235563,
                     -0.,
                     0.252799920322,
                     0.218979358932,
                ]).reshape((9, 9)),
        },
    },
    {
        "meta": {
            "system": "h2o",
            "basis": "cfour-qz2p",
            "scf_type": "df",
            "reference": "rhf",
            "fcae": "ae",
            "corl_type": "df",
            "sdsc": "sd"
        },
        "data": {
            "SVWN TOTAL HESSIAN": np.array(
                [
                     -0.009990362405,
                     -0.,
                     0.000000000001,
                     0.00502229918,
                     -0.,
                     0.,
                     0.005022299179,
                     0.,
                     0.,
                     -0.,
                     0.699077256021,
                     0.,
                     -0.,
                     -0.349550325666,
                     0.274539445833,
                     0.,
                     -0.349550325662,
                     -0.274539445833,
                     0.000000000001,
                     0.,
                     0.449564210084,
                     0.,
                     0.216190331109,
                     -0.22478695452,
                     0.,
                     -0.216190331109,
                     -0.224786954525,
                     0.00502229918,
                     -0.,
                     0.,
                     -0.005826835703,
                     0.,
                     -0.,
                     0.000803572097,
                     0.,
                     0.,
                     -0.,
                     -0.349550325666,
                     0.216190331109,
                     0.,
                     0.379622159841,
                     -0.245365200208,
                     0.,
                     -0.030071862218,
                     0.029174558331,
                     0.,
                     0.274539445833,
                     -0.22478695452,
                     -0.,
                     -0.245365200208,
                     0.215364149782,
                     0.,
                     -0.029174558332,
                     0.009422617805,
                     0.005022299179,
                     0.,
                     0.,
                     0.000803572097,
                     0.,
                     0.,
                     -0.005826835703,
                     0.,
                     -0.,
                     0.,
                     -0.349550325662,
                     -0.216190331109,
                     0.,
                     -0.030071862218,
                     -0.029174558332,
                     0.,
                     0.379622159838,
                     0.245365200207,
                     0.,
                     -0.274539445833,
                     -0.224786954525,
                     0.,
                     0.029174558331,
                     0.009422617805,
                     -0.,
                     0.245365200207,
                     0.215364149785,
                ]).reshape((9, 9)),
        },
    },
    # <<<  CD-AE-CD  >>>
    # <<<  CD-FC-CD  >>>
]


for calc1 in _std_suite_psi4_extension:
    metahash1 = answer_hash(**calc1["meta"])
    for calc0 in _std_suite:
        metahash0 = answer_hash(**calc0["meta"])
        if metahash0 == metahash1:
            calc0["data"].update(calc1["data"])
            break

compute_derived_qcvars(_std_suite)
std_suite = {answer_hash(**calc["meta"]): calc["data"] for calc in _std_suite}