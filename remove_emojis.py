#!/usr/bin/env python3
"""Remove emojis and replace with professional SVG icons in the Experiência section."""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the 4 emoji replacements
replacements = [
    # Amanhecer na Praia - Sun icon
    (
        '<div style="font-size: 3rem; margin-bottom: 12px;">🌅</div>',
        '''<div style="width: 64px; height: 64px; background: rgba(254, 206, 87, 0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 16px;">
<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<circle cx="12" cy="12" r="5"/>
<line x1="12" y1="1" x2="12" y2="3"/>
<line x1="12" y1="21" x2="12" y2="23"/>
<line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/>
<line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/>
<line x1="1" y1="12" x2="3" y2="12"/>
<line x1="21" y1="12" x2="23" y2="12"/>
<line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/>
<line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/>
</svg>
</div>'''
    ),
    # Gastronomia Local - Utensils/Coffee icon
    (
        '<div style="font-size: 3rem; margin-bottom: 12px;">🍽️</div>',
        '''<div style="width: 64px; height: 64px; background: rgba(254, 206, 87, 0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 16px;">
<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M18 8h1a4 4 0 0 1 0 8h-1"/>
<path d="M2 8h16v9a4 4 0 0 1-4 4H6a4 4 0 0 1-4-4V8z"/>
<line x1="6" y1="1" x2="6" y2="4"/>
<line x1="10" y1="1" x2="10" y2="4"/>
<line x1="14" y1="1" x2="14" y2="4"/>
</svg>
</div>'''
    ),
    # Exploração & Natureza - Home/Nature icon
    (
        '<div style="font-size: 3rem; margin-bottom: 12px;">🚶‍♀️</div>',
        '''<div style="width: 64px; height: 64px; background: rgba(254, 206, 87, 0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 16px;">
<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
<polyline points="9 22 9 12 15 12 15 22"/>
<path d="M9 2v4"/>
<path d="M15 2v4"/>
</svg>
</div>'''
    ),
    # Descanso & Conforto - Book/Relax icon
    (
        '<div style="font-size: 3rem; margin-bottom: 12px;">😌</div>',
        '''<div style="width: 64px; height: 64px; background: rgba(254, 206, 87, 0.15); border-radius: 50%; display: flex; align-items: center; justify-content: center; margin-bottom: 16px;">
<svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="var(--gold)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/>
<path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/>
</svg>
</div>'''
    )
]

# Apply all replacements
for old, new in replacements:
    content = content.replace(old, new)

# Write the updated content
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Replaced 4 emojis with professional SVG icons")
print("   🌅 → Sun icon (Amanhecer na Praia)")
print("   🍽️ → Coffee icon (Gastronomia Local)")
print("   🚶‍♀️ → Home icon (Exploração & Natureza)")
print("   😌 → Book icon (Descanso & Conforto)")
