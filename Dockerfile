FROM python:3.7

ENV WORKDIR=/usr/src/ckiptagger
WORKDIR $WORKDIR

# tensorflow-gpu 從 TensorFlow 2.1 開始已被移除，故 tfgpu 選項已無效
RUN pip install -U ckiptagger[tf,gdown]

# 從 google drive 下載最新的資料
COPY download.py .
RUN python download.py

COPY tagging.py .
ENTRYPOINT ["python", "/usr/src/ckiptagger/tagging.py"]
