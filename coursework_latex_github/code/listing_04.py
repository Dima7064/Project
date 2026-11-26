with gr.Row():
    with gr.Column():
        category = gr.Dropdown(cfg.style_choices)
        length = gr.Radio([1, 2, 3], value=2)
        count = gr.Slider(1, MAX_SLOTS, value=10)
        gr.Button("Сгенерировать")
