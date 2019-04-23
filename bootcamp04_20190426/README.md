# DS Bootcamp Environment Setup

For some module, you are required to install this environment.
For the rest, we will use Google Colab

#### Installing pyenv for python

For Mac:
```
brew install pyenv
```

For Ubuntu, you need to clone the repo.
```
cd
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```

Then, modify your environment variables.
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/<.bash_profile/.zshrc>
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/<.bash_profile/.zshrc>
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/<.bash_profile/.zshrc>
```
Note for *Ubuntu*, modify your `~/.bashrc` instead of `~/.bash_profile`.

Lastly, restart your shell so the path changes take effect.
```
exec "$SHELL"
```
* Refer to [pyenv](https://github.com/pyenv/pyenv#installation) for more details

#### Setting up the environment

Install dependencies:
(you have to be connected to Gojek Integration VPN in order to install dependencies from http://artifactory-gojek.golabs.io)

```
make env
```