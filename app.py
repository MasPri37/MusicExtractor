import os
import gradio as gr
from scipy.io.wavfile import write


def inference(audio):
  os.makedirs("out", exist_ok=True)
  write('test.wav', audio[0], audio[1])
  os.system("python3 -m demucs.separate -n htdemucs --two-stems=vocals -d cpu test.wav -o out")
  return "./out/htdemucs/test/vocals.wav","./out/htdemucs/test/no_vocals.wav"
    
title = "Demucs Music Source Separation (v4)"
description = "This is the latest 'bleeding edge version' which enables the new v4 Hybrid Transformer model. <br> for this space, 2 stem sepration (Karaoke Mode) is enabled and CPU mode which has been optimised for best quality & processing time. <p>| Gradio demo for Demucs(v4): Music Source Separation in the Waveform Domain. To use it, simply upload your audio, or click one of the examples to load them. Read more at the links below.</p>"
article = "<p style='text-align: center'><a href='https://arxiv.org/abs/1911.13254' target='_blank'>Music Source Separation in the Waveform Domain</a> | <a href='https://github.com/facebookresearch/demucs' target='_blank'>Github Repo</a> | <a href='https://www.thafx.com' target='_blank'>//THAFX</a></p>"

examples=[['test.mp3']]
gr.Interface(
    inference, 
    gr.Audio(type="numpy", label="Input"),
    [gr.Audio(type="filepath", label="Vocals"),gr.Audio(type="filepath", label="No Vocals / Instrumental")],
    title=title,
    description=description,
    article=article,
    examples=examples
    ).launch(enable_queue=True)