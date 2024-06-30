from modelscope import AutoModelForCausalLM, AutoTokenizer, snapshot_download
from modelscope import GenerationConfig
import streamlit as st
model_dir = snapshot_download('TongyiFinance/Tongyi-Finance-14B')

# Note: The default behavior now has injection attack prevention off.
tokenizer = AutoTokenizer.from_pretrained(model_dir, trust_remote_code=True)

# use bf16
# model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="cuda:0", trust_remote_code=True, bf16=True).eval()
# use cpu only
# model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="cpu", trust_remote_code=True).eval()
model = AutoModelForCausalLM.from_pretrained(model_dir, device_map="cuda:0", trust_remote_code=True).eval()
# 模型加载指定device_map='cuda:0'，更改成device_map='auto'会使用所有可用显卡

# Specify hyperparameters for generation
model.generation_config = GenerationConfig.from_pretrained(model_dir, trust_remote_code=True)

inputs = tokenizer('市盈率是最常用来评估股价水平是否合理的指标之一，是指', return_tensors='pt')
inputs = inputs.to(model.device)
pred = model.generate(**inputs)
st.write(tokenizer.decode(pred.cpu()[0], skip_special_tokens=True))
st.balloons()