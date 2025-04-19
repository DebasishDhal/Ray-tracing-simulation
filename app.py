import gradio as gr

from backend.nonreflecting_ray_tracing import nonreflecting_plotter
from backend.reflecting_ray_tracing import reflecting_plotter

description1 = "A source of light placed at the origin. A spherical non-Reflecting surface placed in front it. This interface simulates the rays interaction with the non-Reflecting surface."
iface1 = gr.Interface(
                      fn = nonreflecting_plotter, 
                      inputs=[
                        gr.Number(label="Circle Center X (a)", value=20),
                        gr.Number(label="Circle Center Y (b)", value=20),
                        gr.Number(label="Radius (r)", value=15),
                        gr.Slider(minimum=3, maximum=1000, step=1, label="Number of Rays", value=50)
                    ],
                    outputs="image",
                    live=True,
                    title="Non-Reflective Ray Tracing", 
                    description=description1,
                 )

description2 = "A source of light placed at the origin. A spherical Reflecting surface placed in front it. This interface simulates the rays interaction with the Reflecting surface."
iface2 = gr.Interface(
                      fn = reflecting_plotter, 
                      inputs=[
                        gr.Number(label="Circle Center X (a)", value=20),
                        gr.Number(label="Circle Center Y (b)", value=20),
                        gr.Number(label="Radius (r)", value=15),
                        gr.Slider(minimum=3, maximum=1000, step=1, label="Number of Rays", value=50)
                    ],
                    outputs="image",
                    live=True,
                    title="Reflective Ray Tracing", 
                    description=description2,
                 )


combinedInterface = gr.TabbedInterface([iface1, iface2],
                                       ['Non-Reflective Ray Tracing', 'Reflective Ray Tracing']
                                      )

combinedInterface.launch(share=False)