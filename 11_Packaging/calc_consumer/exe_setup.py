
import cx_Freeze

cx_Freeze.setup(
    name='NameIt',
    version="0.2.0",
    description="Name it",
    executables=[cx_Freeze.Executable('namer.py')]
)
