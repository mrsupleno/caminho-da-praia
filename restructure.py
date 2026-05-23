#!/usr/bin/env python3
"""
Reorganiza o HTML da Pousada Caminho da Praia na ordem correta
"""
import re

# Ler HTML atual
with open('index.html.backup-before-restructure', 'r', encoding='utf-8') as f:
    html = f.read()

# Extrair seções por ID ou marcadores
def extract_section(start_marker, end_marker):
    pattern = f'{re.escape(start_marker)}.*?{re.escape(end_marker)}'
    match = re.search(pattern, html, re.DOTALL)
    return match.group(0) if match else ''

# Extrair head e navbar (mantém igual)
head = html.split('</head>')[0] + '</head>'
navbar_match = re.search(r'<!-- NAVBAR -->.*?</nav>', html, re.DOTALL)
navbar = navbar_match.group(0) if navbar_match else ''

# Extrair seções
hero_match = re.search(r'<!-- HERO -->.*?</section>', html, re.DOTALL)
hero = hero_match.group(0) if hero_match else ''

# A Pousada (nova versão com 2 colunas)
pousada_match = re.search(r'<!-- A POUSADA -->.*?(?=<!-- )', html, re.DOTALL)
pousada = pousada_match.group(0) if pousada_match else ''

# Café da Manhã (extrair da galeria)
cafe_match = re.search(r'<!-- CAFÉ DA MANHÃ ARTESANAL -->.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
cafe = cafe_match.group(0) if cafe_match else ''

# Quartos (extrair fotos da galeria)
quartos_match = re.search(r'<!-- Quartos -->.*?</div>\s*</div>', html, re.DOTALL)
quartos_imgs = quartos_match.group(0) if quartos_match else ''

# Excursões
excursoes_match = re.search(r'<!-- EXCURSÕES E PACOTES -->.*?</section>', html, re.DOTALL)
excursoes = excursoes_match.group(0) if excursoes_match else ''

# Depoimentos
depoimentos_match = re.search(r'<!-- DEPOIMENTOS -->.*?</section>', html, re.DOTALL)
depoimentos = depoimentos_match.group(0) if depoimentos_match else ''

# Experiência
experiencia_match = re.search(r'<!-- EXPERIÊNCIA -->.*?</section>', html, re.DOTALL)
experiencia = experiencia_match.group(0) if experiencia_match else ''

# Galeria compacta (praia - pegar só 4 fotos)
praia_match = re.search(r'<!-- Praia -->.*?</div>\s*</div>', html, re.DOTALL)
praia_section = praia_match.group(0) if praia_match else ''

# Criar seção de quartos nova
quartos_section = '''
<!-- QUARTOS -->
<section id="quartos" style="background: var(--surface-container); padding: 80px 24px;">
<div class="container">
<div style="text-align: center; margin-bottom: 48px;">
<h2 style="font-family: 'Montserrat', sans-serif; font-size: clamp(2rem, 4vw, 2.5rem); font-weight: 700; color: var(--primary); margin-bottom: 16px;">
Quartos & Suítes
</h2>
<div style="height: 3px; width: 60px; background: var(--gold); margin: 0 auto;"></div>
<p style="max-width: 600px; margin: 24px auto 0; color: var(--on-surface-variant); font-size: 1.05rem;">
Acomodações climatizadas com todo conforto que você e sua família merecem
</p>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
<img src="images/quarto-casal.jpg" alt="Quarto casal" style="border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; height: 280px; object-fit: cover;">
<img src="images/cama-casal.jpg" alt="Cama casal" style="border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; height: 280px; object-fit: cover;">
<img src="images/quarto-triplo.jpg" alt="Quarto triplo" style="border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; height: 280px; object-fit: cover;">
<img src="images/quarto-camas.jpg" alt="Quarto com múltiplas camas" style="border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; height: 280px; object-fit: cover;">
</div>
</div>
</section>
'''

# Criar seção de localização
localizacao_section = '''
<!-- LOCALIZAÇÃO -->
<section id="localizacao" style="background: #ffffff; padding: 80px 24px;">
<div class="container">
<div style="text-align: center; margin-bottom: 48px;">
<h2 style="font-family: 'Montserrat', sans-serif; font-size: clamp(2rem, 4vw, 2.5rem); font-weight: 700; color: var(--primary); margin-bottom: 16px;">
Localização
</h2>
<div style="height: 3px; width: 60px; background: var(--gold); margin: 0 auto;"></div>
</div>

<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 48px; align-items: start;">
<div>
<h3 style="font-family: 'Montserrat', sans-serif; font-size: 1.5rem; font-weight: 600; color: var(--primary); margin-bottom: 24px;">
Como Chegar
</h3>
<div style="display: flex; flex-direction: column; gap: 20px;">
<div style="display: flex; gap: 16px; align-items: start;">
<div style="width: 48px; height: 48px; background: rgba(2, 39, 66, 0.08); border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24" stroke="var(--primary)" stroke-width="2">
<path stroke-linecap="round" stroke-linejoin="round" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
<path stroke-linecap="round" stroke-linejoin="round" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
</svg>
</div>
<div>
<h4 style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; font-weight: 600; color: var(--primary); margin-bottom: 8px;">Endereço</h4>
<p style="color: var(--on-surface-variant); line-height: 1.6;">
Praia de Itaóca<br>
Itapemirim, Espírito Santo<br>
CEP: 29330-000
</p>
</div>
</div>

<div style="display: flex; gap: 16px; align-items: start;">
<div style="width: 48px; height: 48px; background: rgba(197, 155, 39, 0.08); border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-shrink: 0;">
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="var(--gold)"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.125.556 4.122 1.527 5.855L0 24l6.335-1.502A11.943 11.943 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 22c-1.891 0-3.667-.498-5.197-1.371l-.373-.219-3.861.915.977-3.756-.243-.389A9.942 9.942 0 012 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/></svg>
</div>
<div>
<h4 style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; font-weight: 600; color: var(--primary); margin-bottom: 8px;">Contato</h4>
<p style="color: var(--on-surface-variant); line-height: 1.6;">
Telefone/WhatsApp:<br>
<strong style="color: var(--gold);">(31) 7575-7750</strong>
</p>
<a href="https://wa.me/553175757750?text=Ol%C3%A1!%20Vi%20o%20site%20da%20Pousada%20Caminho%20da%20Praia"
target="_blank" rel="noopener"
style="display: inline-flex; align-items: center; gap: 8px; margin-top: 12px; color: var(--tertiary-bright); font-weight: 600; font-size: 0.95rem;">
Falar no WhatsApp
<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2.5"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg>
</a>
</div>
</div>
</div>
</div>

<div>
<iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3750.1234567890123!2d-40.8234567!3d-21.0123456!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x0!2zMjHCsDAwJzQ0LjQiUyA0MMKwNDknMjQuNCJX!5e0!3m2!1spt-BR!2sbr!4v1234567890123!5m2!1spt-BR!2sbr"
width="100%"
height="450"
style="border:0; border-radius: 12px; box-shadow: var(--shadow-md);"
allowfullscreen=""
loading="lazy"
referrerpolicy="no-referrer-when-downgrade"></iframe>
</div>
</div>

<style>
@media (max-width: 900px) {
#localizacao .container > div:nth-child(2) {
grid-template-columns: 1fr !important;
gap: 32px !important;
}
}
</style>
</div>
</section>
'''

# Criar galeria compacta
galeria_section = '''
<!-- GALERIA -->
<section id="galeria" style="background: var(--surface-container); padding: 80px 24px;">
<div class="container">
<div style="text-align: center; margin-bottom: 48px;">
<h2 style="font-family: 'Montserrat', sans-serif; font-size: clamp(2rem, 4vw, 2.5rem); font-weight: 700; color: var(--primary); margin-bottom: 16px;">
Praia & Região
</h2>
<div style="height: 3px; width: 60px; background: var(--gold); margin: 0 auto;"></div>
<p style="max-width: 600px; margin: 24px auto 0; color: var(--on-surface-variant); font-size: 1.05rem;">
A beleza natural de Itaóca espera por você
</p>
</div>

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
<img src="images/vista-mar-por-sol.jpg" alt="Vista do mar ao pôr do sol" style="border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; height: 280px; object-fit: cover;">
<img src="images/praia-por-sol.jpg" alt="Praia ao pôr do sol" style="border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; height: 280px; object-fit: cover;">
<img src="images/vista-mar-manha.jpg" alt="Vista do mar pela manhã" style="border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; height: 280px; object-fit: cover;">
<img src="images/praia-cadeiras.jpg" alt="Cadeiras na praia" style="border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; height: 280px; object-fit: cover;">
<img src="images/passarela-sombrinhas.jpg" alt="Passarela com sombrinhas" style="border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; height: 280px; object-fit: cover;">
<img src="images/pousada-fachada.jpg" alt="Fachada da pousada" style="border-radius: 12px; box-shadow: var(--shadow-md); width: 100%; height: 280px; object-fit: cover;">
</div>
</div>
</section>
'''

# Criar rodapé
footer = '''
<!-- RODAPÉ -->
<footer style="background: var(--primary); color: var(--on-primary); padding: 64px 24px 32px;">
<div class="container" style="max-width: 1200px; margin: 0 auto;">
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 48px; margin-bottom: 48px;">
<!-- Coluna 1: Pousada -->
<div>
<h3 style="font-family: 'Montserrat', sans-serif; font-size: 1.25rem; font-weight: 700; color: var(--gold-light); margin-bottom: 16px;">
Pousada Caminho da Praia
</h3>
<p style="color: rgba(255,255,255,0.75); font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">
Aconchego e natureza à beira-mar em Itaóca, Itapemirim-ES. Sua melhor escolha para relaxar em família.
</p>
<img src="images/logo-caminho-da-praia.jpg" alt="Logo" style="width: 80px; height: 80px; border-radius: 50%; object-fit: cover; border: 3px solid var(--gold-light);">
</div>

<!-- Coluna 2: Links Rápidos -->
<div>
<h4 style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; font-weight: 600; color: var(--gold-light); margin-bottom: 16px;">
Links Rápidos
</h4>
<ul style="list-style: none; padding: 0; margin: 0;">
<li style="margin-bottom: 12px;"><a href="#pousada" style="color: rgba(255,255,255,0.75); text-decoration: none; transition: color 0.2s;">A Pousada</a></li>
<li style="margin-bottom: 12px;"><a href="#quartos" style="color: rgba(255,255,255,0.75); text-decoration: none; transition: color 0.2s;">Quartos</a></li>
<li style="margin-bottom: 12px;"><a href="#excursoes" style="color: rgba(255,255,255,0.75); text-decoration: none; transition: color 0.2s;">Excursões</a></li>
<li style="margin-bottom: 12px;"><a href="#depoimentos" style="color: rgba(255,255,255,0.75); text-decoration: none; transition: color 0.2s;">Depoimentos</a></li>
<li style="margin-bottom: 12px;"><a href="#localizacao" style="color: rgba(255,255,255,0.75); text-decoration: none; transition: color 0.2s;">Localização</a></li>
</ul>
</div>

<!-- Coluna 3: Erica Tur -->
<div>
<h4 style="font-family: 'Montserrat', sans-serif; font-size: 1.1rem; font-weight: 600; color: var(--gold-light); margin-bottom: 16px;">
Erica Tur - Turismo & Hospedagem
</h4>
<p style="color: rgba(255,255,255,0.75); font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">
Organizamos excursões saindo de Minas Gerais com transporte, hospedagem e alimentação inclusos.
</p>
<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="var(--gold-light)"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.125.556 4.122 1.527 5.855L0 24l6.335-1.502A11.943 11.943 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 22c-1.891 0-3.667-.498-5.197-1.371l-.373-.219-3.861.915.977-3.756-.243-.389A9.942 9.942 0 012 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/></svg>
<strong style="color: var(--gold-light); font-size: 1.05rem;">(31) 7575-7750</strong>
</div>
<a href="https://wa.me/553175757750?text=Ol%C3%A1!%20Gostaria%20de%20informa%C3%A7%C3%B5es%20sobre%20excurs%C3%B5es%20e%20hospedagem"
target="_blank" rel="noopener"
style="display: inline-flex; align-items: center; gap: 8px; background: var(--tertiary-bright); color: white; padding: 12px 24px; border-radius: 4px; font-weight: 600; text-decoration: none; transition: all 0.2s; margin-top: 12px;">
<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="white"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/><path d="M12 0C5.373 0 0 5.373 0 12c0 2.125.556 4.122 1.527 5.855L0 24l6.335-1.502A11.943 11.943 0 0012 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 22c-1.891 0-3.667-.498-5.197-1.371l-.373-.219-3.861.915.977-3.756-.243-.389A9.942 9.942 0 012 12C2 6.477 6.477 2 12 2s10 4.477 10 10-4.477 10-10 10z"/></svg>
Falar no WhatsApp
</a>
</div>
</div>

<div style="border-top: 1px solid rgba(255,255,255,0.1); padding-top: 32px; text-align: center;">
<p style="color: rgba(255,255,255,0.6); font-size: 0.9rem;">
© 2026 Pousada Caminho da Praia · Itaóca, Itapemirim-ES · Todos os direitos reservados
</p>
<p style="color: rgba(255,255,255,0.5); font-size: 0.85rem; margin-top: 8px;">
Desenvolvido por <a href="https://supleno.org" target="_blank" style="color: var(--gold-light); text-decoration: none;">Supleno</a>
</p>
</div>
</div>
</footer>

<!-- JavaScript Mobile Menu -->
<script>
const hamburger = document.getElementById('hamburger');
const navLinks = document.getElementById('navLinks');

hamburger?.addEventListener('click', () => {
navLinks?.classList.toggle('active');
hamburger?.classList.toggle('active');
});

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
anchor.addEventListener('click', function (e) {
e.preventDefault();
const target = document.querySelector(this.getAttribute('href'));
if (target) {
navLinks?.classList.remove('active');
hamburger?.classList.remove('active');
window.scrollTo({
top: target.offsetTop - 72,
behavior: 'smooth'
});
}
});
});
</script>
</body>
</html>
'''

print("Script de reorganização criado. Execute manualmente a reorganização no próximo passo.")
