<img width="816" height="544" alt="Moonrise_Base_Image" src="https://github.com/user-attachments/assets/bd3fd199-906c-4b35-81ef-b32303b0f0f8" />


````markdown
# MoonriseGlow

A small experiment in making a complete animated music video with AI tools, Python, and FFmpeg.

The video includes:

- An AI-generated fantasy image
- An AI-generated song
- Eight short animation clips
- Automatically created subtitles
- Automatic crossfades, looping, color effects, and audio fades

## VIDEO DEMO: https://www.youtube.com/watch?v=yOGric3p3yI

## See Also Violet Sun (Forest Moon): https://www.youtube.com/watch?v=VZngccpEIa8

Created by: Thomas B. Sweet (Saguna Anthroness aka Aumaroo AnthroHeart Starwalker)
License: MIT
Date: Thursday, Sept. 17, 2026
Source: AnthroHeart Ecosystem (CC BY 4.0): https://deviantart.com/anthro-shaman

A project like this can often be made in a few hours for roughly $40–$50 in subscriptions and usage credits.

> This project uses fictional animal-like characters and an invented chant language. The chant is not based on a real language or culture.

## Tools

- An image generator, such as FLUX.2 Pro
- Suno for music
- Kling for animation
- Python 3 - The code for rendering the video in this example would normally be created by an AI of your choice for the particular edits you want.
- FFmpeg
- OpenRouter or another AI service for chats, images and coding generation/transmissions
- Fonts from Google Fonts

## Python Editing Script Runtime

Finished: MoonriseGlow_Final.mp4

real 3m39.087s
user 23m41.118s
sys 0m15.233s

## Folder Setup

Create this folder structure:

```text
moonrise-glow/
├── Moonrise_Base_Image.png
├── MoonriseGlow.wav
├── lyrics_moonrise.txt
├── make_moonrise_video.py
├── clips/
│   ├── 01_gather.mp4
│   ├── 02_instruments.mp4
│   ├── 03_nectar.mp4
│   ├── 04_smoke.mp4
│   ├── 05_dance_start.mp4
│   ├── 06_chaos_fun.mp4
│   ├── 07_peak_moon.mp4
│   └── 08_wind_down.mp4
└── fonts/
    └── Cinzel-SemiBold.ttf
```
````

Install FFmpeg:

### macOS

```bash
brew install ffmpeg
```

### Ubuntu or Debian

```bash
sudo apt update
sudo apt install ffmpeg
```

### Windows

```powershell
winget install Gyan.FFmpeg
```

Check that everything works:

```bash
python3 --version
ffmpeg -version
ffprobe -version
```

---

## 1. Create the Master Image

Use this prompt with an image generator:

```text
A wide cinematic 16:9 scene of a joyous communal celebration at night on an alien forest moon. Under a gigantic glowing violet moon, dozens of diverse anthropomorphic creatures gather around glowing fires. Include mammalian, avian, scaled, amphibious, and entirely fictional species with expressive faces and varied silhouettes.

The creatures play strange instruments made from wood, bone, gourds, vines, crystal, and hollow reeds. Some raise glowing nectar gourds in celebration. Others hold ornate herbal pipes releasing colorful blue, green, and violet smoke that curls into playful shapes.

The mood is magical, communal, warm, energetic, and family-friendly. Ancient trees surround the clearing. Their trunks are covered in moss, luminous fungi, hanging vines, and glowing plants. Fireflies and floating spores drift through the air.

Violet moonlight mixes with orange firelight and turquoise bioluminescence. Hyper-detailed cinematic fantasy photography, realistic fur and scales, natural poses, atmospheric mist, volumetric lighting, deep shadows, subtle film grain, rich violet-and-teal color grade, wide establishing composition, fantasy documentary style.
```

Negative prompt:

```text
visible genitals, explicit nudity, sexualized poses, minors, violence, gore, weapons, horror, modern clothing, modern technology, text, captions, watermark, logo, distorted anatomy, extra limbs, extra fingers, duplicate creatures, fused bodies, blurry faces, low resolution, excessive smoke, flat lighting, cropped figures, fisheye distortion
```

Save the image as:

```text
Moonrise_Base_Image.png
```

---

## 2. Create the Song

Use this style prompt with a music generator:

```text
Upbeat tribal fusion with intricate polyrhythmic percussion, playful invented-language chanting, whimsical bone flutes, deep wooden horns, energetic communal celebration, varied character voices, cute high voices mixed with gruff low voices, primal stomp dance, cinematic fantasy atmosphere, joyful rather than aggressive.
```

Generate several versions and choose your favorite.

