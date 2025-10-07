"""
Parseltongue MCP Server
Text encoding and transformation tools inspired by P4RS3LT0NGV3
"""

import base64
import base58
import base62
import base45
import binascii
import urllib.parse
import html
from typing import Any
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("parseltongue")


# ============================================================================
# BASIC ENCODINGS
# ============================================================================

@mcp.tool()
def encode_base64(text: str) -> str:
    """
    Encode text to Base64 format.
    
    Args:
        text: The text to encode
        
    Returns:
        Base64 encoded string
    """
    return base64.b64encode(text.encode('utf-8')).decode('ascii')


@mcp.tool()
def decode_base64(encoded_text: str) -> str:
    """
    Decode Base64 encoded text.
    
    Args:
        encoded_text: The Base64 encoded text
        
    Returns:
        Decoded string
    """
    try:
        return base64.b64decode(encoded_text.encode('ascii')).decode('utf-8')
    except Exception as e:
        return f"Error decoding: {str(e)}"


@mcp.tool()
def encode_base32(text: str) -> str:
    """
    Encode text to Base32 format.
    
    Args:
        text: The text to encode
        
    Returns:
        Base32 encoded string
    """
    return base64.b32encode(text.encode('utf-8')).decode('ascii')


@mcp.tool()
def decode_base32(encoded_text: str) -> str:
    """
    Decode Base32 encoded text.
    
    Args:
        encoded_text: The Base32 encoded text
        
    Returns:
        Decoded string
    """
    try:
        return base64.b32decode(encoded_text.encode('ascii')).decode('utf-8')
    except Exception as e:
        return f"Error decoding: {str(e)}"


@mcp.tool()
def encode_hex(text: str) -> str:
    """
    Encode text to hexadecimal format.
    
    Args:
        text: The text to encode
        
    Returns:
        Hex encoded string
    """
    return binascii.hexlify(text.encode('utf-8')).decode('ascii')


@mcp.tool()
def decode_hex(encoded_text: str) -> str:
    """
    Decode hexadecimal encoded text.
    
    Args:
        encoded_text: The hex encoded text
        
    Returns:
        Decoded string
    """
    try:
        return binascii.unhexlify(encoded_text.encode('ascii')).decode('utf-8')
    except Exception as e:
        return f"Error decoding: {str(e)}"


@mcp.tool()
def encode_binary(text: str) -> str:
    """
    Encode text to binary format (8-bit).
    
    Args:
        text: The text to encode
        
    Returns:
        Binary string representation
    """
    return ' '.join(format(ord(char), '08b') for char in text)


@mcp.tool()
def decode_binary(encoded_text: str) -> str:
    """
    Decode binary encoded text.
    
    Args:
        encoded_text: The binary encoded text (space or comma separated)
        
    Returns:
        Decoded string
    """
    try:
        # Remove spaces and split into 8-bit chunks
        binary_str = encoded_text.replace(' ', '').replace(',', '')
        chars = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
        return ''.join(chr(int(char, 2)) for char in chars if char)
    except Exception as e:
        return f"Error decoding: {str(e)}"


@mcp.tool()
def encode_url(text: str) -> str:
    """
    URL encode text (percent encoding).
    
    Args:
        text: The text to encode
        
    Returns:
        URL encoded string
    """
    return urllib.parse.quote(text)


@mcp.tool()
def decode_url(encoded_text: str) -> str:
    """
    Decode URL encoded text.
    
    Args:
        encoded_text: The URL encoded text
        
    Returns:
        Decoded string
    """
    return urllib.parse.unquote(encoded_text)


@mcp.tool()
def encode_html_entities(text: str) -> str:
    """
    Encode text to HTML entities.
    
    Args:
        text: The text to encode
        
    Returns:
        HTML entity encoded string
    """
    return html.escape(text)


@mcp.tool()
def decode_html_entities(encoded_text: str) -> str:
    """
    Decode HTML entities.
    
    Args:
        encoded_text: The HTML entity encoded text
        
    Returns:
        Decoded string
    """
    return html.unescape(encoded_text)

@mcp.tool()
def encode_ascii85(text: str) -> str:
    """
    Encode text to ASCII85 format.
    
    Args:
        text: The text to encode
    """
    return base64.a85encode(text.encode('utf-8')).decode('ascii')
    
@mcp.tool()
def decode_ascii85(encoded_text: str) -> str:
    """
    Decode ASCII85 encoded text.
    """
    return base64.a85decode(encoded_text.encode('ascii')).decode('utf-8')
    
