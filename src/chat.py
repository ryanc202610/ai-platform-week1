import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. 自動載入同目錄下的 .env 檔案環境變數
load_dotenv()

# 2. 讀取環境變數
base_url = os.getenv("LLM_BASE_URL")
api_key = os.getenv("LLM_API_KEY")
model_name = os.getenv("LLM_MODEL")

# 檢查變數是否正確載入
if not api_key or "your_api_key" in api_key:
    raise ValueError("請先在 .env 檔案中填入正確的 LLM_API_KEY！")

print(f"正在初始化客戶端...")
print(f"Base URL: {base_url}")
print(f"使用模型: {model_name}\n")

# 3. 初始化 OpenAI 客戶端（串接 Gemini OpenAI-Compatible Endpoint）
client = OpenAI(
    base_url=base_url,
    api_key=api_key
)

try:
    # 4. 發送對話請求
    print("正在發送請求給 Gemini...請耐心等候")
    response = client.chat.completions.create(
        model=model_name,
        messages=[
          {"role": "user", "content": "你好！請用繁體中文打個招呼。"}
        ]
    )

    # 5. 印出模型回覆的內容
    reply = response.choices[0].message.content
    print("\n==== Gemini 回覆 ====\n")
    print(reply)
    print("\n=====================\n")
    
    # 6. 觀察並印出 Token 費用與消耗狀況
    if response.usage:
        print("【Token 消耗統計】:")
        print(f" ├─ 輸入 Token 數 (Prompt): {response.usage.prompt_tokens}")
        print(f" ├─ 輸出 Token 數 (Completion): {response.usage.completion_tokens}")
        print(f" └─ 總共消耗 Token 數: {response.usage.total_tokens}")
        print("\n提示：目前使用的是免費額度，不會扣取真實費用。")
    else:
        print("\n無法取得 Token 消耗數據。")

except Exception as e:
    print(f"\n❌ 呼叫 API 時發生錯誤: {e}")
    print("提示：請檢查 .env 中的 API Key 是否正確，以及網路連線是否正常。")
