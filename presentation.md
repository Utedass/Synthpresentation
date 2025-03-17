---
marp: true
theme: gaia
paginate: true
style: |
  .columns {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 1rem;
  }
  .columns3 {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 1rem;
  }
---

<style>
section::after {
  content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
}
</style>

# Det är synd att inte syntha

---

# Innehåll

<div class="columns">
<div>
<ul>
<li> Synthesizers </li>
<li> Ljud och vågformer </li>
<li> Oscillatorer </li>
<li> Control voltage </li>
<li> Filter </li>
<li> Gate </li>
</ul>
</div>
<ul>
<li> Envelop Generator </li>
<li> Sequencer </li>
<li> Länkar och resurser </li>
<li> Demo </li>
</ul>
</div>

---

# Vadå syntesajslar?

- Skapar ljudsignaler från "ingenting", syntetiskt
- Modifierar signalerna genom olika filter och effekter
- Det finns många olika synthesizar
  - Bas, "synth", trummor, trumpeter..
- Analoga och digitala

---

# Modulära synthesizers

- Enskilda funktioner per modul
- Kopplas ihop med patchkablar

---

# Modulära synthesizers

- Enskilda funktioner per modul
- Kopplas ihop med patchkablar
- Den som har flest moduler när den dör vinner

---

# Ljud och vågformer

- Vibration i form av tryckskillnader som propagerar i luften
- Hörbart ljud inom 20 Hz - 20 kHz
- Vågformen påverkar karaktären på ljudet
- Representeras som spänning i en synthesizer, -5 V till 5 V

---

# Oscillatorer

![bg height:7cm width:30cm](img/waves.png)

- Vanliga vågformer:
  - Sinus
  - Triangel
  - Ramp / Sågtand
  - Fyrkant / Puls
- VCO - Voltage Controlled Oscillator
- LFO - Low Frequency Oscillator

---

# Filter

- Brytfrekvens
- Resonans
- Roligast på vågor med mycket frekvensinnehåll
- LP, lågpass är vanligt

---

# Control Voltage - CV

- Styrsignal som påverkar parametrar
  - VCO: Frekvens, vågform, PWM..
  - VCF: Brytfrekvens, resonans..
  - VCA: Dämpning, balans..
- 0 V - 10 V i Eurorack
- 1 V / Oktav
- Kan genereras av LFO, Envelope Generators etc.

---

# Gate & Envelop Generator (EG)

- Gate: Signal som indikerar "ton på" eller anslag
- Aktiv så länge som "tangenten" är nedtryckt
- Trigger: Signal precis som Gate, men enbart en kort puls
- Går att få ut från klaviatur eller sequencer
- Envelop Generator - En CV-källa för att forma ljud
- Gate kan användas för att starta en envelop-cykel
- ASDR: Attack Sustain Decay Release

---

# Sequencer

- Genererar en sekvens av CV
- Kan generera Gate signal på alla eller specifika steg
- Kan vara kvantetiserande

---

# Andra slags moduler

<style scoped>
ul {
    font-size: 20px;
}
</style>
<div class="columns3">
<div>
<ul>

<li> VCA </li>
<li> Mixer </li>
<li> MIDI Interface </li>
<li> Delay </li>
<li> Reverb / Echo </li>
<li> Ring Modulator </li>
<li> Clock Generator </li>
<li> Clock divider </li>
<li> Noise </li>
<li> S/H - Sample & Hold </li>

</ul>
</div>
<div>
<ul>

<li> Multieffekter </li>
<li> Visuella effekter </li>
<li> Attenuverter </li>
<li> Quantizer </li>
<li> Sampler </li>
<li> Distorsion </li>
<li> Compressor </li>
<li> Slew Limiter </li>
<li> Wave Shaper </li>
<li> Trummor </li>

</ul>
</div>
<div>
<ul>

<li> Equalizer </li>
<li> Envelope Follower </li>
<li> Phase Shifter </li>
<li> Tuner </li>
<li> Aritmetiska </li>
<li> Logiska </li>
<li> Utility </li>
<li> Blanka paneler </li>
<li> Special </li>

</ul>
</div>
</div>

---

# Länkar och resurser

<style scoped>
ul {
    font-size: 20px;
}
</style>

- [VCV Rack](https://vcvrack.com/) - Gratis modularsynthmjukvara
- [Make: Analog Synthesizers](https://www.akademibokhandeln.se/bok/make-analog-synthesizers/9781449345228) - Bok av Ray Wilson med mycket grunläggande och matnyttigt
- [MFOS: Music From Outer Space](https://musicfromouterspace.com/) - Ray Wilsons hemsida med många designer
- [Colin Benders - Youtube](https://www.youtube.com/watch?v=Q6OA_Y5o4G0&list=PLBOwYevicX2BVFV58wMYj8F_SqGU45-lI) - Modular Mayhem är en serie videor med rätt bra musik på en Gigantisk modular
- [Analog Circuits for Music Synthesis](https://www.youtube.com/watch?v=mYk8r3QlNi8&list=PLOunECWxELQS5bMdWo9VhmZtsCjhjYNcV) - En kurs av Aaron Lanterman. En del historia och mycket elektronik.
- [Winterbloom - Discord](https://discord.gg/UpfqghQ) - Discordkanal med trevlig atmosfär och massa inspirerande DIY:are
- [Moritz Klein - Youtube](https://www.youtube.com/@MoritzKlein0/videos) - Många DIY-designer och pedagogiska videor
- [Modular Grid](https://modulargrid.net/e/modules/browser) - Databas fullspäckad med info om "alla" moduler som finns. Man kan även planera sitt rack.
- [Modular synthesis Explained](https://youtu.be/cWslSTTkiFU?si=XNqCw8Mf3C-B1Egh) - Andrew Huang förklarar modularsynthar från grunden och bra demos
- [Jegatron - Modular Synthesizers](https://wiki.jegatron.se/doku.php?id=modular_synthesizers:modular_synthesizers) - Min egen samling av länkar och information

---

# Demo