@mcp.tool()
def encode_base58(text: str) -> str:
    """
    Encode text to Base58 format.
    """
    return base58.b58encode(text.encode('utf-8')).decode('ascii')
    
@mcp.tool()
def decode_base58(encoded_text: str) -> str:
    """
    Decode Base58 encoded text.
    """
    return base58.b58decode(encoded_text.encode('ascii')).decode('utf-8')

@mcp.tool()
def encode_base64url(text: str) -> str:
    """
    Encode text to Base64 URL format.
    """
    return base64.urlsafe_b64encode(text.encode('utf-8')).decode('ascii')
    
@mcp.tool()
def decode_base64url(encoded_text: str) -> str:
    """
    Decode Base64 URL encoded text.
    """
    return base64.urlsafe_b64decode(encoded_text.encode('ascii')).decode('utf-8')

@mcp.tool()
def encode_base62(text: str) -> str:
    """
    Encode text to Base62 format.
    """
    # Convert text to bytes, then to int, then encode
    data = text.encode('utf-8')
    num = int.from_bytes(data, byteorder='big')
    return base62.encode(num)
    
@mcp.tool()
def decode_base62(encoded_text: str) -> str:
    """
    Decode Base62 encoded text.
    """
    # Decode to int, then to bytes, then to text
    num = base62.decode(encoded_text)
    # Calculate byte length needed
    byte_length = (num.bit_length() + 7) // 8
    data = num.to_bytes(byte_length, byteorder='big')
    return data.decode('utf-8')
    
@mcp.tool()
def encode_base45(text: str) -> str:
    """
    Encode text to Base45 format.
    """
    return base45.b45encode(text.encode('utf-8')).decode('ascii')
    
@mcp.tool()
def decode_base45(encoded_text: str) -> str:
    """
    Decode Base45 encoded text.
    """
    return base45.b45decode(encoded_text.encode('ascii')).decode('utf-8')
    


# ============================================================================
# CIPHERS
# ============================================================================

@mcp.tool()
def encode_rot13(text: str) -> str:
    """
    Encode text using ROT13 cipher (Caesar cipher with shift of 13).
    
    Args:
        text: The text to encode
        
    Returns:
        ROT13 encoded string
    """
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + 13) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + 13) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)

@mcp.tool()
def decode_rot13(text: str) -> str:
    """
    Decode text using ROT13 cipher (Caesar cipher with shift of 13).
    """
    return encode_rot13(text)



