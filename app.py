import gradio as gr

from backend.nonreflecting_ray_tracing import nonreflecting_plotter
from backend.reflecting_ray_tracing import reflecting_plotter

description1 = (
    "A source of **light** placed at the **origin**. A spherical **non-Reflecting** surface placed in front it."
    "**Change ANY Parameter to get it working.**"
)
iface1 = gr.Interface(
                      fn = nonreflecting_plotter, 
                      inputs=[
                        gr.Number(label="Circle Center X (a)", value=20, info="X coordinate of Circle center"),
                        gr.Number(label="Circle Center Y (b)", value=20, info="Y coordinate of Circle center"),
                        gr.Number(label="Radius (r)", value=15, info="Radius of the circle"),
                        gr.Slider(minimum=3, maximum=1000, step=1, label="Number of Rays", value=50, info="Number of rays to be plotted in total"),
                        gr.Radio(label="Remove Clutter", choices=["Yes", "No"], value="No", info="Only keep rays that are INCIDENT by the surface."),
                    ],
                    outputs=[
                        gr.Image(label="Ray Tracing Output"), 
                        gr.Number(label="Fraction of Incident Rays", info="Out of 100 rays, how many are incident on the surface"),
                    ],
                    live=True,
                    title="Non-Reflective Ray Tracing", 
                    description=description1,
                 )

description2 = ("A source of **light** placed at the **origin**. A spherical **Reflecting surface** placed in front it. This interface simulates the rays interaction with the Reflecting surface."
    "**Change ANY Parameter to get it working.**"
)
iface2 = gr.Interface(
                      fn = reflecting_plotter, 
                      inputs=[
                        gr.Number(label="Circle Center X (a)", value=20, info="X coordinate of Circle center"),
                        gr.Number(label="Circle Center Y (b)", value=20, info="Y coordinate of Circle center"),
                        gr.Number(label="Radius (r)", value=15, info="Radius of the circle"),
                        gr.Slider(minimum=3, maximum=1000, step=1, label="Number of Rays", value=50, info="Number of rays to be plotted in total"),
                        gr.Radio(label="Remove Clutter", choices=["Yes", "No"], value="No", info="Only keep rays that are REFLECTED to the surface."),
                    ],
                    outputs=[
                        gr.Image(label="Ray Tracing Output"), 
                        gr.Number(label="Fraction of Reflected Rays", info="Out of 100 rays, how many get reflected by the surface"),
                    ],
                    live=True,
                    title="Reflective Ray Tracing", 
                    description=description2,
                 )


combinedInterface = gr.TabbedInterface([iface1, iface2],
                                       ['Non-Reflective Ray Tracing', 'Reflective Ray Tracing']
                                      )

combinedInterface.launch(share=False)