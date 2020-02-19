docker build --build-arg --build-arg BUILD_TIME=$(date +%s) . -t aiminders/codelab:py
# 重新 build
# docker build --no-cache  --build-arg --build-arg BUILD_TIME=$(date +%s) . -t aiminders/codelab:py
