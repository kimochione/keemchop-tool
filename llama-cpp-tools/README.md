# llama.cpp Quantize Tools

 2026-06-17 05:59:55

## Binary Tools (bin/)

| Tool | Size |
|------|------|
| `llama-quantize` | 17,896 bytes |

## Scripts (scripts/)

| Script | Size |
|--------|------|
| `convert_hf_to_gguf.py` | 12,592 bytes |
| `convert_llama_ggml_to_gguf.py` | 19,112 bytes |

## Quick Restore

```bash
# Download restore script
wget https://raw.githubusercontent.com/kimochione/keemchop-tool/main/llama-cpp-tools/restore.py

# Run it
python restore.py
```

## Usage

```bash
# Quantize a model
./bin/llama-quantize model.gguf Q4_K_M

# Convert HuggingFace to GGUF
python scripts/convert_hf_to_gguf.py /path/to/model
```
