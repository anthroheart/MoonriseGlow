#!/usr/bin/env python3

"""
MoonriseGlow video maker

Run:

    python3 make_moonrise_video.py

The script:
- Normalizes the Kling clips
- Joins them with crossfades
- Loops the animation to match the song
- Adds a title
- Adds dual-language subtitles
- Applies simple color effects
- Exports an MP4 file
- Created by: Thomas B. Sweet (Saguna Anthroness aka Aumaroo AnthroHeart Starwalker)
- License: MIT
- Date: Thursday, Sept. 17, 2026
- Source: Part of AnthroHeart Ecosystem: https://deviantart.com/anthro-shaman

"""

import glob
import math
import os
import subprocess
import sys
import tempfile


# ----------------------------- SETTINGS -----------------------------

WIDTH = 1280
HEIGHT = 720
FPS = 30

IMAGE_FILE = "Moonrise_Base_Image.png"
AUDIO_FILE = "MoonriseGlow.mp3"
LYRICS_FILE = "lyrics_moonrise.txt"
CLIP_FOLDER = "clips"
FONT_FILE = "fonts/Cinzel-SemiBold.ttf"
OUTPUT_FILE = "MoonriseGlow_Final.mp4"

CROSSFADE_SECONDS = 1.5
TITLE_SECONDS = 4.0

VIDEO_CRF = 18
VIDEO_PRESET = "veryfast"


# ----------------------------- UTILITIES -----------------------------

def run(command):
    """Run a command and stop if it fails."""
    print("$", " ".join(str(item) for item in command))

    result = subprocess.run(command, text=True)

    if result.returncode != 0:
        raise SystemExit("Command failed.")


def get_duration(filename):
    """Return the duration of a media file in seconds."""
    command = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        filename,
    ]

    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
    )

    try:
        return float(result.stdout.strip())
    except ValueError:
        return 0.0


def escape_drawtext(text):
    """Escape common characters for FFmpeg drawtext."""
    return (
        text.replace("\\", "\\\\")
        .replace(":", "\\:")
        .replace("'", "\\'")
        .replace(",", "\\,")
    )


def escape_filter_path(path):
    """Escape a path used inside an FFmpeg filter."""
    return path.replace("\\", "\\\\").replace(":", "\\:")


# ----------------------------- LYRICS -----------------------------

def read_lyrics(filename):
    """
    Read lyrics in this format:

        Chant line | English translation

    Section headings and blank lines are ignored.
    """
    lyric_pairs = []

    with open(filename, encoding="utf-8-sig") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith("[") or line.startswith("#"):
                continue

            if "|" in line:
                chant, translation = line.split("|", 1)
                chant = chant.strip()
                translation = translation.strip()
            else:
                chant = line
                translation = ""

            translation = translation.replace("(", "").replace(")", "")
            lyric_pairs.append((chant, translation))

    return lyric_pairs


def ass_time(seconds):
    """Convert seconds to ASS subtitle time format."""
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    remaining = seconds % 60

    return f"{hours}:{minutes:02d}:{remaining:05.2f}"


def create_subtitles(lyrics, song_duration, filename):
    """
    Create a simple ASS subtitle file.

    The timing is evenly distributed. For perfect timing, edit the
    subtitle timestamps manually after the first render.
    """
    if not lyrics:
        return False

    first_lyric = TITLE_SECONDS + 1.0
    last_lyric = max(song_duration - 3.0, first_lyric + 1.0)
    available_time = last_lyric - first_lyric
    slot_length = available_time / len(lyrics)

    subtitle_header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {WIDTH}
PlayResY: {HEIGHT}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Moonrise,Cinzel,44,&H00FFFFFF,&H00FFFFFF,&H90000000,&H90000000,0,0,0,0,100,100,1,0,1,2,1,2,80,80,70,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""

    events = []

    for index, (chant, translation) in enumerate(lyrics):
        start = first_lyric + index * slot_length
        end = min(start + slot_length * 0.9, song_duration - 0.25)

        if end <= start:
            continue

        text = chant

        if translation:
            text += r"\N{\fs30}" + translation

        event = (
            f"Dialogue: 0,{ass_time(start)},{ass_time(end)},"
            f"Moonrise,,0,0,0,,{{\\fad(250,250)}}{text}"
        )

        events.append(event)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(subtitle_header)
        file.write("\n".join(events))
        file.write("\n")

    return True


# ----------------------------- VIDEO PROCESSING -----------------------------

def normalize_clip(source, destination):
    """Convert a clip to the project's standard format."""
    video_filter = (
        f"scale={WIDTH}:{HEIGHT}:"
        "force_original_aspect_ratio=increase,"
        f"crop={WIDTH}:{HEIGHT}:(iw-{WIDTH})/2:(ih-{HEIGHT})/2,"
        f"fps={FPS},setsar=1,format=yuv420p"
    )

    command = [
        "ffmpeg",
        "-y",
        "-i", source,
        "-an",
        "-vf", video_filter,
        "-c:v", "libx264",
        "-preset", VIDEO_PRESET,
        "-crf", str(VIDEO_CRF),
        destination,
    ]

    run(command)


