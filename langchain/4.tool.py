from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
_result=StrOutputParser()
_llm=ChatOpenAI(
    api_key="ollama", #ollama api_key随便写
    model="qwen2.5:7b", #看ollama中的名
    base_url="http://192.168.10.11:60006/v1",#注意后面加v1
    temperature=0.7
)
_prompt="""
你可以根据用户问题，调用以下的工具：
    查询天气：weather(city),参数city就是查询的城市
    做加法：add(a,b),参数a,b是相加的两个数
返回的结果，按以下的json格式：
{
    "type":1, #如果该值为0，表示没有调用工具，如果该值为1表示调用了工具
    "tool":"xxx", #如果调用了工具，这个值格式为fun_name(\"arg1\",\"arg2\",...)
    "message":"xxx" #如果没有调用工具，直接返回结果
}
问题：2*3=？
"""
rep=_llm.invoke(_prompt)
print(_result.invoke(rep))