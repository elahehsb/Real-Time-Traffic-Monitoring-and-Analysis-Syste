FROM nvcr.io/nvidia/l4t-base:r32.4.3

RUN apt-get update && apt-get install -y \
    python3-pip \
    libopencv-dev \
    python3-opencv

COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt

COPY . /app
WORKDIR /app

CMD ["python3", "edge_processor.py"]