def crossfade_clips(first, second, destination):
    """Join two clips with a video crossfade."""
    first_duration = get_duration(first)
    offset = max(first_duration - CROSSFADE_SECONDS, 0.1)

    filter_graph = (
        f"[0:v][1:v]xfade=transition=fade:"
        f"duration={CROSSFADE_SECONDS}:offset={offset},"
        "format=yuv420p[out]"
    )

    command = [
        "ffmpeg",
        "-y",
        "-i", first,
        "-i", second,
        "-filter_complex", filter_graph,
        "-map", "[out]",
        "-an",
        "-c:v", "libx264",
        "-preset", VIDEO_PRESET,
        "-crf", str(VIDEO_CRF),
        destination,
    ]

    run(command)


def join_clips(clips, temporary_folder):
    """Normalize and crossfade all clips into one video."""
    normalized = []

    for index, clip in enumerate(clips):
        destination = os.path.join(
            temporary_folder,
            f"normalized_{index:02d}.mp4",
        )

        print(f"Normalizing {clip}")
        normalize_clip(clip, destination)
        normalized.append(destination)

    current = normalized[0]

    for index, next_clip in enumerate(normalized[1:], start=1):
        destination = os.path.join(
            temporary_folder,
            f"crossfade_{index:02d}.mp4",
        )

        print(f"Joining clip {index + 1} of {len(normalized)}")
        crossfade_clips(current, next_clip, destination)
        current = destination

    return current


# ----------------------------- FINAL VIDEO -----------------------------

def build_video():
    """Build the final MoonriseGlow video."""
    if not os.path.exists(IMAGE_FILE):
        raise SystemExit(f"Missing image: {IMAGE_FILE}")

    if not os.path.exists(AUDIO_FILE):
        raise SystemExit(f"Missing audio: {AUDIO_FILE}")

    if not os.path.exists(LYRICS_FILE):
        raise SystemExit(f"Missing lyrics: {LYRICS_FILE}")

    clips = sorted(
        glob.glob(os.path.join(CLIP_FOLDER, "*.mp4"))
    )

    if not clips:
        raise SystemExit(f"No MP4 clips found in {CLIP_FOLDER}")

    song_duration = get_duration(AUDIO_FILE)

    print()
    print("MoonriseGlow Video Maker")
    print("------------------------")
    print(f"Found {len(clips)} clips")
    print(f"Song length: {song_duration:.1f} seconds")
    print()

    with tempfile.TemporaryDirectory() as temporary_folder:
        body_video = join_clips(clips, temporary_folder)

        subtitle_file = os.path.join(
            temporary_folder,
            "lyrics.ass",
        )

        lyrics = read_lyrics(LYRICS_FILE)
        create_subtitles(
            lyrics,
            song_duration,
            subtitle_file,
        )

        video_filters = [
            "eq=contrast=1.03:saturation=1.12:brightness=0.02",
            "noise=alls=3:allf=t",
            "vignette=PI/5",
        ]

        if os.path.exists(subtitle_file):
            subtitle_path = escape_filter_path(
                os.path.abspath(subtitle_file)
            )

            video_filters.append(
                f"subtitles=filename='{subtitle_path}'"
            )

        if os.path.exists(FONT_FILE):
            title = escape_drawtext("MoonriseGlow")
            subtitle = escape_drawtext(
                "AnthroHeart Ecosystem"
            )
            font = escape_filter_path(
                os.path.abspath(FONT_FILE)
            )

            video_filters.append(
                f"drawtext=fontfile='{font}':"
                f"text='{title}':"
                "fontcolor=white:fontsize=64:"
                "borderw=3:bordercolor=black@0.6:"
                "x=(w-text_w)/2:y=90:"
                "enable='between(t,0,4)'"
            )

            video_filters.append(
                f"drawtext=fontfile='{font}':"
                f"text='{subtitle}':"
                "fontcolor=0xFFD700:fontsize=28:"
                "borderw=2:bordercolor=black@0.5:"
                "x=(w-text_w)/2:y=170:"
                "enable='between(t,0,4)'"
            )

        video_filters.append(
            f"fade=t=in:st=0:d=1.5"
        )

        video_filters.append(
            f"fade=t=out:st={max(song_duration - 4, 0):.2f}:d=4"
        )

        audio_filters = (
            f"afade=t=in:st=0:d=1.5,"
            f"afade=t=out:st={max(song_duration - 4, 0):.2f}:d=4"
        )

        command = [
            "ffmpeg",
            "-y",

            # Loop the animation body until the song ends.
            "-stream_loop", "-1",
            "-i", body_video,

            "-i", AUDIO_FILE,

            "-vf", ",".join(video_filters),
            "-af", audio_filters,

            "-map", "0:v",
            "-map", "1:a",

            "-t", f"{song_duration:.3f}",

            "-c:v", "libx264",
            "-preset", "slow",
            "-crf", "18",
            "-pix_fmt", "yuv420p",
            "-profile:v", "high",

            "-c:a", "aac",
            "-b:a", "320k",

            "-movflags", "+faststart",
            OUTPUT_FILE,
        ]

        print("Rendering final video...")
        run(command)

    print()
    print(f"Finished: {OUTPUT_FILE}")


if __name__ == "__main__":
    build_video()
