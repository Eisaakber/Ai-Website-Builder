#!/usr/bin/env python3
"""
AI Website Maker - NiceGUI version (fixed expansion component name)
Run with:    python this_file.py
"""

from nicegui import ui
import asyncio
from datetime import datetime

# =====================================
#   GLOBAL DATA (in-memory for demo)
# =====================================
generated_sites = []           # list of dicts

api_keys = {                   # store API keys here (per provider)
    'OpenAI': '',
    'Anthropic Claude': '',
    'Google Gemini': '',
    'Custom API': ''
}

selected_provider = 'OpenAI'   # default

# =====================================
#   HELPER FUNCTIONS
# =====================================

async def generate_website():
    if not description.value.strip():
        ui.notify('Please describe your website first', type='warning', timeout=4000)
        return

    loading_dialog.open()
    progress = ui.linear_progress(value=0).props('instant-feedback').classes('my-4')

    try:
        for i in range(101):
            await asyncio.sleep(0.018)
            progress.set_value(i / 100)

        short_desc = description.value[:90] + '…' if len(description.value) > 90 else description.value

        new_site = {
            'id': len(generated_sites) + 1,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'short_desc': short_desc,
            'pages': pages_slider.value,
            'features': features.value,
            'colors': {'primary': primary_color.value, 'secondary': secondary_color.value},
            'template': template_select.value
        }

        generated_sites.append(new_site)

        ui.notify(f'Mock website #{new_site["id"]} created!', type='positive')
        ui.notify(f'Based on: {short_desc}', type='info', timeout=6000)

    finally:
        loading_dialog.hide()


def clear_api_key():
    api_keys[selected_provider] = ''
    api_key_input.value = ''
    ui.notify(f'API key for {selected_provider} cleared', type='warning')


# =====================================
#   UI LAYOUT
# =====================================

ui.dark_mode().enable()

with ui.header().classes('items-center justify-between px-6 py-3 bg-gradient-to-r from-indigo-800 to-purple-900'):
    ui.label('AI Website Maker').classes('text-2xl font-bold text-white')
    ui.space()
    ui.label('Demo • Mock version • No real AI calls').classes('text-sm italic opacity-70 text-white')

with ui.row().classes('w-full max-w-7xl mx-auto gap-6 p-6'):
    # LEFT COLUMN ── Settings / Sidebar
    with ui.column().classes('w-80 shrink-0 bg-gray-900 rounded-xl p-6 shadow-2xl border border-gray-700'):
        ui.label('Configuration').classes('text-xl font-semibold mb-4 text-indigo-300')

        provider_select = ui.select(
            options=list(api_keys.keys()),
            label='AI Provider',
            value=selected_provider
        ).classes('mb-4').on_value_change(lambda e: globals().update(selected_provider=e.value))

        api_key_input = ui.input(
            label='API Key',
            password=True,
            value=api_keys.get(selected_provider, '')
        ).classes('mb-4')

        async def save_key():
            api_keys[selected_provider] = api_key_input.value.strip()
            ui.notify(f'Key updated for {selected_provider}', type='positive', timeout=2500)

        api_key_input.on('keydown.enter', save_key)
        ui.button('Save Key', on_click=save_key, icon='save').props('flat color=indigo-6').classes('mb-6 w-full')

        ui.button('Clear Key', on_click=clear_api_key, icon='delete').props('flat color=red-7').classes('mb-6 w-full')

        ui.separator().classes('my-4')

        ui.label('Style & Template').classes('text-lg font-medium mb-3')

        template_select = ui.select(
            options=['Modern Minimal', 'Corporate', 'Creative Portfolio', 'E-commerce', 'Blog', 'Landing Page'],
            label='Template Style',
            value='Modern Minimal'
        ).classes('mb-4')

        with ui.row().classes('gap-4'):
            primary_color = ui.color_input(label='Primary', value='#6366f1').classes('w-1/2')
            secondary_color = ui.color_input(label='Secondary', value='#8b5cf6').classes('w-1/2')

        # FIXED: Use ui.expansion (not expander) + set .value after creation
        with ui.expansion('Advanced options') as adv_expansion:
            ui.checkbox('Include animations', value=True)
            ui.checkbox('Responsive design', value=True)
            ui.checkbox('SEO optimized', value=True)

        # Open by default (set False if you want collapsed)
        adv_expansion.value = True

    # RIGHT COLUMN ── Main content + Tabs
    with ui.column().classes('grow'):
        with ui.tabs().classes('mb-6') as tabs:
            tab_generate   = ui.tab('Generate')
            tab_customize  = ui.tab('Customize')
            tab_preview    = ui.tab('Preview')
            tab_export     = ui.tab('Export')

        with ui.tab_panels(tabs, value=tab_generate).classes('w-full'):
            with ui.tab_panel(tab_generate):
                ui.label('Describe your website').classes('text-2xl font-bold mb-4')

                description = ui.textarea(
                    placeholder='e.g. Modern portfolio for a wedding photographer...\n'
                                 'Professional business site for real-estate...\n'
                                 'Small online store selling handmade jewelry',
                    label='Website idea / description'
                ).props('outlined autogrow rounded-xl').classes('w-full min-h-40 mb-6')

                with ui.row().classes('gap-6 mb-6 items-center'):
                    pages_slider = ui.slider(min=1, max=8, value=3).props('label-always').classes('w-1/2')
                    ui.label('Number of main pages').classes('text-gray-300')

                features = ui.select(
                    options=[
                        'Contact / WhatsApp form', 'Photo gallery', 'Testimonials', 'Blog section',
                        'Newsletter signup', 'Mobile menu', 'Dark mode toggle', 'Booking calendar'
                    ],
                    label='Key features',
                    multiple=True
                ).classes('mb-6')

                ui.button(
                    'GENERATE WEBSITE MOCKUP',
                    on_click=generate_website,
                    icon='auto_awesome'
                ).props('unelevated push color=indigo-9 size=lg').classes('w-full text-lg font-bold py-6')

            with ui.tab_panel(tab_customize):
                if not generated_sites:
                    ui.label('No websites generated yet.\nGo to Generate tab.').classes('text-center text-gray-400 py-12 text-xl')
                else:
                    ui.label('Customization coming in next version...').classes('text-center py-12 opacity-70 text-xl')

            with ui.tab_panel(tab_preview):
                if not generated_sites:
                    ui.label('Generate something first').classes('text-center text-gray-400 py-12 text-xl')
                else:
                    ui.label('Preview area (mock)').classes('text-2xl mb-6')
                    ui.html('<div class="h-64 bg-gradient-to-br from-indigo-900/40 to-purple-900/40 rounded-xl flex items-center justify-center text-2xl text-gray-300">Website preview placeholder</div>')

            with ui.tab_panel(tab_export):
                if not generated_sites:
                    ui.label('Nothing to export yet').classes('text-center text-gray-400 py-12 text-xl')
                else:
                    ui.label('Export options coming soon...').classes('text-center py-12 opacity-70 text-xl')

# Loading dialog
with ui.dialog(value=False).props('persistent') as loading_dialog:
    with ui.card().classes('w-96 text-center'):
        ui.label('Generating your website concept...').classes('text-xl font-medium mb-6')
        ui.linear_progress(value=0).props('instant-feedback indeterminate').classes('mb-4')
        ui.label('This is just a demo — no real AI call yet').classes('text-sm opacity-60')

ui.run(
    title='AI Website Maker • NiceGUI',
    dark=True,
    host='127.0.0.1',
    port=8080,
    reload=True
)