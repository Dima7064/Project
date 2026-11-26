from dataclasses import dataclass
import gradio as gr
MAX_SLOTS = 50
            generate_btn = gr.Button("Сгенерировать",
                                      variant="primary", size="lg")
            status = gr.Markdown(value="_Готов к работе._",
                                  elem_classes=["status-bar"])
        # Центральная панель: результаты
        with gr.Column(scale=3, min_width=440):
            gr.Markdown(cfg.heading)
            result_slots = []
            for _ in range(MAX_SLOTS):
                with gr.Row(visible=False) as row:
                    name_tb = gr.Textbox(value="", show_label=False,
                                          interactive=False, container=False,
                                          scale=4, elem_classes=["card-name"])
                    star_btn = gr.Button("", scale=0, min_width=48,
                                          elem_classes=["star-btn"])
                result_slots.append({"row": row, "name": name_tb,
                                      "star": star_btn})
        # Правая панель: избранное
        with gr.Column(scale=1, min_width=260,
                        elem_classes=["favorites-panel"]):
            gr.Markdown("### Избранное")
            fav_display = gr.Textbox(value="", lines=10, show_label=False,
                                      interactive=False,
                                      placeholder="Пока пусто.")
            clear_btn = gr.Button("Очистить всё", size="sm")
            with gr.Row():
                export_txt_btn = gr.Button(".txt", size="sm")
                export_csv_btn = gr.Button(".csv", size="sm")
            download_file = gr.File(label="Скачать", visible=False)
        try:
            pipeline = get_pipeline()
        except (FileNotFoundError, ValueError) as e:
            empty = []
            for _ in range(MAX_SLOTS):
                empty.extend([gr.update(visible=False), gr.update(value="")])
            empty.append(f" {e}")
            yield tuple(empty)
            return
        try:
            results = pipeline.generate(
                style=style, parts=int(parts), count=int(count),
                seed=int(seed) if seed is not None else None)
        except ValueError as e:
            empty = []
            for _ in range(MAX_SLOTS):
                empty.extend([gr.update(visible=False), gr.update(value="")])
            empty.append(f" {e}")
            yield tuple(empty)
            return
        updates = []
        for i in range(MAX_SLOTS):
            if i < len(results):
                updates.extend([gr.update(visible=True),
                                 gr.update(value=results[i].name)])
            else:
                updates.extend([gr.update(visible=False),
                                 gr.update(value="")])
        updates.append(f" {len(results)} названий · {parts} слов")
        yield tuple(updates)
