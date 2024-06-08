mkdir /proj/ciptmp/ix05ogym
# source ~/.bashrc 
# source ~/.bashrc
cd /proj/ciptmp/ix05ogym
python3.11 -m venv myenv --system-site-packages
source myenv/bin/activate
#deactivate
#vscode env
#https://techinscribed.com/python-virtual-environment-in-vscode/
#https://stackoverflow.com/questions/58119823/jupyter-notebooks-in-visual-studio-code-does-not-use-the-active-virtual-environm
pip install transformers
pip install peft
pip install bitsandbytes
pip install datasets
pip install flash-attn
#"unsloth[cu121-ampere-torch231] @ git+https://github.com/unslothai/unsloth.git"
#for storage
#cip-quota
#ncdu