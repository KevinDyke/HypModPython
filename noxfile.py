""" nox file for hyper modern python project """
import nox 

@nox.session(python=["3.9","3.11"])
def tests(session):
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
