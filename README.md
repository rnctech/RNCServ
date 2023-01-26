# RNCServ
service for generation of text, graph and Chinese Poet, Couplet etc.

1, install dependencies
pip3 install -r requirements.txt

2, install paddle and puddlehub for generate Chinese poems / couplets 

 python -m pip install paddlepaddle==2.4.1 -i https://pypi.tuna.tsinghua.edu.cn/simple \
 pip install paddlehub
 
3, run Flask server with environment variable as below \

export API_TOKEN=YOUR_OPENAI_TOKEN \
export REPLICATE_API_TOKEN=YOUR_REPLICATE_TOKEN_OF_GITHUB

4, start server\
python app.py \
go to http://127.0.0.1:8080


