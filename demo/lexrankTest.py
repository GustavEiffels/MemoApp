from lexrank import LexRank
from nltk.tokenize import sent_tokenize
import nltk
from konlpy.tag import Okt # Konlpy의 형태소 분석기 예시

# --- NLTK Punkt and Punkt_Tab Tokenizer Download ---
try:
    print("NLTK Punkt 토크나이저를 다운로드하거나 존재를 확인합니다...")
    nltk.download('punkt') # Main Punkt tokenizer
    print("NLTK Punkt tokenizer 준비 완료.")

    print("NLTK Punkt_Tab 토크나이저를 다운로드하거나 존재를 확인합니다...")
    nltk.download('punkt_tab')
    print("NLTK Punkt_Tab 토크나이저 준비 완료.")

except Exception as e:
    print(f"NLTK 토크나이저 다운로드 중 오류 발생: {e}")
    print("수동으로 다운로드해야 할 수도 있습니다. Python 인터프리터에서 'import nltk; nltk.download(\"punkt\"); nltk.download(\"punkt_tab\")'를 실행해보세요.")
    exit()

# --- 한국어 텍스트 ---
korean_text = """
5일 윤석열 전 대통령을 소환한 내란특검은 피의자 조사가 오후 6시 34분 종료됐다고 밝혔다. 윤 전 대통령은 이날 진술한 내용이 담긴 조서를 열람한 뒤 귀가할 예정이다.
윤 전 대통령은 이날 오전 9시 1분 서울고검 1층 중앙 현관에 도착했고, 조사실로 바로 향했다. 별도의 티타임 없이 9시 4분부터 조사가 시작됐다. 오전 조사는 정오를 약간 넘긴 오후 12시 5분쯤 종료됐고, 오후 조사는 1시 7분 재개됐다. 순수 조사 시간을 모두 더할 경우 8시간 28분이 된다. 지난달 28일 1차 조사 때 총 조사 시간은 5시간 5분이었다.
윤 전 대통령은 1차 조사 당시 조서 열람에 3시간가량을 썼다. 이날은 실제 조사가 이뤄진 시간이 더 긴 만큼, 조서 열람에도 더 많은 시간을 쓸 것으로 보인다. 윤 전 대통령은 이날 저녁식사를 하지 않고 조서를 열람하겠다는 뜻을 특검 측에 밝혔고, 특검도 오전 9시에 출석해 성실히 조사에 임한 점을 감안해 이를 받아들였다고 한다.
"""

# --- 1단계: 텍스트를 문장 단위로 분리 (토큰화) ---
sentences = sent_tokenize(korean_text)
print("\n--- 원본 문장들 ---")
for i, sent in enumerate(sentences):
    print(f"  {i+1}. {sent}")
print("\n" + "="*50 + "\n")

# --- 2단계: LexRank 초기화 및 요약 생성 ---
lxr = LexRank(sentences, stopwords=None)
desired_summary_sentences = 4
extracted_sentences = lxr.get_summary(sentences, threshold=None)
final_summary_sentences = []
if extracted_sentences:
    if len(extracted_sentences) > desired_summary_sentences:
        final_summary_sentences = extracted_sentences[:desired_summary_sentences]
    else:
        final_summary_sentences = extracted_sentences
else:
    print("경고: LexRank가 문장을 추출하지 못했습니다. 원본 텍스트에서 강제로 문장을 자릅니다.")
    if len(sentences) >= desired_summary_sentences:
        final_summary_sentences = sentences[:desired_summary_sentences]
    else:
        final_summary_sentences = sentences

print(f"--- 생성된 요약 ({len(final_summary_sentences)} 문장) ---")
for i, sent in enumerate(final_summary_sentences):
    print(f"  {i+1}. { {sent}}")

# --- 3단계: 요약된 내용을 바탕으로 원문의 내용 정의 (자동화 시도) ---
def define_text_content_auto(summary_list):
    if not summary_list:
        return "이 텍스트는 분석할 내용이 부족합니다."

    okt = Okt() # 형태소 분석기 초기화
    keywords = []
    
    # 요약 문장에서 명사 추출
    for sentence in summary_list:
        # nouns()는 명사만 추출해줍니다.
        keywords.extend([word for word, tag in okt.pos(sentence) if tag in ['Noun'] and len(word) > 1]) 
    
    # 키워드 빈도 계산
    from collections import Counter
    keyword_counts = Counter(keywords)
    
    # 가장 빈번한 상위 N개 키워드 선택 (예: 5개)
    top_keywords = [word for word, count in keyword_counts.most_common(5)]

    # 키워드를 바탕으로 정의 문장 생성 (매우 단순한 형태)
    if top_keywords:
        main_subject = top_keywords[0] if top_keywords else "내용"
        definition = f"이 글은 **{main_subject}**에 대한 내용을 담고 있습니다. 주요 키워드는 {', '.join(top_keywords)} 등입니다. 이는 텍스트의 핵심 주제를 나타냅니다."
        
        # 좀 더 상세한 정의를 위해 요약 문장들을 일부 조합할 수 있습니다.
        # 예시: 요약 첫 문장과 주요 키워드를 조합
        if summary_list:
            first_summary_sentence = summary_list[0].replace('\n', ' ').strip()
            definition_parts = [
                f"이 글은 다음과 같은 내용을 다룹니다: **{first_summary_sentence}**",
                f"주요 주제 및 키워드는 **{', '.join(top_keywords)}** 등입니다."
            ]
            # 모든 요약 문장을 연결하여 더 긴 정의를 만들 수도 있습니다.
            # definition_parts.append("추출된 요약 내용은 다음과 같습니다: " + " ".join(summary_list))
            return "\n".join(definition_parts)
        else:
            return definition
    else:
        return "요약 문장에서 핵심 키워드를 추출할 수 없었습니다."

print("\n" + "="*50 + "\n")
print("--- 원문의 핵심 내용 정의 (자동화 시도) ---")
text_definition = define_text_content_auto(final_summary_sentences)
print(text_definition)