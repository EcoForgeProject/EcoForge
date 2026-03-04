# examples/tool_calling_demo.py
from src.core.xai_client import create_chat
from xai_sdk.tools import tool

@tool
def get_chp_metrics(power: float, fuel: str = "propane") -> dict:
    """Get CHP performance metrics"""
    from src.tools.energy import chp_efficiency_calc
    return chp_efficiency_calc(power, fuel)

chat = create_chat()

chat.register_tools([get_chp_metrics])

# Fixed: use dict format instead of undefined 'user'
chat.append({"role": "user", "content": "What are realistic CHP metrics for a 8kW propane system?"})

response = chat.sample()
print("Response:", response.content)

if response.tool_calls:
    print("\nTool calls made:", len(response.tool_calls))
    for call in response.tool_calls:
        result = call.execute()
        print("Tool result:", result)
