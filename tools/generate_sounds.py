"""Create the small, original sound effects used by Heart Hop.

Run with: python tools/generate_sounds.py
The output is plain 16-bit PCM WAV, which Godot imports without extra plugins.
"""

from __future__ import annotations

import math
import struct
import wave
from pathlib import Path


SAMPLE_RATE = 44_100
OUTPUT_DIR = Path(__file__).resolve().parents[1] / "audio"


def new_buffer(seconds: float) -> list[float]:
    return [0.0] * round(seconds * SAMPLE_RATE)


def add_tone(
    samples: list[float],
    *,
    start: float,
    length: float,
    pitch: float,
    end_pitch: float | None = None,
    volume: float = 0.35,
    brightness: float = 0.18,
    attack: float = 0.008,
    release: float = 0.09,
) -> None:
    """Mix a rounded, lightly retro tone into a sound buffer."""
    first = round(start * SAMPLE_RATE)
    count = round(length * SAMPLE_RATE)
    phase = 0.0
    last_pitch = end_pitch if end_pitch is not None else pitch

    for index in range(count):
        destination = first + index
        if destination >= len(samples):
            break

        progress = index / max(count - 1, 1)
        frequency = pitch * (last_pitch / pitch) ** progress
        phase += 2.0 * math.pi * frequency / SAMPLE_RATE

        age = index / SAMPLE_RATE
        remaining = (count - index) / SAMPLE_RATE
        envelope = min(1.0, age / attack, remaining / release)
        envelope = max(0.0, envelope) ** 1.25

        tone = (
            math.sin(phase) * (1.0 - brightness)
            + math.sin(phase * 2.0) * brightness * 0.72
            + math.sin(phase * 3.0) * brightness * 0.18
        )
        samples[destination] += tone * envelope * volume


def save(name: str, samples: list[float]) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    peak = max(abs(sample) for sample in samples)
    gain = min(1.0, 0.86 / peak) if peak else 1.0
    data = bytearray()
    for sample in samples:
        value = round(max(-1.0, min(1.0, sample * gain)) * 32_767)
        data.extend(struct.pack("<h", value))

    with wave.open(str(OUTPUT_DIR / name), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(SAMPLE_RATE)
        output.writeframes(data)


def make_jump() -> None:
    samples = new_buffer(0.26)
    add_tone(samples, start=0.0, length=0.21, pitch=390, end_pitch=710,
             volume=0.42, brightness=0.23, release=0.075)
    add_tone(samples, start=0.035, length=0.19, pitch=585, end_pitch=925,
             volume=0.11, brightness=0.08, release=0.11)
    save("jump.wav", samples)


def make_heart() -> None:
    samples = new_buffer(0.47)
    add_tone(samples, start=0.0, length=0.22, pitch=784,
             volume=0.31, brightness=0.12, release=0.16)
    add_tone(samples, start=0.11, length=0.3, pitch=1174.66,
             volume=0.34, brightness=0.10, release=0.22)
    add_tone(samples, start=0.13, length=0.27, pitch=1760,
             volume=0.08, brightness=0.0, release=0.24)
    save("heart.wav", samples)


def make_hit() -> None:
    samples = new_buffer(0.38)
    add_tone(samples, start=0.0, length=0.34, pitch=370, end_pitch=155,
             volume=0.38, brightness=0.23, release=0.16)
    add_tone(samples, start=0.025, length=0.25, pitch=250, end_pitch=115,
             volume=0.18, brightness=0.04, release=0.12)
    save("hit.wav", samples)


def make_win() -> None:
    samples = new_buffer(1.45)
    notes = [523.25, 659.25, 783.99, 1046.5]
    for index, pitch in enumerate(notes):
        start = index * 0.19
        length = 0.33 if index < 3 else 0.67
        add_tone(samples, start=start, length=length, pitch=pitch,
                 volume=0.29, brightness=0.16, release=0.18 if index < 3 else 0.46)
        add_tone(samples, start=start + 0.02, length=length, pitch=pitch * 2,
                 volume=0.055, brightness=0.0, release=0.2 if index < 3 else 0.5)
    add_tone(samples, start=0.76, length=0.62, pitch=783.99,
             volume=0.15, brightness=0.05, release=0.46)
    save("win.wav", samples)


if __name__ == "__main__":
    make_jump()
    make_heart()
    make_hit()
    make_win()
    print(f"Wrote four sounds to {OUTPUT_DIR}")
