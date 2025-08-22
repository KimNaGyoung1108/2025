import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

st.title("🧠 AI 기반 증상 분류 건강 도우미")
st.write("⚠️ 이 앱은 참고용 조언만 제공합니다. 의학적 진단은 병원에서 받으세요.")

symptom_disease_map = {
    "두통": {
        "possible_diseases": ["긴장성 두통", "편두통", "감기"],
        "advice": "💡 휴식과 수분 섭취를 하고, 지속되면 진료를 권유합니다."
    },
    "복통": {
        "possible_diseases": ["소화불량", "위염", "장염"],
        "advice": "💡 자극적인 음식을 피하고, 심한 통증은 병원 진료가 필요합니다."
    },
    "기침": {
        "possible_diseases": ["감기", "기관지염", "천식"],
        "advice": "💡 따뜻한 물을 마시고, 2주 이상 지속되면 진료를 권유합니다."
    },
    "발열": {
        "possible_diseases": ["독감", "폐렴", "코로나19"],
        "advice": "💡 체온을 확인하고, 고열이 지속되면 병원에 가야 합니다."
    },
    "어지럼증": {
        "possible_diseases": ["빈혈", "저혈압", "내이질환"],
        "advice": "💡 충분한 휴식을 취하세요. 반복되면 진료를 권유합니다."
    }
}

user_input = st.text_input("현재 증상을 구체적으로 입력하세요:")

if st.button("AI에게 물어보기") and user_input.strip() != "":
    categories = list(symptom_disease_map.keys())
    prompt = f"""
    사용자가 증상을 설명하면 아래 카테고리 중 가장 적절한 것을 골라줘:
    카테고리: {categories}
    사용자 입력: "{user_input}"
    출력은 반드시 하나의 카테고리만 답해.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    matched_symptom = response.choices[0].message.content.strip()

    if matched_symptom in symptom_disease_map:
        info = symptom_disease_map[matched_symptom]
        st.subheader(f"🩺 AI가 분류한 증상: {matched_symptom}")
        st.write("🔎 의심되는 질환:")
        for d in info["possible_diseases"]:
            st.write(f"- {d}")
        st.info(info["advice"])
    else:
        st.error("AI가 적절한 증상을 찾지 못했습니다. 다시 입력해보세요.")
