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
#python  -m ipykernel install --user --name=myenv
pip install transformers
pip install peft
pip install bitsandbytes
pip install datasets
pip install flash-attn
#"unsloth[cu121-ampere-torch231] @ git+https://github.com/unslothai/unsloth.git"
#for storage
#cip-quota
#ncdu
#pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121 --force-reinstall


#install deepspeed goto 
#before AttributeError: 'DeepSpeedCPUAdam' object has no attribute 'ds_opt_adam'
#The error show: cannot make a dir in /tmp/torch_extensions/build for cpu_adam.
#So I change the DEFAULT_TORCH_EXTENSION_PATH in the file /anaconda3/envs/XXXXX/lib/python3.6/site-packages/deepspeed/ops/op_builder/builder.py
#git clone deepspeed then goto folder deepspeed write DS_BUILD_CPU_ADAM=1 pip install 
