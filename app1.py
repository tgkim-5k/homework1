import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os

# 시스템별 한글 폰트 경로 설정
if platform.system() == "Windows":
    font_path = "C:/Windows/Fonts/NanumGothic.ttf"
elif platform.system() == "Darwin":
    font_path = "/System/Library/Fonts/AppleGothic.ttf"
else:  # Linux / Streamlit Cloud / Docker 등
    font_path = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"

# 존재하는 폰트 경로일 경우만 적용
if os.path.exists(font_path):
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rcParams["font.family"] = font_name
else:
    print("⚠️ 폰트 파일이 존재하지 않습니다. 한글이 깨질 수 있습니다.")

plt.rcParams["axes.unicode_minus"] = False  # 마이너스 깨짐 방지
plt.rcParams.update({"font.size": 18})      # 폰트 크기 조정 (선택사항)

