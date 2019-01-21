#!/usr/bin/env python
import console
import conversion
import sst

test_files = ["sample/rolling_in_the_deep/reference_stylized.mp3"]

for f in test_files:
    console.time("preprocessing")
    console.log("starting", f)
    audio, sample_rate = conversion.file_to_audio(f)
    amplitude, phase = conversion.audio_to_spectrogram(audio,fft_window_size=1536)
    console.timeEnd("preprocessing")
    console.time("extracting fundamental")
    fundamental = sst.extract_fundamental(amplitude)
    console.timeEnd("extracting fundamental")
    conversion.image_to_file(fundamental, f + ".fundamental.png")

    console.time("fundamental to harmonics")
    harmonics = sst.fundamental_to_harmonics(fundamental, amplitude)
    console.timeEnd("fundamental to harmonics")
    conversion.image_to_file(harmonics, f + ".harmonics.png")

    fundamental_audio = conversion.amplitude_to_audio(fundamental, fft_window_size=1536, phase_iterations=1, phase=phase)
    conversion.audio_to_file(fundamental_audio, f + ".fundamental.mp3")

    harmonics_audio = conversion.amplitude_to_audio(harmonics, fft_window_size=1536, phase_iterations=1, phase=phase)
    conversion.audio_to_file(harmonics_audio, f + ".harmonics.mp3")
    console.log("finished", f)
