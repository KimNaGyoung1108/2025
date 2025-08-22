import streamlit as st

st.title("🩺 증상 기반 건강 도우미")

# 키워드 매핑 (사용자가 입력할 수 있는 다양한 표현들)
symptom_keywords = {
    "두통": ["두통", "머리 아파", "편두통", "머리가 욱신", "머리가 무겁다"],
    "복통": ["복통", "배 아파", "속이 쓰려", "위가 아파", "장에 통증"],
    "기침": ["기침", "콜록", "목이 아프다", "가래"],
    "발열": ["열", "고열", "체온", "열이 난다"],
    "어지럼증": ["어지럽다", "빙글빙글", "현기증"]
}

# 증상-질환 매핑
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

if st.button("확인하기"):
    matched_symptom = None
    
    for main_symptom, keywords in symptom_keywords.items():
        for word in keywords:
            if word in user_input:
                matched_symptom = main_symptom
                break
    
    if matched_symptom:
        info = symptom_disease_map[matched_symptom]
        st.subheader(f"🩺 입력 증상 분류: {matched_symptom}")
        st.write("🔎 의심되는 질환:")
        for d in info["possible_diseases"]:
            st.write(f"- {d}")
        st.info(info["advice"])
    else:
        st.write("❓ 해당 증상은 데이터에 없습니다. 가까운 병원을 방문하세요.")
