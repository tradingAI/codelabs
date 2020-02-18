# https://github.com/iminders/services/blob/master/docker-images/aiminders/bazel/latest.Dockerfile
FROM aiminders/library:bazel.latest

ENV CODE_DIR /root/codelabs

ARG BUILD_DATE
ENV BUILD_DATE=${BUILD_DATE}
COPY . $CODE_DIR/pylab
RUN cd $CODE_DIR/pylab && rm -rf __pycache__ && \
    find . -name "*.pyc" -delete && \
    pip install -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com -r requirements.txt && \
    pip install -e .
RUN rm -rf /root/.cache/pip \
    && find / -type d -name __pycache__ -exec rm -r {} \+



CMD /bin/bash
