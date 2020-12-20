# Závěrečný projek kurzu Pyladies - Ostrava 2020

## Název projektu: Hra typu Had

Zadání: https://naucse.python.cz/2020/pyladies-ostrava-podzim/projects/snake/

### Požadavky
* Tento projekt byl vytvořen pomocí Python 3.9.0

### Instalace
Aplikace využívá knihovnu [Pyglet](https://github.com/pyglet/pyglet)
>`pip install pyglet`

### Pravidla hry
* Hrací pole má 13x10 dílků
* Jeden dílek má 48 pixelů
* Had se ovládá šipkami
* Vyjetí mimo hrací plochu ukončí hru
* Kousntí do sebe sama ukončí hru
* Po spapání tří jídel had vykaká hovínko
* Spapání hovínka ukončí hru
* Po ukonční hry se v shellu zobrazí dosažené skóre

### Poznámky
Ve složce `food` je možné jídlo měnit, přidávat a mazat.

Během hry se v shellu zobrazují pomocné informace o aktuálním umístění jednotlivých objektů na hrací ploše.