Save the selected audio file as:

```text
MoonriseGlow.wav
```

---

## 3. Create the Animation Clips

Use the master image as the reference image for every animation.

Recommended settings:

- 15 seconds
- 720p
- One output per prompt
- Native audio disabled

Use this negative prompt for every clip:

```text
text, watermark, logo, signature, subtitles, modern clothing, modern technology, distorted anatomy, extra limbs, morphing faces, flickering, jitter, warping, blurry, low quality, oversaturated, aggressive, violent, horror
```

### Clip 1 — `01_gather.mp4`

```text
Wide shot. Diverse anthropomorphic creatures emerge from the treeline and walk toward a glowing gathering beneath a giant violet moon. The mood is warm, joyful, and full of anticipation.
```

### Clip 2 — `02_instruments.mp4`

```text
Medium shot. Fur-covered and scaled creatures play wooden drums, bone flutes, gourds, and hollow reeds. Their heads and shoulders move naturally with the rhythm while fireflies float around them.
```

### Clip 3 — `03_nectar.mp4`

```text
Close-up. A small cute creature and a larger gruff creature smile and clink glowing gourd cups before taking a drink. Wholesome, friendly celebration.
```

### Clip 4 — `04_smoke.mp4`

```text
Medium shot. A circle of creatures relaxes around a glowing fire and passes ornate wooden pipes. Blue and green smoke curls into playful shapes while everyone smiles and talks.
```

### Clip 5 — `05_dance_start.mp4`

```text
A diverse group begins a rhythmic stomping dance around a glowing fire pit. Dust, sparks, and bioluminescent spores rise from the ground.
```

### Clip 6 — `06_chaos_fun.mp4`

```text
High-energy celebration. Many different species dance, laugh, jump, and move together. A small character safely rides on the shoulders of a much larger character. Playful and non-violent.
```

### Clip 7 — `07_peak_moon.mp4`

```text
Wide epic shot. The entire gathering dances beneath the enormous violet moon. The moon pulses gently while the celebration lights up the forest canopy.
```

### Clip 8 — `08_wind_down.mp4`

```text
Slow peaceful shot. The celebration winds down. Creatures sit close together and look up at the moon while smoke, fireflies, and glowing spores drift slowly through the air.
```

---

## 4. Create the Lyrics File

Create `lyrics_moonrise.txt`.

The pipe character separates the invented chant from its English translation.

```text
[Intro]

Kruk-tuk chikka-cha! | Gather round the fire glow
Oolu-loo brum-hum tuk. | See the violet moon rise slow
Yip-yap kree-ko! | Bring the drums, bring the feet
Grum-pa-pa zoop! | Feel the forest heartbeat

[Chorus]

Moonrise Glow! Chikka-rokka-ho! | We are living, we are here!
Moonrise Glow! Oolu-oolu-lo! | Nothing hidden, nothing to fear!

[Verse 2]

Sippa-sip glim-glam. | Taste the sweet shining nectar
Puffa-puff woo-shhh. | Breathe the smoke, floating vector
Hee-hee gruff-gruff. | Funny thoughts in the head
Tik-tokala zoom! | Spinning round instead

[Bridge]

Rokka-rok! | Stomp the ground
Chikka-chok! | Wake the sound
Oolu-ee! | Wild and free
Kruk-tuk-tee! | You and me

[Final Chorus]

Moonrise Glow! Chikka-rokka-ho! | We are living, we are here!
Moonrise Glow! Oolu-oolu-lo! | Nothing hidden, nothing to fear!

[Outro]

Glim-glam... woo-shhh... | Goodnight moon...
```

---

## 5. Run the Python Editor

Save the following file as:

```text
make_moonrise_video.py
```

```python
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
- Source: AnthroHeart Ecosystem (CC BY 4.0): https://deviantart.com/anthro-shaman

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
AUDIO_FILE = "MoonriseGlow.wav"
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
```

Run it:

```bash
python3 make_moonrise_video.py
```

The finished video will be saved as:

```text
MoonriseGlow_Final.mp4
```

## Notes

The subtitles are timed evenly across the song. They will usually be close enough for a first version, but you can manually adjust the timing later if you want perfect synchronization.

The animation clips are looped to fill the length of the song. Because the loop happens at the end of the animation sequence, there may be a visible jump when the clips start over. That is normal for this simple version.

Before publishing, check the commercial-use rules for the AI services, music, images, animation, and fonts you used.

## Credits

- Concept and direction: AnthroHeart
- Music: Generated with Suno
- Image: Generated with an AI image model
- Animation: Generated with Kling
- Editing: Python and FFmpeg

```

```
