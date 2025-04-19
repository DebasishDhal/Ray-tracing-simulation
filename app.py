import gradio as gr

from backend.nonreflecting_ray_tracing import nonreflecting_plotter

description1 = "A source of light placed at the origin. A spherical non-reflecting surface placed in front it. This interface simulates the rays interaction with the non-reflecting surface."
iface1 = gr.Interface(
                      fn = nonreflecting_plotter, 
                      inputs=[
                        gr.Number(label="Circle Center X (a)", value=20),
                        gr.Number(label="Circle Center Y (b)", value=20),
                        gr.Number(label="Radius (r)", value=15),
                        gr.Slider(minimum=1, maximum=1000, step=1, label="Number of Rays", value=50)
                    ],
                    outputs="image",
                    live=True,
                    title="Channel domination", 
                    description=description1,
                 )

combinedInterface = gr.TabbedInterface([iface1],
                                       ['Channel domination']
                                      )

combinedInterface.launch(share=False)