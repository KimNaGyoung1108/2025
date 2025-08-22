import streamlit as st

st.title("🩺 증상 기반 건강 도우미")
st.write("⚠️ 이 앱은 참고용 조언만 제공합니다. 정확한 진단은 반드시 의료기관에서 받으세요.")

# 키워드 매핑 (다양한 표현 → 대표 증상)
symptom_keywords = {
    "두통": ["두통", "머리 아파", "머리가 욱신", "머리가 띵해", "편두통", "머리가 지끈"],
    "복통": ["복통", "배 아파", "속이 쓰려", "위가 아파", "장에 통증", "속이 더부룩"],
    "기침": ["기침", "콜록", "목이 아파", "가래", "기침이 심해"],
    "발열": ["발열", "열", "체온 올라감", "고열", "열이 난다"],
    "어지럼증": ["어지럽다", "빙글빙글", "현기증", "머리가 핑 돈다"],
    "가슴통증": ["가슴 아파", "흉통", "가슴 답답", "가슴이 조여옴"],
    "호흡곤란": ["숨차다", "호흡곤란", "숨쉬기 힘들다", "가쁜 호흡"],
    "설사": ["설사", "배가 자주 아파서 화장실 감", "묽은 변", "장에 탈"],
    "피로감": ["피곤하다", "무기력", "기운 없음", "쉽게 지침", "피로감"],
    "체중감소": ["체중이 줄었다", "살이 빠짐", "갑자기 마름", "체중감소"]
}

# 증상-질환 매핑
symptom_disease_map = {
    "두통": {
        "possible_diseases": ["긴장성 두통", "편두통", "감기"],
        "advice": "💡 충분한 휴식과 수분 섭취를 하세요. 증상이 지속되면 병원을 방문하세요."
    },
    "복통": {
        "possible_diseases": ["소화불량", "위염", "장염", "과민성 대장 증후군"],
        "advice": "💡 자극적인 음식을 피하세요. 통증이 심하거나 오래가면 병원을 권유합니다."
    },
    "기침": {
        "possible_diseases": ["감기", "기관지염", "천식", "폐렴"],
        "advice": "💡 따뜻한 물을 마시고, 2주 이상 지속되면 병원을 방문하세요."
    },
    "발열": {
        "possible_diseases": ["독감", "폐렴", "코로나19", "감염성 질환"],
        "advice": "💡 체온을 확인하세요. 38도 이상 고열이 지속되면 즉시 진료가 필요합니다."
    },
    "어지럼증": {
        "possible_diseases": ["빈혈", "저혈압", "메니에르병", "혈액순환 장애"],
        "advice": "💡 충분히 쉬고, 반복되면 병원을 방문하세요."
    },
    "가슴통증": {
        "possible_diseases": ["협심증", "심근경색", "역류성 식도염"],
        "advice": "💡 흉통이 심하거나 왼쪽 팔/턱으로 통증이 퍼지면 즉시 응급실로 가야 합니다."
    },
    "호흡곤란": {
        "possible_diseases": ["천식", "폐렴", "만성폐쇄성폐질환(COPD)", "심부전"],
        "advice": "💡 호흡이 불편하면 응급 상황일 수 있습니다. 즉시 진료가 필요합니다."
    },
    "설사": {
        "possible_diseases": ["장염", "식중독", "과민성 대장 증후군"],
        "advice": "💡 수분을 충분히 섭취하세요. 혈변이나 탈수 증상이 있으면 병원에 가야 합니다."
    },
    "피로감": {
        "possible_diseases": ["빈혈", "갑상선 질환", "수면 부족", "만성 피로 증후군"],
        "advice": "💡 충분히 쉬고, 피로가 장기간 지속되면 진료를 권유합니다."
    },
    "체중감소": {
        "possible_diseases": ["갑상선 항진증", "당뇨병", "암", "만성 감염"],
        "advice": "💡 원인 모를 체중 감소는 반드시 병원에서 검사가 필요합니다."
    }
}

# 사용자 입력
user_input = st.text_input("현재 증상을 구체적으로 입력하세요:")

if st.button("확인하기"):
    matched_symptom = None
    for main_symptom, keywords in symptom_keywords.items():
        for word in keywords:
            if word in user_input:
                matched_symptom = main_symptom
                break
        if matched_symptom:
            break

    if matched_symptom:
        info = symptom_disease_map[matched_symptom]
        st.subheader(f"🩺 입력 증상 분류: {matched_symptom}")
        st.write("🔎 의심되는 질환:")
        for d in info["possible_diseases"]:
            st.write(f"- {d}")
        st.info(info["advice"])
    elif user_input.strip() == "":
        st.warning("⚠️ 증상을 입력해주세요.")
    else:
        st.error("❓ 해당 증상은 데이터에 없습니다. 가까운 병원을 방문하세요.")
