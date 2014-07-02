import cx_Freeze

cx_Freeze.setup(
    name='web_searcher',
    version="0.2.0",
    description="Fun web searching",
    executables=[cx_Freeze.Executable('web_searcher.py')]
)
