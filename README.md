# 🎵 lofi-station CLI

Uma estação de música lofi no terminal.
Escolha seu mood, foque e relaxe.

## Funcionalidades
- Seleção de mood (Focus / Chill)
- Interface bonita com Rich
- Timer Pomodoro integrado

## Decisões técnicas

### 🎵 Player de áudio: pygame

**Opção considerada:** `yt-dlp + mpv` — streaming direto do YouTube 
no terminal, sem abrir navegador.

**Problema:** `mpv` requer Xcode 15 para compilação, incompatível 
com macOS 12 que não recebe mais atualizações.

**Decisão:** usar `pygame` com arquivos `.mp3` locais — simples, 
funcional e sem dependências externas problemáticas.