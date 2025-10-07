#!/usr/bin/env python3
"""
Examples of using the Parseltongue encoding tools.
Run: uv run python examples.py
"""

from main import (
    encode_base64, decode_base64,
    encode_morse, decode_morse,
    encode_rot13,
    encode_caesar, decode_caesar,
    encode_zalgo,
    encode_bubble_text,
    encode_upside_down,
    encode_zero_width, decode_zero_width,
    reverse_text,
)

def demo_basic_encodings():
    print("=" * 60)
    print("BASIC ENCODINGS")
    print("=" * 60)
    
    text = "Hello World"
    print(f"\nOriginal: {text}")
    
    encoded = encode_base64(text)
    print(f"Base64: {encoded}")
    print(f"Decoded: {decode_base64(encoded)}")
    
    encoded = encode_morse(text)
    print(f"\nMorse: {encoded}")
    print(f"Decoded: {decode_morse(encoded)}")


def demo_ciphers():
    print("\n" + "=" * 60)
    print("CIPHERS")
    print("=" * 60)
    
    text = "Secret Message"
    print(f"\nOriginal: {text}")
    
    encoded = encode_rot13(text)
    print(f"ROT13: {encoded}")
    print(f"ROT13 again (decode): {encode_rot13(encoded)}")
    
    encoded = encode_caesar(text, shift=5)
    print(f"\nCaesar (shift 5): {encoded}")
    print(f"Decoded: {decode_caesar(encoded, shift=5)}")


def demo_unicode_styles():
    print("\n" + "=" * 60)
    print("UNICODE STYLES")
    print("=" * 60)
    
    text = "Awesome"
    print(f"\nOriginal: {text}")
    print(f"Bubble: {encode_bubble_text(text)}")
    print(f"Upside Down: {encode_upside_down(text)}")
    print(f"Zalgo (low): {encode_zalgo(text, 'low')}")
    print(f"Zalgo (high): {encode_zalgo(text, 'high')}")


def demo_steganography():
    print("\n" + "=" * 60)
    print("STEGANOGRAPHY (HIDDEN TEXT)")
    print("=" * 60)
    
    secret = "TOP SECRET"
    print(f"\nSecret message: {secret}")
    
    # Encode to zero-width (invisible)
    hidden = encode_zero_width(secret)
    print(f"Hidden encoding length: {len(hidden)} characters (appears invisible)")
    
    # Add to visible text
    visible_text = f"This is a normal message{hidden}"
    print(f"\nVisible text: {visible_text[:30]}...")
    print(f"Contains hidden message: {len(hidden) > 0}")
    
    # Extract the hidden part and decode
    extracted = visible_text[25:]  # Everything after the visible message
    decoded = decode_zero_width(extracted)
    print(f"Decoded secret: {decoded}")


def demo_utilities():
    print("\n" + "=" * 60)
    print("UTILITIES")
    print("=" * 60)
    
    text = "racecar"
    print(f"\nOriginal: {text}")
    reversed_text = reverse_text(text)
    print(f"Reversed: {reversed_text}")
    print(f"Is palindrome: {text == reversed_text}")


if __name__ == "__main__":
    print("\n🐍 PARSELTONGUE MCP SERVER - EXAMPLES 🐍\n")
    
    demo_basic_encodings()
    demo_ciphers()
    demo_unicode_styles()
    demo_steganography()
    demo_utilities()
    
    print("\n" + "=" * 60)
    print("✓ All examples completed!")
    print("=" * 60)
    print("\nTo use as MCP server, add to your Claude Desktop config:")
    print('See README.md for configuration instructions.')
    print()
