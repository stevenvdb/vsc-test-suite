envars = {
    'VSC_HOME':
    {
        'exe': ['print(os.environ["USER"] in os.environ["VSC_HOME"])'],
    },
    'VSC_DATA':
    {
        'exe': ['print(os.environ["USER"] in os.environ["VSC_DATA"])'],
    },
    'VSC_SCRATCH':
    {
        'exe': ['print(os.environ["USER"] in os.environ["VSC_SCRATCH"])'],
    },
    'VSC_ARCH_LOCAL':
    {
        # archspec is automatically installed as part of ReFrame
        'exe': [
            'import archspec.cpu',
            'aliases = {"skylake": "skylake_avx512"}',  # exceptions to the (full) archspec name
            'env = os.environ["VSC_ARCH_LOCAL"]',
            'if env in aliases.keys():',
            '    env = aliases[env]',
            'print(env == archspec.cpu.host().name)',
        ],
    },
    'VSC_ARCH_SUFFIX':
    {
        'exe': ['print(os.environ["VSC_ARCH_SUFFIX"] in ["", "-ib"])'],
    },
    'VSC_INSTITUTE':
    {
        'exe': ['print(os.environ["VSC_INSTITUTE"] in ["antwerpen", "brussel", "gent", "leuven"])'],
    },
    'VSC_INSTITUTE_LOCAL':
    {
        'exe': ['print(os.environ["VSC_INSTITUTE_LOCAL"] in ["antwerpen", "brussel", "gent", "leuven"])'],
    },
    'VSC_INSTITUTE_CLUSTER':
    {
        'exe': ['print(os.environ["VSC_INSTITUTE_CLUSTER"] != "")'],
    },
    'VSC_OS_LOCAL':
    {
        'exe': ['print(os.environ["VSC_OS_LOCAL"] in ["CO7", "RHEL8", "centos8", "centos7"])'],
    },
    'VSC_SCRATCH_NODE':
    {
        'exe': ['print(os.environ["VSC_SCRATCH_NODE"] in ["/local", "/node_scratch", "/tmp"])'],
    },
    'VSC_SCRATCH_SITE':
    {
        'exe': ['print(os.environ["VSC_SCRATCH_SITE"] == os.environ["VSC_SCRATCH"])'],
    },
}
