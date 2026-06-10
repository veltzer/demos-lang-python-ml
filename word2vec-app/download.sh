#!/bin/bash
# Download mid-range (100-dimensional) GloVe word embeddings.
#
# GloVe 6B was trained on Wikipedia 2014 + Gigaword 5 (6 billion tokens,
# 400k vocabulary). The single zip ships 50/100/200/300d variants; we keep
# only the 100d file (~347MB unpacked) and discard the rest.
set -euo pipefail
cd "$(dirname "$0")"

ZIP=glove.6B.zip
WANT=glove.6B.100d.txt
# HuggingFace mirror — same file as Stanford's, but its CDN is far faster.
URL=https://huggingface.co/stanfordnlp/glove/resolve/main/glove.6B.zip

if [[ -f "$WANT" ]]; then
    echo "$WANT already present, nothing to do."
    exit 0
fi

if [[ ! -f "$ZIP" ]]; then
    echo "Downloading $URL (~822 MB) ..."
    curl -L -o "$ZIP" "$URL"
fi

echo "Extracting $WANT ..."
unzip -o "$ZIP" "$WANT"
rm -f "$ZIP"
echo "Done: $(du -h "$WANT" | cut -f1) $WANT"
