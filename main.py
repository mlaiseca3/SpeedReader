from nicegui import ui

ui.label('Enter text to read')

ui.input(label='Text', placeholder='start typing',
         on_change=lambda e: result.set_text('you typed: ' + e.value),
            validation={'Input too long': lambda value: len(value) < 20 }).props('clearable')
result = ui.label()

ui.label('Toggle slider to set reading speed')
slider = ui.slider(min=0, max=1, step=0.01, value=0.5)
ui.circular_progress().bind_value_from(slider, 'value')


ui.run()