@mcp.tool()
def encode_caesar(text: str, shift: int = 3) -> str:
    """
    Encode text using Caesar cipher with custom shift.
    
    Args:
        text: The text to encode
        shift: Number of positions to shift (default: 3)
        
    Returns:
        Caesar cipher encoded string
    """
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr((ord(char) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= char <= 'Z':
            result.append(chr((ord(char) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(char)
    return ''.join(result)


@mcp.tool()
def decode_caesar(text: str, shift: int = 3) -> str:
    """
    Decode Caesar cipher with known shift.
    
    Args:
        text: The encoded text
        shift: Number of positions used to shift (default: 3)
        
    Returns:
        Decoded string
    """
    return encode_caesar(text, -shift)


@mcp.tool()
def encode_atbash(text: str) -> str:
    """
    Encode text using Atbash cipher (reverse alphabet substitution).
    
    Args:
        text: The text to encode
        
    Returns:
        Atbash cipher encoded string
    """
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr(ord('z') - (ord(char) - ord('a'))))
        elif 'A' <= char <= 'Z':
            result.append(chr(ord('Z') - (ord(char) - ord('A'))))
        else:
            result.append(char)
    return ''.join(result)

@mcp.tool()
def decode_atbash(text: str) -> str:
    """
    Decode Atbash cipher.
    """
    return encode_atbash(text)


@mcp.tool()
def encode_morse(text: str) -> str:
    """
    Encode text to Morse code.
    
    Args:
        text: The text to encode
        
    Returns:
        Morse code string
    """
    morse_map = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
        '8': '---..', '9': '----.', ' ': '/'
    }
    return ' '.join(morse_map.get(char.upper(), char) for char in text)


@mcp.tool()
def decode_morse(encoded_text: str) -> str:
    """
    Decode Morse code to text.
    
    Args:
        encoded_text: The Morse code (space separated)
        
    Returns:
        Decoded string
    """
    morse_reverse = {
        '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
        '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
        '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
        '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
        '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2',
        '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7',
        '---..': '8', '----.': '9', '/': ' '
    }
    try:
        return ''.join(morse_reverse.get(code, '?') for code in encoded_text.split(' '))
    except Exception as e:
        return f"Error decoding: {str(e)}"


# ============================================================================
# UNICODE TRANSFORMATIONS
# ============================================================================

@mcp.tool()
def encode_zalgo(text: str, intensity: str = "medium") -> str:
    """
    Add Zalgo/glitch effect to text using combining diacritical marks.
    
    Args:
        text: The text to transform
        intensity: Effect intensity - "low", "medium", or "high" (default: "medium")
        
    Returns:
        Zalgo-ified text
    """
    combining_marks_up = [
        '\u0300', '\u0301', '\u0302', '\u0303', '\u0304', '\u0305', '\u0306',
        '\u0307', '\u0308', '\u0309', '\u030A', '\u030B', '\u030C', '\u030D',
        '\u030E', '\u030F', '\u0310', '\u0311', '\u0312', '\u0313', '\u0314'
    ]
    combining_marks_down = [
        '\u0316', '\u0317', '\u0318', '\u0319', '\u031A', '\u031B', '\u031C',
        '\u031D', '\u031E', '\u031F', '\u0320', '\u0321', '\u0322', '\u0323',
        '\u0324', '\u0325', '\u0326', '\u0327', '\u0328', '\u0329', '\u032A'
    ]
    
    intensity_map = {"low": 1, "medium": 3, "high": 6}
    num_marks = intensity_map.get(intensity.lower(), 3)
    
    import random
    result = []
    for char in text:
        result.append(char)
        if char.strip():  # Don't add marks to whitespace
            for _ in range(random.randint(0, num_marks)):
                result.append(random.choice(combining_marks_up))
            for _ in range(random.randint(0, num_marks)):
                result.append(random.choice(combining_marks_down))
    return ''.join(result)


@mcp.tool()
def encode_upside_down(text: str) -> str:
    """
    Flip text upside down using Unicode characters.
    
    Args:
        text: The text to flip
        
    Returns:
        Upside down text
    """
    upside_down_map = {
        'a': '\u0250', 'b': 'q', 'c': '\u0254', 'd': 'p', 'e': '\u01DD',
        'f': '\u025F', 'g': '\u0183', 'h': '\u0265', 'i': '\u1D09',
        'j': '\u027E', 'k': '\u029E', 'l': '\u05DF', 'm': '\u026F',
        'n': 'u', 'o': 'o', 'p': 'd', 'q': 'b', 'r': '\u0279',
        's': 's', 't': '\u0287', 'u': 'n', 'v': '\u028C', 'w': '\u028D',
        'x': 'x', 'y': '\u028E', 'z': 'z',
        'A': '\u2200', 'B': 'q', 'C': '\u0186', 'D': 'p', 'E': '\u018E',
        'F': '\u2132', 'G': '\u05E4', 'H': 'H', 'I': 'I', 'J': '\u017F',
        'K': '\u029E', 'L': '\u02E5', 'M': 'W', 'N': 'N', 'O': 'O',
        'P': '\u0500', 'Q': 'b', 'R': '\u1D1A', 'S': 'S', 'T': '\u22A5',
        'U': '\u2229', 'V': '\u039B', 'W': 'M', 'X': 'X', 'Y': '\u2144',
        'Z': 'Z',
        '0': '0', '1': '\u0196', '2': '\u1105', '3': '\u0190', '4': '\u3123',
        '5': '\u03DB', '6': '9', '7': '\u3125', '8': '8', '9': '6',
        '.': '\u02D9', ',': '\'', '!': '\u00A1', '?': '\u00BF', ' ': ' '
    }
    return ''.join(upside_down_map.get(char, char) for char in reversed(text))


@mcp.tool()
def encode_bubble_text(text: str) -> str:
    """
    Enclose letters in circles (bubble text).
    
    Args:
        text: The text to transform
        
    Returns:
        Bubble text
    """
    # Circled letters start at U+24B6 for uppercase, U+24D0 for lowercase
    result = []
    for char in text:
        if 'A' <= char <= 'Z':
            result.append(chr(0x24B6 + ord(char) - ord('A')))
        elif 'a' <= char <= 'z':
            result.append(chr(0x24D0 + ord(char) - ord('a')))
        elif '0' <= char <= '9':
            result.append(chr(0x245F + ord(char) - ord('0') + 1))
        else:
            result.append(char)
    return ''.join(result)


@mcp.tool()
def encode_fullwidth(text: str) -> str:
    """
    Convert to full-width Unicode characters (aesthetic/vaporwave style).
    
    Args:
        text: The text to transform
        
    Returns:
        Full-width text
    """
    result = []
    for char in text:
        if '\u0021' <= char <= '\u007E':
            # Convert ASCII printable to fullwidth
            result.append(chr(ord(char) + 0xFEE0))
        else:
            result.append(char)
    return ''.join(result)


@mcp.tool()
def encode_strikethrough(text: str) -> str:
    """
    Add strikethrough to text using combining characters.
    
    Args:
        text: The text to strike through
        
    Returns:
        Strikethrough text
    """
    return ''.join(char + '\u0336' for char in text)


@mcp.tool()
def encode_underline(text: str) -> str:
    """
    Add underline to text using combining characters.
    
    Args:
        text: The text to underline
        
    Returns:
        Underlined text
    """
    return ''.join(char + '\u0332' for char in text)


# ============================================================================
# STEGANOGRAPHY
# ============================================================================

@mcp.tool()
def encode_zero_width(text: str) -> str:
    """
    Hide text using zero-width Unicode characters (steganography).
    The text becomes invisible but can be decoded.
    
    Args:
        text: The text to hide
        
    Returns:
        Zero-width encoded text (appears invisible)
    """
    # Use zero-width characters to represent binary
    zwj = '\u200D'  # Zero Width Joiner (represents 1)
    zwnj = '\u200C'  # Zero Width Non-Joiner (represents 0)
    zwsp = '\u200B'  # Zero Width Space (separator)
    
    result = []
    for char in text:
        binary = format(ord(char), '016b')  # 16-bit representation
        for bit in binary:
            result.append(zwj if bit == '1' else zwnj)
        result.append(zwsp)  # Separator between characters
    
    return ''.join(result)


@mcp.tool()
def decode_zero_width(encoded_text: str) -> str:
    """
    Decode zero-width encoded text.
    
    Args:
        encoded_text: The zero-width encoded text
        
    Returns:
        Decoded visible text
    """
    zwj = '\u200D'
    zwnj = '\u200C'
    zwsp = '\u200B'
    
    try:
        chars = encoded_text.split(zwsp)
        result = []
        for char_code in chars:
            if not char_code:
                continue
            binary = ''.join('1' if c == zwj else '0' for c in char_code)
            if binary:
                result.append(chr(int(binary, 2)))
        return ''.join(result)
    except Exception as e:
        return f"Error decoding: {str(e)}"


@mcp.tool()
def encode_invisible_ink(text: str, cover_text: str = "Read between the lines") -> str:
    """
    Hide text within cover text using Unicode variation selectors.
    
    Args:
        text: The text to hide
        cover_text: The visible cover text (default: "Read between the lines")
        
    Returns:
        Cover text with hidden message
    """
    # Use variation selectors to encode hidden text
    vs15 = '\uFE0E'  # Text style variation selector
    vs16 = '\uFE0F'  # Emoji style variation selector
    
    hidden_binary = ''.join(format(ord(c), '08b') for c in text)
    
    result = []
    bit_index = 0
    for char in cover_text:
        result.append(char)
        if bit_index < len(hidden_binary):
            result.append(vs16 if hidden_binary[bit_index] == '1' else vs15)
            bit_index += 1
    
    return ''.join(result)


# ============================================================================
# UTILITY
# ============================================================================

@mcp.tool()
def reverse_text(text: str) -> str:
    """
    Simply reverse the text string.
    
    Args:
        text: The text to reverse
        
    Returns:
        Reversed text
    """
    return text[::-1]


@mcp.tool()
def encode_pig_latin(text: str) -> str:
    """
    Encode text to Pig Latin.
    
    Args:
        text: The text to encode
        
    Returns:
        Pig Latin encoded text
    """
    def convert_word(word):
        if not word:
            return word
        
        vowels = 'aeiouAEIOU'
        if word[0] in vowels:
            return word + 'way'
        
        # Find first vowel
        for i, char in enumerate(word):
            if char in vowels:
                return word[i:] + word[:i] + 'ay'
        return word + 'ay'
    
    words = text.split()
    return ' '.join(convert_word(word) for word in words)


if __name__ == "__main__":
    mcp.run()
