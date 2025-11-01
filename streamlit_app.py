import streamlit as st

st.title("🎉 Wer wird am ehesten – Umfrage unter Freunden")

# Anzahl der Kandidaten festlegen
num_candidates = st.number_input("Wie viele Kandidaten gibt es?", min_value=1, max_value=50, step=1)

# Eingabefelder für Kandidatennamen
st.subheader("👥 Kandidatennamen eingeben")
candidates = []
for i in range(num_candidates):
    name = st.text_input(f"Kandidat {i+1}", key=f"candidate_{i}")
    if name.strip():  # Nur nicht-leere Namen übernehmen
        candidates.append(name.strip())

# Kategorien
categories = [
    "Wer wird Millionär?", "Wer wird Influencer?", "Wer wird Politiker?",
    "Wer wird Schauspieler?", "Wer wird Sänger?", "Wer wird Wissenschaftler?",
    "Wer wird Sportler?", "Wer wird Künstler?", "Wer wird Koch?",
    "Wer wird Autor?", "Wer wird Gamer?", "Wer wird Tänzer?", "Wer wird Comedian?",
    "Wer wird Designer?", "Wer wird Fotograf?", "Wer gibt am meisten Geld aus", "Wer wird Musiker?", "Wer wird Unternehmer?",
    "Wer wird Lehrer?", "Wer wird Arzt?", "Wer wird Ingenieur?", "Wer wird am schnellsten obdachlos?",
    "Wer wird Pilot?", "Wer wird Architekt?", "Wer wird Journalist?", "Wer wird Programmierer?",
    "Wer wird Mechaniker?", "Wer wird Friseur?", "Wer wird Landwirt?", "Wer wird Feuerwehrmann?",
    "Wer wird Polizist?", "Wer wird Soldat?"
]

# Nur weitermachen, wenn Kandidaten eingegeben wurden
if candidates:
    num_voters = st.number_input("Wie viele Personen stimmen ab?", min_value=1, step=1)

    # Stimmen speichern
    votes = {category: {name: 0 for name in candidates} for category in categories}

    # Abstimmung
    for voter in range(1, num_voters + 1):
        st.header(f"🗳️ Person {voter} stimmt ab")
        for category in categories:
            choice = st.radio(f"{category}", candidates, key=f"{voter}_{category}")
            votes[category][choice] += 1

    # Auswertung anzeigen
    if st.button("📊 Auswertung anzeigen"):
        st.header("Ergebnisse")
        for category in categories:
            st.subheader(f"🏆 {category}")
            sorted_votes = sorted(votes[category].items(), key=lambda x: x[1], reverse=True)
            for i, (name, count) in enumerate(sorted_votes[:3], 1):
                st.write(f"{i}. {name} – {count} Stimme(n)")
else:
    st.warning("Bitte gib mindestens einen Kandidatennamen ein.")
#memory
# Kartenpaare definieren
cards = ["🍎", "🍌", "🍇", "🍓", "🍍", "🥝"]
cards *= 2  # Paare erzeugen
random.shuffle(cards)

# Session-Status initialisieren
if "flipped" not in st.session_state:
    st.session_state.flipped = [False] * len(cards)
if "matched" not in st.session_state:
    st.session_state.matched = [False] * len(cards)
if "last_click" not in st.session_state:
    st.session_state.last_click = None
st.title("🧠 Memory-Spiel")

# Karten anzeigen
for i, card in enumerate(cards):
    col = st.columns(6)[i % 6]
    with col:
        if st.session_state.matched[i] or st.session_state.flipped[i]:
            st.button(card, key=f"card_{i}", disabled=True)
        else:
            if st.button("❓", key=f"card_{i}"):
                st.session_state.flipped[i] = True
                if st.session_state.last_click is None:
                    st.session_state.last_click = i
                else:
                    j = st.session_state.last_click
                    if cards[i] == cards[j]:
                        st.session_state.matched[i] = True
                        st.session_state.matched[j] = True
                    else:
                        st.warning("Kein Match!")
                        st.session_state.flipped[i] = False
                        st.session_state.flipped[j] = False
                    st.session_state.last_click = None
