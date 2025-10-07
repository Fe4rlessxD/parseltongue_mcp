# Setup Guide for Parseltongue MCP Server

## Quick Start

### 1. Install Dependencies

```bash
cd /path/to/parseltongue_mcp
uv sync
```

### 2. Test the Server

```bash
# Run examples to verify everything works
uv run python examples.py

# Or test individual tools
uv run python -c "from main import encode_morse; print(encode_morse('HELLO'))"
```

### 3. Configure Claude Desktop

Edit your Claude Desktop configuration file:

**Location:**

- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/Claude/claude_desktop_config.json`

**Add this configuration:**

```json
{
  "mcpServers": {
    "parseltongue": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/parseltongue_mcp",
        "run",
        "python",
        "main.py"
      ]
    }
  }
}
```

**If you already have other MCP servers configured**, add the `parseltongue` entry to the existing `mcpServers` object:

```json
{
  "mcpServers": {
    "existing-server": {
      "command": "...",
      "args": ["..."]
    },
    "parseltongue": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/parseltongue_mcp",
        "run",
        "python",
        "main.py"
      ]
    }
  }
}
```

### 4. Restart Claude Desktop

After saving the configuration, completely quit and restart Claude Desktop for the changes to take effect.

### 5. Verify in Claude

Once restarted, you can test the tools in Claude:

**Try asking:**

- "Encode 'Hello World' to Base64"
- "Convert 'HELP' to Morse code"
- "Create bubble text for 'Welcome'"
- "Hide 'secret' using zero-width encoding"
- "Apply Zalgo effect to 'Chaos' with high intensity"

## Available Tools (30+)

### Basic Encodings

- `encode_base64`, `decode_base64`
- `encode_base32`, `decode_base32`
- `encode_hex`, `decode_hex`
- `encode_binary`, `decode_binary`
- `encode_url`, `decode_url`
- `encode_html_entities`, `decode_html_entities`

### Ciphers

- `encode_rot13`
- `encode_caesar`, `decode_caesar` (with custom shift)
- `encode_atbash`
- `encode_morse`, `decode_morse`

### Unicode Transformations

- `encode_zalgo` (with intensity: low/medium/high)
- `encode_upside_down`
- `encode_bubble_text`
- `encode_fullwidth`
- `encode_strikethrough`
- `encode_underline`

### Steganography

- `encode_zero_width`, `decode_zero_width`
- `encode_invisible_ink`

### Utilities

- `reverse_text`
- `encode_pig_latin`

## Troubleshooting

### MCP Server Not Appearing in Claude

1. **Check configuration path**: Make sure the path in your config points to the correct directory
2. **Verify JSON syntax**: Use a JSON validator to ensure your config file is valid
3. **Check logs**: Look for errors in Claude Desktop's logs
4. **Restart completely**: Quit Claude Desktop entirely (not just close the window)

### Import Errors

```bash
# Reinstall dependencies
cd /path/to/parseltongue_mcp
uv sync --reinstall
```

### Testing Without Claude

```bash
# Use MCP Inspector to test the server
npx @modelcontextprotocol/inspector uv --directory /path/to/parseltongue_mcp run python main.py
```

## Advanced Usage

### Running Server Directly

```bash
# Start the server in stdio mode (for MCP communication)
uv run python main.py
```

### Using as a Python Library

```python
from main import encode_base64, encode_morse, encode_zalgo

# Use the functions directly
encoded = encode_base64("Hello World")
morse = encode_morse("SOS")
glitchy = encode_zalgo("Text", intensity="high")
```

## Examples

See `examples.py` for comprehensive usage examples:

```bash
uv run python examples.py
```

## Support

For issues or questions:

1. Check the README.md for detailed documentation
2. Review the examples.py file for usage patterns
3. Test tools individually before using in Claude

---

**Happy encoding!** 🐍
