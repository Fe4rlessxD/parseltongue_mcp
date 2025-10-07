# Parseltongue MCP Server 🐍

A Model Context Protocol (MCP) server providing 40+ text encoding, cipher, and transformation tools inspired by [P4RS3LT0NGV3](https://github.com/elder-plinius/P4RS3LT0NGV3).

## Features

### 📦 Basic Encodings (22 tools)

- **Base64**: Encode/decode Base64
- **Base64URL**: Encode/decode Base64 URL-safe format
- **Base32**: Encode/decode Base32
- **Base58**: Encode/decode Base58 (Bitcoin-style)
- **Base62**: Encode/decode Base62
- **Base45**: Encode/decode Base45
- **ASCII85**: Encode/decode ASCII85
- **Hexadecimal**: Encode/decode hex
- **Binary**: Encode/decode 8-bit binary
- **URL Encoding**: Percent encoding for URLs
- **HTML Entities**: Encode/decode HTML entities

### 🔐 Ciphers (8 tools)

- **ROT13**: Classic rotation cipher (encode/decode)
- **Caesar Cipher**: Custom shift cipher (encode/decode)
- **Atbash**: Reverse alphabet substitution (encode/decode)
- **Morse Code**: Encode/decode to Morse code

### 🎨 Unicode Transformations (6 tools)

- **Zalgo Text**: Glitch effect with combining marks
- **Upside Down**: Flip text using Unicode
- **Bubble Text**: Circle-enclosed letters (Ⓐⓑⓒ)
- **Full Width**: Vaporwave aesthetic (ｆｕｌｌ　ｗｉｄｔｈ)
- **Strikethrough**: S̶t̶r̶i̶k̶e̶t̶h̶r̶o̶u̶g̶h̶
- **Underline**: U̲n̲d̲e̲r̲l̲i̲n̲e̲d̲

### 🕵️ Steganography (3 tools)

- **Zero-Width Encoding**: Hide text using invisible Unicode characters (encode/decode)
- **Invisible Ink**: Hide messages within cover text

### 🔧 Utilities (2 tools)

- **Reverse Text**: Simple string reversal
- **Pig Latin**: Classic word game transformation

## Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd parseltongue_mcp

# Install dependencies using uv
uv sync

# Or using pip
pip install -e .
```

## Usage

### As an MCP Server

Add to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "parseltongue": {
      "command": "uv",
      "args": [
        "--directory",
        "(Full path)/parseltongue_mcp",
        "run",
        "parseltongue-mcp"
      ]
    }
  }
}
```

### Running Directly

```bash
# Using uv
uv run parseltongue-mcp

# Or with python
python main.py
```

## Available Tools

### Encoding Examples

```python
# Base64
encode_base64(text="Hello World")
# Returns: "SGVsbG8gV29ybGQ="

# Base64URL (URL-safe)
encode_base64url(text="Hello World")
# Returns: "SGVsbG8gV29ybGQ="

# Base58 (Bitcoin-style)
encode_base58(text="Hello")
# Returns: "9Ajdvzr"

# Base62
encode_base62(text="Hello")
# Returns: "5TP3P3v"

# Base45
encode_base45(text="Hello")
# Returns: "JBSWY3DP"

# ASCII85
encode_ascii85(text="Hello")
# Returns: "87cURD]i"

# Morse Code
encode_morse(text="SOS")
# Returns: "... --- ..."

# Binary
encode_binary(text="Hi")
# Returns: "01001000 01101001"

# Hexadecimal
encode_hex(text="Hi")
# Returns: "4869"

# Zero-Width (Steganography)
encode_zero_width(text="secret")
# Returns invisible Unicode characters
```

### Cipher Examples

```python
# ROT13
encode_rot13(text="Hello World")
# Returns: "Uryyb Jbeyq"

# Caesar Cipher with custom shift
encode_caesar(text="Attack at dawn", shift=5)
# Returns: "Fyyfhp fy ifbs"

# Atbash
encode_atbash(text="SECRET")
# Returns: "HVXIVG"
```

### Unicode Transformation Examples

```python
# Zalgo Text
encode_zalgo(text="Chaos", intensity="high")
# Returns: C̴̢̛͇̽h̵͎̓a̸̰͊ö̶́̚s̸̰̈

# Upside Down
encode_upside_down(text="Hello")
# Returns: "olləH"

# Bubble Text
encode_bubble_text(text="Hello")
# Returns: "Ⓗⓔⓛⓛⓞ"

# Full Width
encode_fullwidth(text="Wave")
# Returns: "Ｗａｖｅ"

# Strikethrough
encode_strikethrough(text="Cancelled")
# Returns: "C̶a̶n̶c̶e̶l̶l̶e̶d̶"

# Underline
encode_underline(text="Important")
# Returns: "I̲m̲p̲o̲r̲t̲a̲n̲t̲"
```

## Tool Categories

All tools are exposed as MCP tools with detailed descriptions and type hints:

| Category                | Count | Examples                                                         |
| ----------------------- | ----- | ---------------------------------------------------------------- |
| Basic Encodings         | 22    | Base64, Base58, Base62, Base45, ASCII85, Hex, Binary, URL        |
| Ciphers                 | 8     | ROT13, Caesar, Atbash, Morse                                     |
| Unicode Transformations | 6     | Zalgo, Upside Down, Bubble, Full Width, Strikethrough, Underline |
| Steganography           | 3     | Zero-Width, Invisible Ink                                        |
| Utilities               | 2     | Reverse, Pig Latin                                               |

## Development

```bash
# Install development dependencies
uv sync

# Run the server in development mode
uv run python main.py

# Test with MCP inspector
npx @modelcontextprotocol/inspector uv run python main.py
```

## Technical Details

- **Framework**: FastMCP (MCP Python SDK)
- **Python Version**: 3.12+
- **Dependencies**:
  - `mcp[cli]>=1.16.0` - MCP server framework
  - `httpx>=0.28.1` - HTTP client (for potential future features)

## Credits

Inspired by [P4RS3LT0NGV3](https://github.com/elder-plinius/P4RS3LT0NGV3) by elder-plinius.

## License

Open source. See LICENSE file for details.

## Contributing

Contributions welcome! Areas to expand:

- More cipher algorithms (Vigenère, Rail Fence, Playfair)
- Fantasy language encodings (Elvish, Klingon, etc.)
- Ancient scripts (Runes, Hieroglyphics)
- Additional Unicode styles
- Batch encoding/decoding operations

## Examples in Action

### Hiding Messages

```python
# Create invisible message
hidden = encode_zero_width(text="TOP SECRET")
visible = f"This is a normal message{hidden}"
# Looks like: "This is a normal message"
# But contains hidden text!

# Decode it
decode_zero_width(encoded_text=hidden)
# Returns: "TOP SECRET"
```

### Text Styling

```python
# Create stylized text for social media
normal = "AWESOME"
bubble = encode_bubble_text(text=normal)      # ⒶⓌⒺⓈⓄⓂⒺ
wide = encode_fullwidth(text=normal)          # ＡＷＥＳＯＭＥ
zalgo = encode_zalgo(text=normal)             # A̴W̸E̵S̶O̴M̵E̸
strike = encode_strikethrough(text=normal)    # A̶W̶E̶S̶O̶M̶E̶
underline = encode_underline(text=normal)     # A̲W̲E̲S̲O̲M̲E̲
upside = encode_upside_down(text=normal)      # ƎWOSƎפ∀
```

### Classic Ciphers

```python
# Encode a message with Caesar cipher
message = "Meet at the park"
encoded = encode_caesar(text=message, shift=7)
# Returns: "Tlla ha aol whyr"

# Decode it
decode_caesar(text=encoded, shift=7)
# Returns: "Meet at the park"
```

---

Made with 🐍 and MCP
